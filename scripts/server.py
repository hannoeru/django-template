import subprocess


def main():
    cmd = ["python", "manage.py", "runserver", "3000"]
    subprocess.run(cmd)
