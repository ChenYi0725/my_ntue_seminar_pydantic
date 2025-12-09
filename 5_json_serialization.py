import pydantic


class User(pydantic.BaseModel):
    name: str
    age: int
    email: pydantic.EmailStr


user1 = User(name="Alice", age=25, email="alice@gmail.com")
user1_dict = user1.model_dump()
user1_json = user1.model_dump_json()
print("Origin: ", user1)
print("Serialized Dict:", user1_dict)
print("Serialized JSON:", user1_json)


# ============================================
json_string = '{"name":"Bob","age":25,"email":"bob@gmail.com"}'
user2 = User.model_validate_json(json_string)
print("Deserialized from JSON:", user2)


user3_info = {
    "name": "Charlie",
    "age": 30,
    "email": "charlie@gmail.com",
}  # 丟去json serialization.py
user3 = User(**user3_info)
print(user3)
