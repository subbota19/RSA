import random

BIT_LEN = 2048
TEST_PRIME_LEN = 30


class KeyGenerating:
    def __init__(self, bit_len: int = BIT_LEN, test_prime_list_len: int = TEST_PRIME_LEN):
        self.bit_len = bit_len
        self.test_prime_list_len = test_prime_list_len

    def generating_prime_number(self):
        return random.randrange(pow(2, self.bit_len - 1) + 1, pow(2, self.bit_len - 1))

    def generating_prime_list(self):
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
