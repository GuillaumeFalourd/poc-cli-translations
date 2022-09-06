from pathlib import Path

HOME = Path.home()
CLI_DIR = HOME / ".poc"
LANGUAGE_FILE = CLI_DIR / "locale"

def main():
    print("Hello World")
    return 0

if __name__ == "__main__":
    main()