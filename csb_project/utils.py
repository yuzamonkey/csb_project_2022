from .models import User

def user_is_in_db(username):
    user = User.objects.filter(username=username)
    if len(user) == 1 and user[0].username == username:
        return True
    return False
