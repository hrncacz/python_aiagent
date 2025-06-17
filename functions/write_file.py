import os
from google import genai
from google.genai import types


def write_file(working_directory, file_path, content):
    path = os.path.join(os.path.abspath(working_directory), file_path)
    if not os.path.abspath(working_directory) in os.path.abspath(path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    else:
        try:
            file_path_arr = file_path.split("/")
            subdir = os.path.abspath(working_directory)
            if len(file_path_arr) > 1:
                for part_dir in file_path_arr[:len(file_path_arr) - 1]:
                    subdir = os.path.join(subdir, part_dir)
                    if not os.path.exists(subdir):
                        os.mkdir(subdir)
            with open(path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        except Exception as e:
            return f"Error: {e}"


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
