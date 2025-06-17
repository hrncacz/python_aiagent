import os
from google import genai
from google.genai import types


def get_file_content(working_directory, file_path):
    path = os.path.join(os.path.abspath(working_directory), file_path)
    if not os.path.abspath(working_directory) in os.path.abspath(path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        try:
            with open(path, "r") as file:
                file_content = file.read()
                if len(file_content) > 10000:
                    file_content = file_content[:10000] + f"\n[...File \"{
                        file_path}\" truncated at 10000 characters]"
                return file_content
        except Exception as e:
            return f"Error: {e}"


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
