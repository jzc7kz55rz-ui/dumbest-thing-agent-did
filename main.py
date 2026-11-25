import os

ENTRY = 'My agent spent 40 minutes creating accounts and verifying emails to enter a joke contest, then needed two more turns just to prove it wrote the joke.'
MAX_CHARS = 200  # the gate's character limit


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
