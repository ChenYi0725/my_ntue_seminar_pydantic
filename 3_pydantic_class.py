import pydantic


class PydanticUser(pydantic.BaseModel):
    name: str
    age: int

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class OriginUser:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # def __repr__(self) -> str:
    #     return f"name={self.name}, age={self.age}"


user1 = PydanticUser(name="Eason", age="22")
# user2 = PydanticUser(name="Yi-Tong", age="twenty-three")
user2 = OriginUser(name="Chi-yu", age=22)
print(type(user1.age))


# print(user1.greet())
