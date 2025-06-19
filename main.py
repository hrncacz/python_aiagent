import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from prompts import system_prompt
from call_functions import available_functions
from functools import reduce


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("Missing prompt")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [types.Content(
        role="user", parts=[types.Part(text=user_prompt)])]
    verbose = "--verbose" in sys.argv

    for i in range(20):
        cont = generate_content(client, messages, verbose)
        if isinstance(cont, str):
            print(cont)
            return
        elif isinstance(cont, dict):
            candidates = cont["candidates"]
            c_final = list(map(lambda l: l.content, candidates))
            messages += c_final
            messages += cont["function_responses"]


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")
    if not response.function_calls:
        return response.text
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(
                f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result)

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    resp_dict = {"candidates": response.candidates,
                 "function_responses": function_responses}
    return resp_dict


main()
