import sys
from openai import OpenAI

def read_log_message(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def add_context_message(log_message):
    context_message = """
    You are a genious Senior Developer with profound knowledge about debbuging 
    and error messages in all programming languages and you know in detail the inner workings of
    linux kernel and Windows data_structures. You are ONLY tasked to, uppon recieving a log or error 
    message, diagnose the most probable cause of the problem and suggest a correction for a 
    developer. Refrain from any interaction beyound that.You should refrain from using difficult
    terminology. Give instructions that a begginer in that language could follow. Do not
    suggest code, explain whatmust be corrected. Use at most 200 words while conveing clearly
    the diognostics and solution. Begin your response straight with thediagnostics and
    then present the solution.The log message is the following: 
    """
    full_message = context_message+log_message
    return full_message

def make_request_openai(full_message):
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5-nano",
        input=full_message
    )
    return response

def main():
    arguments = sys.argv
    if len(arguments) < 2:
      print("Usage: python main.py <path_to_file>")
      sys.exit(1)
    file_path = arguments[1]
    log_message = read_log_message(file_path)
    full_message = add_context_message(log_message)
    response = make_request_openai(full_message)
    print(response.output_text)

if __name__ == "__main__":
    main()
