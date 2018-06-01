class Decode(object):
    def __init__(self, a):
        self.a = a

    @property
    def get_dec(self):
        self.a = int(self.a.decode())
        print('Прием и декодирование чила')
        return self.a

    @property
    def get_enc(self):
        a = int(self.a.encode())
        return a


class Encode_send_sum(Decode):
    def get_sum_en(self, b):
        self.b = b
        return str(self.b + self.a).encode()
