import re


class UserRegistration:

    def inputValidation(self, string, regex):
        """
        matching string with regex
        :param string:
        :param regex:
        :return string or "not valid" message:
        """
        match = re.search(regex, string)
        if match:
            return string
        else:
            return "Not Valid"


if __name__ == '__main__':
    user = UserRegistration()
    name_regex = "^[A-Z][a-z]{2,}$"
    email_regex = "^\w{3,}(\.\w{3,})*\@[a-z]{2,}\.[a-z]{2,3}(\.[a-z]{2})*$"
    phone_regex = "^91 [6-9][0-9]{9}$"
    password_regex = "(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$"

    first_name = input("Enter your first name : ")
    print(user.inputValidation(first_name, name_regex))
    last_name = input("Enter your last name : ")
    print(user.inputValidation(last_name, name_regex))
    email = input("Enter your emailId : ")
    print(user.inputValidation(email, email_regex))
    phone_no = input("Enter your phone number : ")
    print(user.inputValidation(phone_no, phone_regex))
    password = input("Enter Password : ")
    print(user.inputValidation(password, password_regex))