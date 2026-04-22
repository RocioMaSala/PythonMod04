import sys


def transform_data(content: str) -> None:

    print("\nTransform data")
    print("---\n\n")

    lines: list[str] = content.splitlines()
    lines = [line + '#' for line in lines]
    transformed_content = "\n".join(lines)
    print(transformed_content)
    print("\n\n---")

    sys.stdout.write("Enter new file name (or empty):")
    sys.stdout.flush()
    new_file_name = sys.stdin.readline().strip()
    if len(new_file_name) > 0:
        print(f"Saving data to '{new_file_name}'")
        try:
            new_file = open(new_file_name, "w")
            new_file.write(transformed_content)
            print(f"Data saved in file '{new_file_name}'.\n")
            new_file.close()
        except Exception as e:
            print(
                f"[STDERR] Error opening file '{new_file_name}': {e}",
                file=sys.stderr
                )
            print("Data not saved.")
            return

    else:
        print("Not saving data.")


def recover_ancient_text() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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
            print(
                f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
                file=sys.stderr
                )
            return


if __name__ == "__main__":
    recover_ancient_text()
