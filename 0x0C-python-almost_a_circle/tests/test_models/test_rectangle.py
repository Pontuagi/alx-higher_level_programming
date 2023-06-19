from models.rectangle import Rectangle
import unittest

class test_Rectangle(unittest.TestCase):
    """ this class test the rectangle class """
    def test_AttributeAssignment(self):
        """ checking if attributees assign correctly """
        r1 = Rectangle(1, 2, 4, 5, 8)
        r2 = Rectangle(2, 4)
        r3 = Rectangle (4, 5, 8, 4)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 8)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)


    def test_PrivateAttribute(self):
        """ attempt to access private attribute """
        r1 = Rectangle(4, 5, 6, 7, 3)

        with self.assertRaises(AttributeError):
            r1.__width
        with self.assertRaises(AttributeError):
            r1.__height
        with self.assertRaises(AttributeError):
            r1.__x
        with self.assertRaises(AttributeError):
            r1.__y

    def test_inheritance(self):
        """test if rectangle inherited from base"""
        r1 = Rectangle(1, 2, 4, 7, 9)
        self.assertEqual(r1.id, 9)

    def test_setters(self):
        """check if the setters and getters work fine"""
        r1 = Rectangle(3, 5, 9, 0, 98)
        r1.width = 12
        r1.height = 17
        r1.x = 0
        r1.y = 7
        
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 7)

    def test_inputErrors(self):
        """ check if the values passed are correct and raises correct errors"""
        r1 = Rectangle(1, 6, 2, 3)
        with self.assertRaises(ValueError):
            r1.width = 0
        #        raise ValueError("width must be > 0")
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            r1.x = -10
        with self.assertRaises(ValueError):
            r1.y = -30

        with self.assertRaises(TypeError):
            r1.width = ('a')
        with self.assertRaises(TypeError):
            r1.height = "invalid"
        with self.assertRaises(TypeError):
            r1.y = "false"
        with self.assertRaises(TypeError):
            r1.x = "char"

    def test_area(self):
        """check if it returns the right area """
        r1 = Rectangle(5, 6, 7, 9)
        self.assertEqual(r1.area(), 30)

    def test_update(self):
        """ checks if the update method works correctly"""
        r1 = Rectangle(2, 4, 7, 3, 8)
        r1.update(13, 12, 3, 6, 9)
        self.assertEqual(r1.id, 13)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 9)

        r1.update(4, 8, 4)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 9)

        r1.update(width=1, height=6, x=3, y=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 2)

    def test_str(self):
        """ test if __str__ output is as expected"""
        r1 = Rectangle(2, 4, 5, 7, 9)
        r2 = Rectangle(10, 17, 13, 12, 17)
        
        self.assertEqual(str(r1), '[Rectangle] (9) 5/7 - 2/4')
        self.assertEqual(str(r2), '[Rectangle] (17) 13/12 - 10/17')

if __name__ == '__main__':
    unittest.main()
