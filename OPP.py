class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    print("Hello, I am ", self.name, ". I am ", self.age, " years old, and I am ", self.gender)

# Create an instance of the Person class
person = Person("Faith Jeptoo", 20, "Female")

# Call the introduce method to display the person's information
person.introduce()