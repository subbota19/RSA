from key_generating import KeyGenerating
import yaml

HOME_KEY_DIR = "/home/yauheni/PyCharmProjects/student/security/RSA/key_capacity"


class RSA:
    def __init__(self):
        self.q = None
        self.p = None
        self.n = None
        self.e = None
        self.public_exponent = None
        self.private_exponent = None

        self.key_gen = KeyGenerating()

    @staticmethod
    def euclid_checker(number_1: int, number_2: int) -> int:
        while number_1 != 0:
            number_1, number_2 = number_2 % number_1, number_1
        return number_2

    @staticmethod
    def save_key(key: list, file_name: str) -> None:
        with open('{}/{}'.format(HOME_KEY_DIR, file_name), 'w') as file:
            yaml.dump({'key': key}, file, default_flow_style=False, sort_keys=False)

    @staticmethod
    def generate_private_exponent(e: int, check_number: int) -> int:

        u1, u2, u3 = 1, 0, e
        v1, v2, v3 = 0, 1, check_number

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

        return u1 % check_number

    def generate_diff_prime_number(self, count: int = 2) -> set:
        output_set = set()
        while len(output_set) != count:
            output_set.add(self.key_gen.generate_key())
        return output_set

    def generate_public_exponent(self, check_number: int) -> int:
        e = None
        is_invalid_number = True
        while is_invalid_number:
            e = self.key_gen.generate_key()
            if self.euclid_checker(e, check_number) == 1:
                is_invalid_number = False
        return e

    def run(self):
        self.q, self.p = self.generate_diff_prime_number()

        self.n = self.q * self.p

        self.e = (self.p - 1) * (self.q - 1)

        self.public_exponent = self.generate_public_exponent(self.e)

        self.save_key(key=[self.n, self.public_exponent], file_name='public_key.yaml')

        self.private_exponent = self.generate_private_exponent(self.public_exponent, self.e)

        self.save_key(key=[self.n, self.private_exponent], file_name='private_key.yaml')
