from modules.family_util import print_full_name
from  classes.family import Parent, Child

papa = Parent("Uwe", "Sluga")
mama = Parent("Sabine", "Sluga")
print_full_name(papa.add_child(Child("Anton", "Sluga", papa, mama)))
print_full_name(papa.add_child(Child("Anni", "Sluga", papa, mama)))

for child in papa.get_childs():
    print(child.get_full_name() + 
          " belongs to papa " + child.get_papa().get_full_name() + 
          " and mama " + child.get_mama().get_full_name())
