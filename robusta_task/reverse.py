import requests


def encrypt(text: str):
    resp = requests.post(
        "http://backendtask.robustastudio.com/encode", json={"string": text}
    )
    return resp.json().get("string")


def decrypt(encrypted_text: str):
    resp = requests.post(
        "http://backendtask.robustastudio.com/decode", json={"string": encrypted_text}
    )
    return resp.json().get("string")


if __name__ == "__main__":
    assert encrypt("Hello world") == "dlrow olleH"
    assert decrypt("dlrow olleH") == "Hello world"
