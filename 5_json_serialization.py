import pydantic


class User(pydantic.BaseModel):
    name: str
    age: int
    email: pydantic.EmailStr


# ============================================
user1 = User(name="Eason", age=22, email="eason@gmail.com")
user1_dict = user1.model_dump()
user1_json = user1.model_dump_json()
print()
print("Origin: ", user1)
print("Serialized Dict:", user1_dict)
print("Serialized JSON:", user1_json)
print()

# ============================================
json_string = '{"name":"Yi-Tong","age":23,"email":"yitong@gmail.com"}'
user2 = User.model_validate_json(json_string)
print(user2)
print()
# ============================================
user3_info = {
    "name": "Chi-yu",
    "age": 22,
    "email": "chiyu@gmail.com",
}
user3 = User(**user3_info)
print(user3)
print()
