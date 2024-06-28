from user import User

user = User()

user.register("James, 123456, test@mail.com, abc")

email = input("Enter Your Email ")
password = input("Enter Your Password ")
print(user.login(email, password))


class User:
    pass