import re


class UserRegistration:

    def validateName(self, regex, name):
        match = re.search(regex, name)
        if match:
            return name
        else:
            return "Not Valid"

    def takeFirstName(self):
        first_name = input("Enter your first name : ")
        return user.validateName(name_regex, first_name)

    def takeLastName(self):
        last_name = input("Enter your last name : ")
        return user.validateName(name_regex, last_name)


if __name__ == '__main__':
    user = UserRegistration()
    name_regex = "^[A-Z][a-z]{2,}"
    print(user.takeFirstName())
    print(user.takeLastName())
