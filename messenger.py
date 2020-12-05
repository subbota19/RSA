import yaml, os

from collections import OrderedDict
from rsa_implementation import RSA

HOME_KEY_DIR = "/home/yauheni/PyCharmProjects/student/security/RSA/key_capacity"
ALPHABET = OrderedDict({'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6,
                        'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11,
                        'k': 12, 'l': 13, 'm': 14, 'n': 15, 'o': 16,
                        'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21,
                        'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26,
                        'z': 27})
SEPARATOR = ','


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
        return str(pow(ALPHABET[symbol], e) % n)

    @staticmethod
    def decrypt_symbol(index: int, n: int, d: int) -> str:
        return list(ALPHABET.keys())[pow(index, d) % n - 1]

    def main(self):

        is_generate = int(input('Generate new public and private key? \n 0 - no \n 1 - yes\n'))

        if is_generate:
            self.rsa.run()

        public_key = self.get_key('public_key.yaml')
        private_key = self.get_key('private_key.yaml')

        if not public_key or not private_key:
            raise Exception('Please generate public and private keys!!!')

        case = int(input('Choice option:\n 0 - encrypt \n 1 - decrypt\n'))

        text = input('Input text:\n')

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
        print('Result: {}'.format(SEPARATOR.join(self.output)))


if __name__ == '__main__':
    messenger_obj = Messenger()
    messenger_obj.main()
