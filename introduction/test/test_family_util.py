from modules.family_util import print_full_name
from classes.family import Parent
import unittest

class FamilyUtilTestCase(unittest.TestCase):

    unittest.main()
    
    def test_print_full_name(self):
        full_name = print_full_name(Parent("Uwe", "Sluga"))
        self.assertEqual(full_name, 'Uwe Sluga')
