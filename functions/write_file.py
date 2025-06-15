import os


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
