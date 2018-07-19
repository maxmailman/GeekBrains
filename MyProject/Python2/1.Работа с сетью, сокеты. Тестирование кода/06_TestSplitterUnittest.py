import splitter
import unittest
import val as val


# Модульные тесты
class TestSplitFuction(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов, если необходимо
        pass

    def tearDown(self):
        # Выполнить завершающие действия, если необходимо
        pass

    def testsimpestring(self):
        r = splitter.split("GOOG 100 490.50")
        self.assertEqual(r, ['GOOG', '100', '490.50'])

    def testtypeconvert(self):
        r = splitter.split("GOOG 100 490.50", [str, int, float])
        self.assertEqual(r, ['GOOG', 100, 490.5])

    def testdelimiter(self):
        r = splitter.split("GOOG,100,490.50", delimiter=',')
        self.assertEqual(r, ['GOOG', '100', '490.50'])


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
