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

            def find_user(self, user_id):
                for (user) in self.user_generator():
                    if (user.user_id == user_id):
                        return user

                return None

            def get_similarity(self, user1, user2):
                set1 = set(user1.liked_items)
                set2 = set(user2.liked_items)
                same_items = set1.intersection(set2)

                return len(same_items), tuple(same_items)

            def recommend(self, user_id):
                target_user = self.find_user(user_id)

                if (target_user is None):
                    print("not found")
                    return []

                liked_set = set(target_user.liked_items)
                result = {}

                for (other_user) in self.users:
                    if (other_user.user_id == user_id):
                        continue

                    similarity, same_items = self.get_similarity(target_user, other_user)

                    if (similarity == 0):
                        continue

                    for (item_id) in other_user.liked_items:
                        if (item_id in liked_set):
                            continue

                        if (item_id not in self.items_map):
                            continue

                        if (item_id not in result):
                            result[item_id] = {
                                "item": self.items_map[item_id],
                                "score": 0,
                                "why": []
                            }

                        result[item_id]["score"] += similarity

                        same_text = ", ".join(same_items)
                        result[item_id]["why"].append(
                            f"user {other_user.user_id} liked it same {same_text}"
                        )

                recommendations = []

                for (value) in result.values():
                    recommendations.append(
                        Recommendation(
                            value["item"],
                            value["score"],
                            value["why"]
                        )
                    )

                return sorted(recommendations, key=lambda rec: rec.score, reverse=True)