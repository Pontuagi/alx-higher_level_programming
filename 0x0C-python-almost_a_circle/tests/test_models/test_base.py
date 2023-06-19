import unittest

class TestBase(unittest.TestCase):
    def test_idAssignement(self):
        """
        check auto incrementind id assignement
        test explicit id assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(9)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 9)

    def test_PrivateAttribute(self):
        """ attempt to access private attribute"""
        b1 = Base()

        with self.assertRaises(AttributeError):
            b1.__nb_objects

    def test_invalidIdType(self):
        """ test if TypeError is raised if id is not integer"""
        with self.assertRaises(TypeError):
            Base("id")

    def test_existingId(self):
        """ Test id with same id """
        b1 = Base(1)
        b2 = Base(1)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, 1)


if __name__ = '__main__':
    unittest.main()
