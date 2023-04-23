import flet_material as fm
import unittest


dropdown = fm.Admonitions(
    type_="note", expanded_height=300, expanded=False, controls_list=None
)


class TestButtons(unittest.TestCase):
    def test_parameter_types(self):
        self.assertIsInstance(dropdown.type_, str)
        self.assertIsInstance(dropdown.expanded_height, int)
        self.assertIsInstance(dropdown.expanded, bool)
        self.assertIsInstance(dropdown.controls_list, (list, type(None)))


if __name__ == "__main__":
    unittest.main()
