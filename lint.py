# lint.py

import subprocess

if __name__ == "__main__":
    result = subprocess.run(["flake8", "app.py"])
    exit_code = result.returncode

    if exit_code == 0:
        print("No style issues found.")
    else:
        print("Style issues found.")

    exit(exit_code)
