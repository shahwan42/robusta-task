import json

from robusta_task import utils


def to_bits(char: str):
    return ("0" * 16 + bin(ord(char))[2:])[-16:]


def to_char(bits: str):
    return chr(int(bits, 2))


def matrix_multiply(X, Y):
    result = [
        [sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X
    ]
    return [[round(element) for element in row] for row in result]


def encrypt(text: str):
    result = []
    for char in text:
        bits = [[int(bit) for bit in to_bits(char)]]
        result.append(matrix_multiply(bits, utils.matrix))

    return result


def decrypt(encrypted_text: list):
    if type(encrypted_text):
        encrypted_text = json.loads(encrypted_text)

    result = ""
    for enc_char in encrypted_text:
        char_bits = matrix_multiply(enc_char, utils.imatrix)
        result += to_char("".join(str(bit) for bit in char_bits[0]))

    return result


if __name__ == "__main__":
    print(encrypt("ahmed"))
    print(encrypt("Shahwan42"))

    print(decrypt(encrypt("ahmed")))
    print(decrypt(encrypt("Shahwan42")))
