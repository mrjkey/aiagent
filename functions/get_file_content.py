import os
from functions.get_files_info import path_norm_valid

MAX_CHARS=10000

def get_file_content(working_directory: str, file_path: str) -> str:
    norm_file, valid_target_dir = path_norm_valid(working_directory, file_path)

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

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Reads and returns the contents of a file relative to the working directory, truncated to {MAX_CHARS} characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
