import pydantic


class UserModel(pydantic.BaseModel):
    name: str
    age: int
    email: (
        pydantic.EmailStr
    )  # pydantic.EmailStr  # 使用內建的 EmailStr 類型來驗證 email 格式 #pip install pydantic[email]
    # ------
    password: str
    confirm_password: str
    full_name: str | None = None  # 用來示範「自動補齊」
    # ------

    @pydantic.field_validator("age")  # 強制範圍限制、基本驗證
    def validate_age(cls, value):
        if value <= 0:
            raise ValueError(f"age must be a positive integer:{value}")
        return value

    @pydantic.field_validator("name")  # 複雜轉型
    def strip_name(cls, v):
        return (
            v.strip()
        )  # => 用來移除字串開頭和結尾的空白字元 (可以做其他變動，像是加上字元等等)

    @pydantic.field_validator("age")  # 跨型別修改
    def convert_age_to_int(cls, v):
        return int(v)  # => 自動將輸入值轉換為整數

    # ----------- model validator（跨欄位驗證）----------- #

    @pydantic.model_validator(mode="after")
    def check_passwords_and_compose_name(self):
        # 1. 檢查：密碼與確認密碼是否一致
        if self.password != self.confirm_password:
            raise ValueError("password 與 confirm_password 必須相同")

        # 2. 自動補齊：如果 full_name 沒有提供，自動用 name 產生
        if self.full_name is None:
            self.full_name = self.name.title()  # 簡單把名字做格式化

        return self


user1 = UserModel(
    name="   alice ",
    age="23.9",
    email="alice@example.com",
    password="abcd1234",
    confirm_password="abcd1234",
)
print(user1)
