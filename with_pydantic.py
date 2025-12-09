import pydantic


class UserModel(pydantic.BaseModel):
    name: str
    age: int
    email: (
        pydantic.EmailStr
    )  # pydantic.EmailStr  # 使用內建的 EmailStr 類型來驗證 email 格式 #pip install pydantic[email]


# ------
# 查看型別標註（例如 int, str, list[int]）

# 檢查輸入值是否符合該型別

# 若能轉型，就自動轉型（例如 "20" → 20）
# ------


# 正確使用
user1 = UserModel(name="Alice", age=25, email="eason123@gmail.com")

print(user1)
# 錯誤使用，會引發驗證錯誤
try:
    user2 = UserModel(name="Bob", age="twenty-five", email="bob@gmail.com")
except pydantic.ValidationError as e:
    print("Validation Error:", e)

# ===========================================

# ===========================================
try:
    user4 = UserModel(name="David", age=28, email="invalid.email.format")
    print(user4)
except pydantic.ValidationError as e:
    print("Validation Error:", e)
