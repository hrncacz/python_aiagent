import os
import subprocess
from google import genai
from google.genai import types


def run_python_file(working_directory, file_path):
    path = os.path.join(os.path.abspath(working_directory), file_path)
    if not os.path.abspath(working_directory) in os.path.abspath(path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(path):
        return f'Error: File "{file_path}" not found.'
    elif not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    else:
        try:
            result = subprocess.run(
                ['python3', path], capture_output=True, text=True, timeout=30)
            result.check_returncode()
            if result.stdout == None:
                return "No output produced."
            else:
                return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        except subprocess.CalledProcessError as scpe:
            return f"Process exited with code {scpe.returncode}"
        except Exception as e:
            return f"Error: executing Python file: {e}"


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
