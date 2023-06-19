from models.rectangle import Rectangle
import unittest

class test_Rectangle(unittest.TestCase):
    """ this class test the rectangle class """
    def test_AttributeAssignment(self):
        """ checki if attributees assign correctly """
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
        """ attemp to access private attribute """
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
        r1 = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            if r1.width <= 0:
                raise ValueError("width must be > 0")
        with self.assertRaises(ValueError):
            if r1.height <= 0:
                raise ValueError("height must be > 0")
        with self.assertRaises(ValueError):
            if r1.x <= 0:
                raise ValueError("x must be >= 0")
        with self.assertRaises(ValueError):
            if r1.y <= 0:
                raise ValueError("y must be >= 0")

        with self.assertRaises(TypeError):
            if not isinstance(r1.width, int):
                raise TypeError("width must be an integer")
        with self.assertRaises(TypeError):
            if not isinstance(r1.height, int):
                raise TypeError("height must be an integer")
        with self.assertRaises(TypeError):
            if not isinstance(r1.y, int):
                raise TypeError("y must be an integer")
        with self.assertRaises(TypeError):
            if not isinstance(r1.x, int):
                raise TypeError("x must be an integer")

    def test_area(self):
        """check if it returns the right area """
        r1 = Rectangle(5, 6, 7, 9)
        self.assertEqual(r1.area, 30)

if __name__ == '__main__':
    unittest.main()
