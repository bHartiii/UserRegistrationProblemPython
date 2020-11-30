import re


class UserRegistration:
    def validateName(self, name):
        match = re.search("^[A-Z][a-z]{2,}", name)
        if match:
            return name
        else:
            return "Not Valid"


if __name__ == '__main__':
    user = UserRegistration()
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    user.validateName(first_name)
    user.validateName(last_name)
