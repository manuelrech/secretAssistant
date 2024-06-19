import os
import pyperclip
from openai import OpenAI
from dotenv import load_dotenv
from pynput.keyboard import Key
from prompts import REFINE_PROMPT, ANSWER_PROMPT
from pylatexenc.latex2text import LatexNodes2Text

class ResponseHandler:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.char_buffer = []
        self.last_detailed_response = ""
        self.aggregated_text = ""

    def get_detailed_response(self, text):
        messages = [
            {"role": "system", "content": ANSWER_PROMPT},
            {"role": "user", "content": text}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o",  # Correct model identifier
            messages=messages
        )
        return response.choices[0].message.content.strip()

    def get_concise_response(self, detailed_response, original_text):
        messages = [
            {"role": "user", "content": original_text},
            {"role": "system", "content": REFINE_PROMPT},
            {"role": "user", "content": detailed_response}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o",  # Correct model identifier
            messages=messages,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                self.char_buffer.append(key.char)
                if len(self.char_buffer) > 3:
                    self.char_buffer.pop(0)
                
                sequence = ''.join(self.char_buffer)
                if sequence == '///':
                    if not self.aggregated_text:
                        self.aggregated_text = pyperclip.paste()
                    print("\n\n\n======================================== NEW QUESTION ========================================", flush=True)
                    print(f">>> QUESTION TEXT:\n{self.aggregated_text}", flush=True)

                    detailed_response = self.get_detailed_response(self.aggregated_text)
                    print(">>> LONG ANSWER", flush=True)
                    print(detailed_response, flush=True)
                    self.last_detailed_response = detailed_response

                    concise_response = self.get_concise_response(detailed_response, self.aggregated_text)
                    pyperclip.copy(LatexNodes2Text().latex_to_text(concise_response).replace("**", "").replace('`', ''))
                    print(">>> SHORT ANSWER", flush=True)
                    print(concise_response, flush=True)

                    self.char_buffer = []
                    self.aggregated_text = ""

                elif sequence == ',,,':
                    if self.last_detailed_response:
                        pyperclip.copy(LatexNodes2Text().latex_to_text(self.last_detailed_response).replace("**", ""))
                        print(f">>> ACTION: Required long answer", flush=True)
                    else:
                        self.char_buffer = []
                
                elif sequence == '[[[':
                    copied_text = pyperclip.paste()
                    self.aggregated_text += copied_text + "\n\n"
                    print(f">>> ACTION: added text \n{self.aggregated_text}", flush=True)
                    self.char_buffer = []

                elif sequence == ']]]':
                    self.aggregated_text = ""
                    print(">>> ACTION: cleared clipboard", flush=True)
                    self.char_buffer = []
        except Exception as e:
            print(f"Error: {e}", flush=True)

    def on_release(self, key):
        if key == Key.esc:
            return False