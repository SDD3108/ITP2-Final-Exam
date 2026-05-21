from models.recom import Recommendation
from utils.validators import validate_users


class RecommendationService:
    def __init__(self, users, items):
        validate_users(users)

        self.users = users
        self.items = items
        self.items_map = {item.item_id: item for item in items}

    def user_generator(self):
        for (user) in self.users:
            yield user