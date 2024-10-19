class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"i am a cat,my name is {self.name}. i am {self.age} years old")
    def make_sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"i am a dog,my name is {self.name}. i am {self.age} years old")
    def make_sound(self):
        print("bark")
c = cat("dodo",2)
d = dog("cookie",4)
for animal in(c,d):
    animal.make_sound()
    animal.intro()