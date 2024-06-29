import subprocess
def run_command(command):
    completed_process = subprocess.run(command, capture_output=True, text=True)
    if completed_process.returncode != 0:
        print(f"错误: {completed_process.stderr}")
    else:
        print(f"Success: {completed_process.stdout}")