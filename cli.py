import typer

from robusta_task import shift, matrix, reverse

ENCRYPTION_ALGORITHM = {"shift": shift, "matrix": matrix, "reverse": reverse}
CHOICES = [key for key in ENCRYPTION_ALGORITHM]

app = typer.Typer()


@app.command()
def encrypt(encryption_algorithm: str, text: str):
    enc_type = ENCRYPTION_ALGORITHM.get(encryption_algorithm)
    if not enc_type:
        typer.echo(f"ERROR: Encryption choices are: {CHOICES}")
    else:
        typer.echo(enc_type.encrypt(text))


@app.command()
def decrypt(encryption_algorithm: str, text: str):
    enc_type = ENCRYPTION_ALGORITHM.get(encryption_algorithm)
    if not enc_type:
        typer.echo(f"ERROR: Decryption choices are: {CHOICES}")
    else:
        typer.echo(enc_type.decrypt(text))


if __name__ == "__main__":
    app()
