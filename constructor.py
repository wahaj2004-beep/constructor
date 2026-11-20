class Family:
    def __init__(self,first_name,last_name,age,relation):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self_relation=relation

    def full_name(self):
        return self.first_name+ " " + self.last_name

father=Family("John", "parr", 49, "father")
mother=Family("Catherine", "parr", 30,"mother")
print("the name of the father is", father.first_name)
print("the name of the mother is", mother.first_name)