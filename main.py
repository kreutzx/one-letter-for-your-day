import os

LETTER = "Z"


def main():
    # A one-letter entry must be exactly one alphabetic character.
    assert len(LETTER) == 1 and LETTER.isalpha(), LETTER
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
