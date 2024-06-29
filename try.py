# Python代码示例
import subprocess

# 构建LGPO命令
command = [
    "LGPO.exe", "/t", "Computer", "/v", "Disable",
    "/p", "HKLM\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU",
    "/n", "NoAutoUpdate", "/d", "1"
]

# 运行命令
completed_process = subprocess.run(command, capture_output=True, text=True)

# 打印输出和错误
print("Output:", completed_process.stdout)
print("Error:", completed_process.stderr)
