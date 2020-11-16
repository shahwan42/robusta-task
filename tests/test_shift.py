from robusta_task.shift import encrypt


def test_encrypt():
    assert encrypt("Hello World") == "Khoor Zruog"
    assert encrypt("Ahmed") == "Dkphg"
    assert encrypt("Ziad") == "Cldg"
    assert encrypt("Ahmed Loay Shahwan") == "Dkphg Ordb Vkdkzdq"
