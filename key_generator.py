import random, datetime

from log import Logging

BIT_LEN = 2048
TEST_PRIME_LEN = 50
TEST_COUNT_RABIN_ATTEMPT = 20

logger = Logging(name=__name__).get_logger()


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
        logger.info('available test(-s) - {}'.format(list_with_test))
        return list_with_test

    def __generating_number(self) -> int:
        logger.info('generate number with bit len - {}'.format(BIT_LEN))
        random.seed(datetime.datetime.now())
        return random.randint(pow(2, self.bit_len - 1) + 1, pow(2, self.bit_len) - 1)

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
        is_prime_number = True

        for prime_number in self.test_prime_list:
            if test_number % prime_number == 0 and pow(prime_number, 2) <= test_number:
                is_prime_number = False
                break
        return is_prime_number

    def test_rabin_miller(self, test_number: int) -> bool:
        component = test_number - 1
        max_divisions_by_two = 0

        while component % 2 == 0:
            component = component // 2
            max_divisions_by_two += 1
        for trials in range(5):
            rand_range = random.randrange(2, test_number - 1)
            pow_number = pow(rand_range, component, test_number)
            if pow_number != 1:
                index = 0
                while pow_number != (test_number - 1):
                    if index == max_divisions_by_two - 1:
                        return False
                    else:
                        index = + 1
                        pow_number = pow(pow_number, 2) % test_number
            return True

    def generate_key(self) -> int:
        is_failed_test = True
        test_number = None
        while is_failed_test:
            test_number = self.__generating_number()
            logger.info('generate number: {}'.format(test_number))
            for test in KeyGenerating.get_test():
                if not test(self, test_number):
                    logger.info('test - {} is failed'.format(test))
                    break
                logger.info('test - {} is passed'.format(test))
            else:
                is_failed_test = False
        return test_number
