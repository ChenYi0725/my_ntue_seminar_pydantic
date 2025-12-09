import pydantic


class User(pydantic.BaseModel):
    name: str
    age: int
    # ------
    email: pydantic.EmailStr
    password: str
    confirm_password: str
    full_name: str | None = None
    # ------

    @pydantic.field_validator("age")
    def validate_age(cls, value):
        if value <= 0:
            raise ValueError(f"age must be a positive integer:{value}")
        return value

    @pydantic.field_validator("age", mode="before")
    def convert_age_to_int(cls, v):
        return int(v)

    @pydantic.field_validator("name")  # 複雜轉型
    def strip_name(v):
        return v.strip()

    # ----------- model validator（跨欄位驗證）----------- #

    @pydantic.model_validator(mode="after")
    def check_passwords_and_compose_name(self):
        if self.password != self.confirm_password:
            raise ValueError("password and confirm_password must be the same")

        if self.full_name is None:
            self.full_name = self.name.title()  

        return self


user1 = User(
    name="Eason",
    age=23,
    email="eason@gmail.com",
    password="abcd1234",
    confirm_password="abcd1234",
)
print(f"\n{user1}\n")
