from .validators import validate_email_user, validate_password_user

class UserCreateSerializer:

    def __init__(self, data) -> None:
        self.data = data
        self.validated_data = {}
        self.errors = {}

    def is_valid(self):

        username = self.data.get("username")
        first_name = self.data.get("first_name")
        email = self.data.get("email")
        password = self.data.get("password")

        required_fields = ["username", "first_name", "email", "password"]
        for field in required_fields:
            if not self.data.get(field):
                self.errors[field] = f"{field.replace('_', ' ').capitalize()} obrigatório"

        password_error = validate_password_user(password, username ,first_name, email)
        if password_error:
            self.errors["password"] = password_error

        email_error = validate_email_user(email)

        if email_error:
            self.errors["email"] = email_error

        if self.errors:
            return False

        self.validated_data = {
            "username": username,
            "first_name": first_name,
            "email": email,
            "password": password
        }

        return True