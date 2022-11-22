import random           # TODO написать функцию генерации случайных паролей
import string


def get_random_password(n: int = 8) -> str:
    letter_number = string.ascii_letters + string.digits
    password = ''.join(random.sample(letter_number, n))
    return password


print(get_random_password(8))
