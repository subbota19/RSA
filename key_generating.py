import random

BIT_LEN = 2048
TEST_PRIME_LEN = 50
TEST_COUNT_RABIN_ATTEMPT = 20


class KeyGenerating:
    def __init__(self, bit_len: int = BIT_LEN, test_prime_list_len: int = TEST_PRIME_LEN):
        self.bit_len = bit_len
        self.test_prime_list_len = test_prime_list_len
        self.test_prime_list = self.__generating_prime_list()

    @classmethod
    def get_test(cls) -> list:
        list_with_test = []
        for test_name, test in cls.__dict__.items():
            if test_name.startswith('test'):
                list_with_test.append(test)
        return list_with_test

    def __generating_number(self) -> int:
        return random.randrange(pow(2, self.bit_len - 1) + 1, pow(2, self.bit_len) - 1)

    def __generating_prime_list(self) -> list:
        count = 2
        output_prime_list = []
        while len(output_prime_list) < self.test_prime_list_len:
            for number in output_prime_list:
                if count % number == 0:
                    break
            else:
                output_prime_list.append(count)
            count += 1
        return output_prime_list

    def test_low_level_prime(self, test_number: int) -> bool:
        is_prime_number = False

        for prime_number in self.test_prime_list:
            if test_number % prime_number == 0 and pow(prime_number, 2) <= test_number:
                is_prime_number = True
                break
        return is_prime_number

    def generate_key(self) -> int:
        is_failed_test = True
        test_number = None
        while is_failed_test:
            test_number = self.__generating_number()
            print('new')
            for test in KeyGenerating.get_test():
                if test(self, test_number):
                    break
            else:
                is_failed_test = False
        return test_number


g = KeyGenerating()
print(g.generate_key())
