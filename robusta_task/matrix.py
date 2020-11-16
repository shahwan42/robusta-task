from robusta_task import utils


def to_bits(char: str):
    return ("0" * 16 + bin(ord(char))[2:])[-16:]


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


if __name__ == "__main__":
    print(encrypt("ahmed"))
    print(encrypt("Shahwan42"))
