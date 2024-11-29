import random


class MarsURLEncoder:
    _symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    _encode_size = 10

    def __init__(self):
        self.urls = dict()

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        hash = [None] * self._encode_size
        key = ''
        while True:
            for i in range(0, self._encode_size):
                hash[i] = random.choice(self._symbols)
            key = ''.join(hash)
            if key not in self.urls:
                break

        self.urls[key] = long_url

        return f'https://ma.rs/{key}'

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        try:
            last_slash = short_url.rindex('/')
            key = short_url[last_slash + 1:]
            if key in self.urls:
                return self.urls[key]
        except ValueError:
            pass

        return None
