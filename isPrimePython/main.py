import unittest


def isPrime(n):

    if n == 1:
        return False

    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


class TestIsPrimeFunction(unittest.TestCase):

    def test_isPrime(self):
        # Тесты для функции isPrime

        # Проверка на простые числа
        self.assertTrue(isPrime(2))  # 2 - простое число
        self.assertTrue(isPrime(17))  # 17 - простое число
        self.assertTrue(isPrime(29))  # 29 - простое число

        # Проверка на составные числа
        self.assertFalse(isPrime(1))  # 1 - не является простым
        self.assertFalse(isPrime(4))  # 4 - не является простым
        self.assertFalse(isPrime(15))  # 15 - не является простым

        # Дополнительные тесты
        self.assertTrue(isPrime(7919))  # 7919 - простое число
        self.assertFalse(isPrime(100))  # 100 - не является простым

if __name__ == '__main__':
    unittest.main()

