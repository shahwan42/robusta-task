from robusta_task.matrix import encrypt


def test_encrypt():
    assert encrypt("ahmed") == [
        [[14, 17, 4, 15, 8, 11, 7, 1, 3, 14, 15, 13, 12, 20, 19, 3]],
        [[15, 12, 12, 14, 15, 15, 14, 9, 6, 14, 12, 8, 8, 20, 17, 5]],
        [[24, 23, 14, 25, 17, 20, 22, 18, 8, 30, 22, 21, 23, 36, 25, 14]],
        [[18, 19, 5, 22, 8, 13, 14, 10, 5, 22, 20, 20, 18, 27, 20, 12]],
        [[13, 10, 4, 18, 6, 10, 13, 10, 5, 14, 15, 14, 9, 18, 13, 12]],
    ]
