import sys


def recover_ancient_text() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            text = open(sys.argv[1])
            print("---\n\n")
            print(text.read())
            print("\n\n---")
            text.close()
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    recover_ancient_text()
