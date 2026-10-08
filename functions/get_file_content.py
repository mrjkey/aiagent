import os

MAX_CHARS=10000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_dir = os.path.join(abs_working_dir, file_path)
        norm_file = os.path.normpath(full_dir)
        valid_target_dir = os.path.commonpath([abs_working_dir, norm_file]) == abs_working_dir
    except Exception as e:
        return f"Error: {e}"

    if not valid_target_dir:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(norm_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    content = ""
    with open(norm_file) as f:
        content = f.read(MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content