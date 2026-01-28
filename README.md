# cli-ai-debugging-assistant
An OpenAI API proof of concept designed to provide usefull guidance on how to solve error messages without leaving the terminal.

## How to use:

python3 app.py /path/to/log

output: up to 200 words of diognostic and solution regarding errors found in the logs

## Example:

\> ./program.cpp 2> error.log  
\> python3 app.py error.log

## Configuration:

   step1: obtain OpenAI API key using this link https://platform.openai.com/api-keys  
   step2: open ~/.bashrc or equivalent file and add a line with 
'''echo OPENAI\_API\_KEY "\<insert your openai api key here\>"'''  
   step3: use '''echo OPENAI\_API\_KEY "\<insert your openai api key here\>"''' to apply change immediately
