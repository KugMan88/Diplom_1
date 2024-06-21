from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Бургер "Тетя из Барселоны"', 2000)
        assert bun.get_name() == 'Бургер "Тетя из Барселоны"', 'Unable to get bun name'

    def test_bun_get_price(self):
        bun = Bun('Бургер "Тетя из Барселоны"', 2000)
        assert bun.get_price() == 2000, 'Unable to get bun price'