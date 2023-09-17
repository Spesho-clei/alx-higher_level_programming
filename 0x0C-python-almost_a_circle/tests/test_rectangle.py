#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        rectangle1 = Rectangle(5, 10)
        self.assertEqual(rectangle1.width, 5)
        self.assertEqual(rectangle1.height, 10)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)
        self.assertEqual(rectangle1.id, 1)

        rectangle2 = Rectangle(3, 7, 1, 2, 100)
        self.assertEqual(rectangle2.width, 3)
        self.assertEqual(rectangle2.height, 7)
        self.assertEqual(rectangle2.x, 1)
        self.assertEqual(rectangle2.y, 2)
        self.assertEqual(rectangle2.id, 100)

    def test_width_getter_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

    def test_height_getter_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.height = 20
        self.assertEqual(rectangle.height, 20)

    def test_x_getter_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.x = 2
        self.assertEqual(rectangle.x, 2)

    def test_y_getter_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.y = 3
        self.assertEqual(rectangle.y, 3)

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        rectangle = Rectangle(2, 3, 1, 1)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '\n #\n #\n #\n')

    def test_str(self):
        rectangle = Rectangle(3, 4, 2, 1, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/1 - 3/4")

    def test_update_args(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(10, 2, 2, 2, 2)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

    def test_update_kwargs(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(id=10, width=2, height=2, x=2, y=2)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

    def test_to_dictionary(self):
        rectangle = Rectangle(5, 10, 2, 1, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 1}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
