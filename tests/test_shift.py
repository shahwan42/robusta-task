from robusta_task.shift import encrypt, decrypt


def test_encrypt():
    assert encrypt("Hello World") == "Khoor Zruog"
    assert encrypt("Ahmed") == "Dkphg"
    assert encrypt("Ziad") == "Cldg"
    assert encrypt("Ahmed Loay Shahwan") == "Dkphg Ordb Vkdkzdq"


def test_decrypt():
    assert decrypt("Khoor Zruog") == "Hello World"
    assert decrypt("Dkphg") == "Ahmed"
    assert decrypt("Cldg") == "Ziad"
    assert decrypt("Dkphg Ordb Vkdkzdq") == "Ahmed Loay Shahwan"
