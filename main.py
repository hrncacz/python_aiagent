import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Getting content of a selected file up to 10000 characters.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Path to a specific file, relative to working directory. If not providet function will end with error message"
                )
            }
        )
    )
    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Run specified python file.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Path to a specific file, relative to working directory. If not providet function will end with error message"
                )
            }
        )
    )
    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write to a specified file new content.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Path to a specific file, relative to working directory. If not providet function will end with error message"
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="Content which should be written into existing or a new file."
                )
            }
        )
    )
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    if len(sys.argv) < 2:
        print("Missing prompt")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [types.Content(
        role="user", parts=[types.Part(text=user_prompt)])]
    response = client.models.generate_content(
        model=model, contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),)
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")
    function_call_parts = response.function_calls
    for function_call_part in function_call_parts:
        print(f"Calling function: {
              function_call_part.name}({function_call_part.args})")
    if response.text:
        print(f"Response: {response.text}")


main()
