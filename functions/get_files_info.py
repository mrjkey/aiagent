import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_dir = os.path.join(abs_working_dir, directory)
        norm = os.path.normpath(full_dir)
        valid_target_dir = os.path.commonpath([abs_working_dir, norm]) == abs_working_dir
    except Exception as e:
        return f"Error: {e}"

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    return f'Success: "{directory}" is within the working directory'