def encrypt(text: str):
    words = text.split(" ")
    result = []

    for word in words:
        for char in word:
            if char.isupper():
                result.append(chr((ord(char) + 3 - 65) % 26 + 65))
            else:
                result.append(chr((ord(char) + 3 - 97) % 26 + 97))
        result.append(" ")

    return "".join(result).strip()


def decrypt(encrypted_text: str):
    words = encrypted_text.split(" ")
    result = []

    for word in words:
        for char in word:
            if char.isupper():
                result.append(chr((ord(char) - 3 - 65) % 26 + 65))
            else:
                result.append(chr((ord(char) - 3 - 97) % 26 + 97))
        result.append(" ")

    return "".join(result).strip()


if __name__ == "__main__":
    # Encrypt
    expected1 = "Khoor Zruog"
    result1 = encrypt("Hello World")
    print(result1)
    expected2 = "Dkphg"
    result2 = encrypt("Ahmed")
    print(result2)
    expected3 = "Cldg"
    result3 = encrypt("Ziad")
    print(result3)
    expected4 = "Dkphg Ordb Vkdkzdq"
    result4 = encrypt("Ahmed Loay Shahwan")
    print(result4)
    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3
    assert expected4 == result4

    # Decrypt
    expected5 = "Hello World"
    result5 = decrypt("Khoor Zruog")
    print(result5)
    expected6 = "Ahmed"
    result6 = decrypt("Dkphg")
    print(result6)
    expected7 = "Ziad"
    result7 = decrypt("Cldg")
    print(result7)
    expected8 = "Ahmed Loay Shahwan"
    result8 = decrypt("Dkphg Ordb Vkdkzdq")
    print(result8)
    assert expected5 == result5
    assert expected6 == result6
    assert expected7 == result7
    assert expected8 == result8
