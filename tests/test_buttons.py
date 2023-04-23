import flet_material as fm
import unittest


button = fm.Buttons(width=220, height=55, title="Give this repo a star!")


class TestButtons(unittest.TestCase):
    def test_parameter_types(self):
        self.assertIsInstance(button.width, int)
        self.assertIsInstance(button.height, int)
        self.assertIsInstance(button.title, str)


if __name__ == "__main__":
    unittest.main()
