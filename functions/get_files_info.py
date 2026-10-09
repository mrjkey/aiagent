import os

def path_norm_valid(working_directory: str, second_path: str) -> tuple(str, bool):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_dir = os.path.join(abs_working_dir, second_path)
        norm_dir = os.path.normpath(full_dir)
        valid_target_dir = os.path.commonpath([abs_working_dir, norm_dir]) == abs_working_dir
    except Exception as e:
        return f"Error: {e}", False

    if not valid_target_dir:
        return f'Error: Cannot list "{second_path}" as it is outside the permitted working directory', False

    return norm_dir, valid_target_dir

def get_files_info(working_directory: str, directory: str = ".") -> str:
    norm_dir, valid_target_dir = path_norm_valid(working_directory, directory)
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(norm_dir):
        return f'Error: "{directory}" is not a directory'

    contents = os.listdir(norm_dir)
    content_strings = []
    for element in contents:
        full_path = os.path.join(norm_dir, element)
        content_strings.append(f"{element}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")
    ret_string = f"Results for {directory} directory:\n"
    for cs in content_strings:
        ret_string += "- " + cs + "\n"

    # return f'Success: "{directory}" is within the working directory'
    return ret_string