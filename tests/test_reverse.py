from unittest.mock import patch, Mock

from robusta_task.reverse import encrypt, decrypt


@patch(
    "robusta_task.reverse.requests.post",
    return_value=Mock(json=Mock(return_value={"string": "dlrow olleH"})),
)
def test_encrypt(mock_post):
    assert encrypt("Hello world") == "dlrow olleH"
    mock_post.assert_called()


@patch(
    "robusta_task.reverse.requests.post",
    return_value=Mock(json=Mock(return_value={"string": "Hello world"})),
)
def test_decrypt(mock_post):
    assert decrypt("dlrow olleH") == "Hello world"
    mock_post.assert_called()
