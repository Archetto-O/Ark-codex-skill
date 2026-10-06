"""Install the downloadable deskpet's runtime in its own virtual environment."""

import argparse
import os
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--python", default=sys.executable)
    args = parser.parse_args()
    venv = args.project / ".venv"
    if not venv.exists():
        subprocess.check_call([args.python, "-m", "venv", str(venv)])
    python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    subprocess.check_call([str(python), "-m", "pip", "install", "PySide6==6.11.2"])
    print("Environment ready. Run 启动桌宠.bat to start the pet.")


if __name__ == "__main__":
    main()
