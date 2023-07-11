import flet_material as fm
import unittest


dropdown = fm.Admonitions(
    type_="note", expanded_height=300, expand=False, components=None
)


class TestButtons(unittest.TestCase):
    def test_parameter_types(self):
        self.assertIsInstance(dropdown.type_, str)
        self.assertIsInstance(dropdown.expanded_height, int)
        self.assertIsInstance(dropdown.components, (list, type(None)))


if __name__ == "__main__":
    unittest.main()
