def ceaser(text, shift_key):
    result = ""
    words = text.split()
    print(words)
    cwords = []
    for i in words:
        result = ""
        for char in i:
            print(char)
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) + shift_key - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + shift_key - 97) % 26 + 97)
            else:
                result += char
        print(f"{cwords},{result}")
        cwords.append(result)
    return " ".join(cwords)


print("This cipher only converts alphabets to a ciphered text. \n"
      "Any number or special character given in the text will be as it is.\n")
plain_text = input("Enter the text to convert it into cipher text: ")
key = int(input("Enter shift key: "))
print()
cipher_text = ceaser(plain_text, key)

print(f"Plain Text: {plain_text} \n"
      f"Letter Shift Count: {key} \n"
      f"Cipher Text: {cipher_text}")
