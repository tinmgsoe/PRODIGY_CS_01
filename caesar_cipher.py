def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            shifted = (ord(char) - start + shift * (-1 if decrypt else 1)) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").upper()
        if choice == 'Q':
            break
        elif choice == 'E':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, decrypt=True)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
