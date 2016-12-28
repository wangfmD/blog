import unittest

class TestMgr(unittest.TestCase):
    def test_a(self):
        a = 2
        self.assertEqual(a,2,'=====error====')

if __name__ == '__main__':
    unittest.main()