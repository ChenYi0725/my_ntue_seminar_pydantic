# python 是動態型別的語言

num = 10

print(type(num))
num = "10"
print(type(num))


# ===========================================
# python 的型別註記(type hinting)是給開發者和工具使用的，python執行時不會檢查
class Person:
    def __init__(self, name: str, age: int):  # 單純型別註記，python執行時不會檢查
        self.name: str = name  # 單純型別註記
        self.age: int = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


user = Person("Eason", 22)
print(user)
print(user.greet())
user = Person("Eason", "twenty-two")  # 不會報錯
print(user.greet())

# ===========================================
# dataclass 的型別註記(type hinting)也是給開發者和工具使用的，python執行時不會檢查
from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    age: int


dog = Animal("Buddy", 3)
print(dog)
cat = Animal("Kitty", "three")  # 不會報錯
print(cat)


# ===========================================
# python 的檢查方式
def type_checking_example_int(x: int):
    if not isinstance(x, int):
        raise TypeError("x must be int")


def type_checking_example_str(x: str):
    if not isinstance(x, str):
        raise TypeError("x must be str")
