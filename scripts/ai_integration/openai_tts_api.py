from os import path


def main() -> int:
    key_file_path = path.join(path.dirname(path.realpath(__file__)), "api_key")
    with open(key_file_path) as api_key:
        key = api_key.readline().strip()

    return 0


if __name__ == "__main__":
    main()
