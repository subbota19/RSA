from key_generating import KeyGenerating


class RSA:
    def __init__(self):
        self.q = None
        self.p = None
        self.n = None
        self.e = None
        self.key_gen = KeyGenerating()

    @staticmethod
    def euclid_checker(number_1, number_2):
        while number_1 != 0:
            number_1, number_2 = number_2 % number_1, number_1
        return number_2

    def generate_diff_prime_number(self, count=2):
        output_set = set()
        while len(output_set) != count:
            output_set.add(self.key_gen.generate_key())
        return output_set

    def generate_public_exponent(self, check_number):
        e = None
        is_invalid_number = True
        while is_invalid_number:
            e = self.key_gen.generate_key()
            if self.euclid_checker(e, check_number) == 1:
                is_invalid_number = False
        return e

    def generate_private_exponent(self, check_number):
        e = None
        is_invalid_number = True
        while is_invalid_number:
            e = self.key_gen.generate_key()
            if self.euclid_checker(e, check_number) == 1:
                is_invalid_number = False
        return e

    def main(self):
        self.q, self.p = self.generate_diff_prime_number()

        self.n = self.q * self.p

        self.e = self.generate_public_exponent((self.p - 1) * (self.q - 1))


rsa = RSA()
rsa.main()
print(rsa.q, rsa.p)
