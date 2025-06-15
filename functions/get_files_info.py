import os


def get_files_info(working_directory, directory=None):
    path = os.path.join(os.path.abspath(working_directory), directory)
    if not os.path.abspath(working_directory) in os.path.abspath(path):
        return(f'Error: Cannot list "{
              directory}" as it is outside the permitted working directory')
    elif not os.path.isdir(path):
        return(f'Error: "{directory}" is not a directory')
    else:
        directory_content_arr = os.listdir(path)
        formated_output = list(map(lambda l: f"- {l}: file_size:{os.path.getsize(os.path.join(path, l))} bytes, is_dir={os.path.isdir(os.path.join(path, l))}",directory_content_arr))
        return "\n".join(formated_output)
