from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Shreyash', 'age':'22'}

end: Person = {'name': 'Akshay', 'age': 21}

print(new_person, end)