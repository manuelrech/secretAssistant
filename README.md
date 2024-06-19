# secretAssistant
Educational purposes only ;)

![Demo](demo/smartAssistantDemo.gif)

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
2. Create a virtual environment and activate it
   ```sh
   python3 -m venv .secretAss
   source .secretAss/bin/activate
   ```
3. Install dependencies
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

## Extra for Mac users


You can have an undercover app that runs all this in the background and logs everything in a log file.

![app](demo/automator_application.png)

### Instructions
1. You should create a file called `run.sh` like the following (change the paths accordingly, in case I will create a version with relative paths).
   ```sh
   #!/bin/bash

   # Define the log file path with timestamp
   LOG_FILE="/Users/manuel/dev/secretAss/logs/log_file_$(date +%Y%m%d_%H%M%S).txt"

   # Ensure the Python script has the correct environment
   source /Users/Manuel/dev/secretAss/.smartAss/bin/activate

   # Run the Python script and redirect both stdout and stderr to the log file
   /Users/Manuel/dev/smartAss/.secretAss/bin/python /Users/Manuel/dev/secretAss/main.py > "$LOG_FILE" 2>&1
   ```
2. Create a folder called `logs`.
3. Open Automator.
4. Click new document.
5. Choose application.
6. Select the action 'Run Shell Script'
7. Paste the path to your run file. (For me it is '/Users/Manuel/dev/smartAss/run_script.sh')
8. Save your application and run it!

Note: I am saying for Mac because it is what I use, but for sure that is also available somehow on windows, feel free to contribute. 