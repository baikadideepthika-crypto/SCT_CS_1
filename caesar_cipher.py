def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'd':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def main():
    print("=" * 40)
    print("   Caesar Cipher - SkillCraft Technology")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  E - Encrypt")
        print("  D - Decrypt")
        print("  Q - Quit")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == 'q':
            print("\nGoodbye!")
            break
        elif choice in ('e', 'd'):
            message = input("Enter your message: ")
            while True:
                try:
                    shift = int(input("Enter shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Please enter a number between 1 and 25.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            mode = 'e' if choice == 'e' else 'd'
            output = caesar_cipher(message, shift, mode)

            action = "Encrypted" if choice == 'e' else "Decrypted"
            print(f"\n{action} Message: {output}")
        else:
            print("Invalid choice. Please enter E, D, or Q.")


if __name__ == "__main__":
    main()
