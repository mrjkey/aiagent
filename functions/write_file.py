import os
from functions.get_files_info import path_norm_valid

def write_file(working_directory: str, file_path: str, content: str) -> str:
    norm_file, valid_target_dir = path_norm_valid(working_directory, file_path)
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'


    if os.path.isdir(norm_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    with open(norm_file, "w") as f:
        result = f.write(content)
        if result > 0:
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    return "Error: something went wrong"


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file relative to the working directory, creating the file or overwriting it if it already exists",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
