
class Auto(object):
    def __init__(self):
        self._marke = None

    def hupen(self):
        print('Hup....Hup')


class Opel(Auto):

    def __init__(self):
        self._marke = 'Opel'


class Ferrari(Auto):
    def __init__(self):
        self._marke = 'Ferrari'

    def hupen(self):
        print('Brrrrrrrrrrrr!!')


class Vw(Auto):
    def __init__(self):
        self._marke = 'vw'

    def hupen(self):
        print('Pffffffffffff!')


class Nissan(Auto):
    def __init__(self):
        self._marke = 'nissan'

    def hupen(self):
        print('hust hust hust!')


class AutoFactory(object):
    @staticmethod
    def create_auto(self, marke):
        if marke == 'opel':
            return Opel()
        elif marke == 'ferrari':
            return Ferrari()
        elif marke == 'vw':
            return Vw()
        elif marke == 'nissan':
            return Nissan()


if __name__ == '__main__':
    print('----> create opel <-----')
    auto = AutoFactory().create_auto('opel')
    print(auto._marke)
    auto.hupen()
    print('----> create ferrari <-----')
    auto = AutoFactory().create_auto('ferrari')
    print(auto._marke)
    auto.hupen()
    print('----> create vw <-----')
    auto = AutoFactory().create_auto('vw')
    print(auto._marke)
    auto.hupen()
    print('\nENDE\n')