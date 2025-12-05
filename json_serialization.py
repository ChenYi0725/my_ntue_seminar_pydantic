import pydantic


class UserModel(pydantic.BaseModel):
    name: str
    age: int
    email: (
        pydantic.EmailStr
    )  # pydantic.EmailStr  # 使用內建的 EmailStr 類型來驗證 email 格式 #pip install pydantic[email]


user1 = UserModel(name="Alice", age=25, email="alice@gmail.com")
user1_dict = user1.dict()
user1_json = user1.json()
print("Origin: ", user1)
print("Serialized Dict:", user1_dict)
print("Serialized JSON:", user1_json)


# ============================================
json_string = '{"name":"Bob","age":25,"email":"bob@gmail.com"}'
user2 = UserModel.parse_raw(json_string)
print("Deserialized from JSON:", user2)
