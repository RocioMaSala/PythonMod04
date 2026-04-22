def secure_archive(name: str, mode: str, content: str) -> tuple[bool, str]:
    if mode == "r":
        try:
            with open(name, mode) as file:
                data = file.read()
                print("Using 'secure_archive' to read from a regular file:")
                return (True, data)
        except FileNotFoundError as e:
            print("Using 'secure_archive' to read from a nonexistent file:")
            return (False, str(e))
        except PermissionError as e:
            print("Using 'secure_archive' to read from an inaccessible file:")
            return (False, str(e))
        except Exception as e:
            return (False, str(e))

    elif mode == "w":
        try:
            with open(name, mode) as file:
                print(
                    "Using 'secure_archive' to write previous content "
                    "to a new file:")
                file.write(content)
                return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    return (False, "Invalid mode")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print(secure_archive("foo", "r", "none"))
    print()

    print(secure_archive("privado", "r", "none"))
    print()

    print(secure_archive("txt", "r", "none"))
    print()

    print(secure_archive("nuevo", 'w', 'hola'))
    print()
