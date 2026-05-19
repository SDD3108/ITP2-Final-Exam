class User:
    def __init__(self,user_id,name,liked_items):
        self._user_id=user_id
        self._name=name
        self._liked_items=list(liked_items)

    def user_id(self):
        return self._user_id
    def name(self):
        return self._name
    def liked_items(self):
        return self._liked_items

    def get_role(self):
        return "user"
    def can_manage(self):
        return False

class RegularUser(User):
    def get_role(self):
        return "regular"

class AdminUser(User):
    def get_role(self):
        return "admin"
    def can_manage(self):
        return True
