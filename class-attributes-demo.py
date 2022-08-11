class Pet:
    categories = ["bird","cat","dog"]    # a class attribute
    def __init__(self, name, category):
        if category not in Pet.categories:
            raise ValueError(f"{category} is not in pet categories")
        self.name = name
        self.category = category
        
    def set_category(self, category):
        if category not in Pet.categories:
            raise ValueError(f"{category} is not in pet categories")
        self.category = category


lucky = Pet("Lucky", "dog")
print(lucky.name)
print(lucky.category)

missy = Pet("Missy","bird")
print(missy.name)
print(missy.category)

# missy.set_category("lion")  # raise value error, we must append Pet categories
# print(miss.category)

# we can set category here both from instance and class

Pet.categories.append("lion") 
missy.set_category("lion")
print(missy.category)

lucky.categories.append("cow")
lucky.set_category("cow")
print(Pet.categories)
print(lucky.category)