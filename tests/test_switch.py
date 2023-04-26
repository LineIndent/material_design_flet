import flet as ft
import flet_material as fm
import unittest


switch = fm.Switchs()


class TestButtons(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual(switch.width, 54)
        self.assertEqual(switch.height, 25)
        self.assertEqual(switch.border_radius, 25)
        self.assertEqual(switch.bgcolor, "white10")
        self.assertEqual(switch.padding, 4)
        self.assertEqual(switch.clip_behavior, ft.ClipBehavior.HARD_EDGE)

    def test_parameter_types(self):
        # Test if switch is an instance of the Switchs class:
        self.assertIsInstance(switch, fm.Switchs)


if __name__ == "__main__":
    unittest.main()
