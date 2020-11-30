import re


class UserRegistration:
    def takeUserInput(self):
        first_name = input("Enter your first name : ")
        match = re.search("^[A-Z][a-z]{2,}", first_name)
        if match:
            return first_name
        else:
            return "Not Valid"


if __name__ == '__main__':
    user = UserRegistration()
    print(user.takeUserInput())
