from classes.family import Parent, Child
import unittest


class FamilyTestCase(unittest.TestCase):
    
    unittest.main
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.papa = Parent("Uwe", "Sluga")
        self.mama = Parent("Sabine", "Sluga")
        self.papa.add_child(Child("Anton", "Sluga", self.papa, self.mama))
        self.mama.add_child(Child("Anni", "Sluga", self.papa, self.mama))
        self.papaFirstChild = self.papa.get_childs()[0]
        self.mamaFirstChild = self.mama.get_childs()[0]
        self.papaSecondChild = self.papa.get_childs()[1]
        self.mamaSecondChild = self.mama.get_childs()[1]
        print(self.papa.get_full_name())
        print(self.mama.get_full_name())
    
    def test_get_childs(self):
        self.assertEqual(self.papaFirstChild, self.mamaFirstChild)
        self.assertEqual(self.papaSecondChild, self.mamaSecondChild)
    
    def test_get_childs_same_papa(self):
        self.assertEqual(self.papaFirstChild.get_papa(), self.papaSecondChild.get_papa())
        self.assertEqual(self.mamaFirstChild.get_papa(), self.mamaSecondChild.get_papa())
        
    def test_get_childs_same_mama(self):
        self.assertEqual(self.papaFirstChild.get_mama(), self.papaSecondChild.get_mama())
        self.assertEqual(self.mamaFirstChild.get_mama(), self.mamaSecondChild.get_mama())
