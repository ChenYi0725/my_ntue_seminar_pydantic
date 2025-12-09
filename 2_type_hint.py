from datetime import datetime


class User:
    def __init__(self, name: str, age: int, id: int):
        self.name: str = name
        self.age: int = age
        if not isinstance(id, int):
            raise TypeError("id must be int")

    def greet(self) -> str:
        return f"Hello, I am {self.name} and I am {self.age} years old."

    def get_birth_year(self) -> int:
        return int(datetime.now().year) - self.age


user1 = User("Eason", 22, 1)
user2 = User("Chi-yu", "twenty-two", 2)  # <---- 不會報錯

print(user1.greet())
print(user2.greet())

# print("Birth Year:", user1.get_birth_year(), end="\n\n")
# print("Birth Year:", user2.get_birth_year())
