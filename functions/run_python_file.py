import os
from functions.get_files_info import path_norm_valid
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        norm_file, valid_target_dir = path_norm_valid(working_directory, file_path)

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(norm_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not norm_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", norm_file]
        if args is not None and len(args) > 0:
            command.extend(args)

        result = subprocess.run(
            command, cwd=working_directory, capture_output=True, text=True, timeout=30
        )

        output = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        else:
            output.append(f"STDOUT: {result.stdout}")
            output.append(f"STDERR: {result.stderr}")

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"



