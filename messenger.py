import yaml, os

from collections import OrderedDict
from log import Logging
from rsa_implementation import RSA

HOME_KEY_DIR = "/home/yauheni/PyCharmProjects/student/security/RSA/key_capacity"
ALPHABET = OrderedDict(
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
     'z': 26}
)
SEPARATOR = ','

logger = Logging(name=__name__).get_logger()


class Messenger:
    def __init__(self):
        self.rsa = RSA()
        self.output = []

    @staticmethod
    def get_key(file_name: str) -> dict:
        output_dict = {}
        if os.path.exists('{}/{}'.format(HOME_KEY_DIR, file_name)):
            with open('{}/{}'.format(HOME_KEY_DIR, file_name), 'r')as file:
                output_dict = yaml.load(file, Loader=yaml.FullLoader)
        return output_dict

    @staticmethod
    def encrypt_symbol(symbol: str, n: int, e: int) -> str:
        try:
            return str(pow(ALPHABET[symbol], e) % n)
        except KeyError:
            raise Exception('Undefined symbol - {}'.format(symbol))

    @staticmethod
    def decrypt_symbol(index: int, n: int, d: int) -> str:
        try:
            return list(ALPHABET.keys())[pow(index, d) % n - 1]
        except IndexError:
            logger.info('your private key or public key is wrong')
            raise Exception('Decrypt error')

    def main(self):

        logger.info('Program was starting...')

        is_generate = int(input('Generate new public and private key? \n 0 - no \n 1 - yes\n'))

        if is_generate:
            self.rsa.run()

        public_key = self.get_key('public_key.yaml')
        private_key = self.get_key('private_key.yaml')

        logger.info('export from key_capacity: public key:{}\tprivate key:{}'.format(public_key, private_key))

        if not public_key or not private_key:
            raise Exception('Please generate public and private keys!!!')

        case = int(input('Choice option:\n 0 - encrypt \n 1 - decrypt\n'))

        text = input('Input text:\n')

        logger.info('user text: {} with option {}'.format(text, case))

        if case:
            text = [int(symbol) for symbol in text.split(SEPARATOR)]

        for symbol in text:
            function = {0: self.encrypt_symbol, 1: self.decrypt_symbol}
            parameters = {0: (symbol, public_key['key'][0], public_key['key'][1]),
                          1: (symbol, private_key['key'][0], private_key['key'][1])}
            if function.get(case, None):
                self.output.append(function[case](*parameters[case]))
            else:
                print('Please choice 0 or 1 option')
        print('Result: {}'.format(self.output))
        print('Result with separator: {}'.format(SEPARATOR.join(self.output)))
        logger.info('Result: {}'.format(self.output))


if __name__ == '__main__':
    messenger_obj = Messenger()
    messenger_obj.main()
