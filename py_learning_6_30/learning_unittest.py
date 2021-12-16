import unittest
import CheckName


class Check(unittest.TestCase):
    def test_check_name_function(self):
        full_name = CheckName.get_name()
        self.assertEqual(full_name, 'Janis Joplin')
