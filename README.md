# secretAssistant

![Demo](video_demo/smartAssistantDemo.gif)

`secretAssistant` is a productivity tool that leverages the OpenAI API to provide quick and concise answers to your clipboard content. By utilizing simple keyboard commands, you can query, refine, and retrieve detailed responses from GPT-4o.

## Features

- **Trigger Answer Generation (`///`)**: Automatically sends the content of your clipboard as a query to OpenAI's GPT-4o, and receives both a detailed and a concise response.
- **Add More Content (`[[[`)**: Allows you to add additional text to your query incrementally.
- **Retrieve Detailed Response (`,,,`)**: Fetches the detailed response generated by the initial query.
- **Clear Aggregated Text (`]]]`)**: Clears the aggregated text buffer.

## How It Works

1. **Initialize a Query**:
   - Type `///` to send the current clipboard content as a query.
   - The tool will output a detailed answer and a refined, concise answer.
   - The concise answer will be copied back to your clipboard.

2. **Retrieve Detailed Response**:
   - Type `,,,` to copy the detailed response to your clipboard.

3. **Add More Content**:
   - Type `[[[` to add the current clipboard content to an aggregated text buffer.
   - Keep adding portions of text by typing `[[[`.
   - Finally send it with `///`. 

4. **Clear Aggregated Text**:
   - Type `]]]` to clear the aggregated text buffer.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/manuelrech/secretAssistant.git
   cd secretAssistant
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   - Create an `.env` file in the root directory of the project.
   - add your OpenAI key to the `.env` file.
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
```sh
python3 main.py
````

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or enhancements.

## Contact
For any questions or inquiries, please contact rech.manuel.27@gmail.com