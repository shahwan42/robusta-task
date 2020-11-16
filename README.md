# Robusta Task

## Prepare

> On Ubuntu

- Install Python 3.8, then
- `$ pip install poetry`
- `$ poetry install`
- `$ poetry shell`

> Using Docker

- Make sure docker is installed, cd into the project directory, then
- `$ docker build -t robusta_task .`
- `$ docker run -it robusta_task`
- `$ poetry shell` to activate the virtualenv inside the container

## Run

- `$ python cli.py encrypt/decrypt ALGORITHM TEXT/ENCRYPTED_TEXT`

## Examples

### Shift Algorithm

- `$ python cli.py encrypt shift 'Hello world'`
- `$ python cli.py decrypt shift 'Khoor zruog'`

### Matrix Algorithm

- `$ python cli.py encrypt matrix 'shahwan42'`
- `$ python cli.py decrypt matrix '[[[27, 26, 15, 20, 18, 20, 14, 3, 14, 25, 22, 22, 21, 33, 28, 5]], [[15, 12, 12, 14, 15, 15, 14, 9, 6, 14, 12, 8, 8, 20, 17, 5]], [[14, 17, 4, 15, 8, 11, 7, 1, 3, 14, 15, 13, 12, 20, 19, 3]], [[15, 12, 12, 14, 15, 15, 14, 9, 6, 14, 12, 8, 8, 20, 17, 5]], [[31, 28, 16, 27, 18, 22, 21, 12, 16, 33, 27, 29, 27, 40, 29, 14]], [[14, 17, 4, 15, 8, 11, 7, 1, 3, 14, 15, 13, 12, 20, 19, 3]], [[23, 16, 17, 23, 24, 21, 27, 20, 10, 28, 20, 15, 20, 34, 21, 16]], [[19, 15, 8, 17, 3, 14, 9, 9, 13, 19, 13, 18, 11, 22, 11, 9]], [[19, 15, 11, 12, 12, 16, 8, 2, 13, 17, 11, 11, 11, 22, 13, 2]]]'`

### Reverse Algorithm

- `$ python cli.py encrypt reverse "Hello world"`
- `$ python cli.py decrypt reverse "dlrow olleH"`
