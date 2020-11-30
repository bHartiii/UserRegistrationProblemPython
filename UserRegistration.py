import re


class UserRegistration:

<<<<<<< HEAD
    def inputValidation(self, string, regex):
        match = re.search(regex, string)
=======
    def validateName(self, regex, name):
        match = re.search(regex, name)
>>>>>>> UC2-LastNameValidation
        if match:
            return string
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
<<<<<<< HEAD
    email_regex = "^\w{3,}(\.\w{3,})*\@[a-z]{2,}\.[a-z]{2,3}(\.[a-z]{2})*$"
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    email = input("Enter your emailId : ")
    print(user.inputValidation(first_name, name_regex))
    print(user.inputValidation(last_name, name_regex))
    print(user.inputValidation(email, email_regex))
=======
    print(user.takeFirstName())
    print(user.takeLastName())
>>>>>>> UC2-LastNameValidation
