from .validators import validate_email_user, validate_password_user, validate_strong_password

class UserCreateSerializer:

    def __init__(self, data) -> None:
        self.data = data
        self.validated_data = dict()
        self.errors = dict()

    def is_valid(self):
        username = self.data.get("username")
        first_name = self.data.get("first_name")
        email = self.data.get("email")
        password = self.data.get("password")

        required_fields = ["username", "first_name", "password", "email"]

        for field in required_fields:
            if not self.data.get(field):
                self.errors.setdefault(field, [])
                self.errors[field].append("Required field")

        password_error = validate_password_user(password, username, first_name, email)
        password_not_strong = validate_strong_password(password)

        if password_error and password_not_strong:
            self.errors.setdefault("password", [])
            self.errors["password"].extend(password_error)
            self.errors["password"].extend(password_not_strong)

        email_error = validate_email_user(email)

        if email_error:
            self.errors.setdefault("email", [])
            self.errors["email"].extend(email_error)

        if self.errors:
            return False

        self.validated_data = {
            "username": username,
            "first_name": first_name,
            "email": email,
            "password": password
        }

        return True

class UserLoginSerializer:

    @staticmethod
    def username_and_password_is_valid(username, password):

        errors = {
            'username': list(),
            'password': list()
        }

        if len(username) <= 2:
            errors['username'].append("Username is too short")

        password_error = validate_password_user(password, username)

        if password_error:
            errors['password'].extend(password_error)

        return errors






