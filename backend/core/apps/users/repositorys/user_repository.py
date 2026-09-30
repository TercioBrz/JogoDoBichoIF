from ...users.models.UserModel import *
class UserRepository:
    @staticmethod
    def get_user_by_id(id_user):

        return User.objects.get(id=id_user)

userrepository = UserRepository()