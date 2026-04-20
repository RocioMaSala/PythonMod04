import sys


def transform_data(content: str) -> None:

    print("\nTransform data")
    print("---\n\n")

    lines: list[str] = content.splitlines()
    lines = [line + '#' for line in lines]
    transformed_content = "\n".join(lines)
    print(transformed_content)
    print("\n\n---")

    new_file_name = input("Enter new file name (or empty):")
    if len(new_file_name) > 0:
        new_file = open(new_file_name, "w")
        print(f"Saving data to {new_file_name}")
        new_file.write(transformed_content)
        print(f"Data saved in file '{new_file_name}'.\n")
        new_file.close()
    else:
        print("Not saving data.")


def recover_ancient_text() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            text = open(sys.argv[1])
            content = text.read()
            text.close()

            print("---\n\n")
            print(content)
            print("\n\n---")
            print(f"File '{sys.argv[1]}' closed.")

            transform_data(content)

        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return


if __name__ == "__main__":
    recover_ancient_text()
