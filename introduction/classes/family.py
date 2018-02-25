from classes.person import Person

class Child(Person):
    
    def __init__(self, first_name, last_name, parent_papa, parent_mama):
        super().__init__(first_name, last_name)
        self.parent_papa = parent_papa
        self.parent_mama = parent_mama
        
    def get_papa(self):
        return self.parent_papa
    
    def get_mama(self):
        return self.parent_mama
                 

class Parent(Person):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.childs = []
        
    def add_child(self, child):
        if child not in child.parent_papa.childs:
            child.parent_papa.childs.insert(0, child)
        if child not in child.parent_mama.childs:
            child.parent_mama.childs.insert(0, child)
        return child
        
    def get_childs(self):
        return self.childs