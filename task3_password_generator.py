"""Task 3: Password generator with length and complexity options."""
import secrets
import string

LEVELS = {
    "1": ("Low (letters only)", string.ascii_letters),
    "2": ("Medium (letters + digits)", string.ascii_letters + string.digits),
    "3": ("High (letters + digits + symbols)",
          string.ascii_letters + string.digits + string.punctuation),
}


def generate_password(length, charset, ensure_mix=True):
    while True:
        pwd = "".join(secrets.choice(charset) for _ in range(length))
        if not ensure_mix:
            return pwd
        # make sure every character class in the charset appears (when possible)
        classes = [string.ascii_lowercase, string.ascii_uppercase,
                   string.digits, string.punctuation]
        needed = [c for c in classes if any(ch in c for ch in charset)]
        if length < len(needed) or all(any(ch in c for ch in pwd) for c in needed):
            return pwd


def main():
    print("===== PASSWORD GENERATOR =====")
    while True:
        try:
            length = int(input("Desired password length (4-128): "))
            if not 4 <= length <= 128:
                raise ValueError
        except ValueError:
            print("Enter a whole number between 4 and 128.")
            continue

        print("\nComplexity:")
        for k, (name, _) in LEVELS.items():
            print(f"  {k}. {name}")
        level = input("Choose complexity (1-3): ").strip()
        if level not in LEVELS:
            print("Invalid choice.\n")
            continue

        print(f"\nGenerated password: {generate_password(length, LEVELS[level][1])}")
        if input("\nGenerate another? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
