import sys
from services.fileManager import read_json,write_json
from services.parser import parse_users,parse_items
from services.recommendation import RecommendationService

def print_result(user_id,result):
    print(f"for user id {user_id}")

    if(len(result)==0):
        print("no items")
        return

    for(rec) in result:
        print(" ")
        print(f"item {rec.item.item_id}")
        print(f"title {rec.item.title}")
        print(f"genre {rec.item.genre}")
        print(f"score {rec.score}")
        print("why")

        for(reason) in rec.reasons:
            print(reason)

def main():
    users_data=read_json("data/users.json")
    items_data=read_json("data/items.json")

    if(users_data is None or items_data is None):
        print("error")
        return

    try:
        users=parse_users(users_data)
        items=parse_items(items_data)

        user_id=1

        if(len(sys.argv)>1):
            user_id=int(sys.argv[1])

        service=RecommendationService(users,items)
        result=service.recommend(user_id)

        print_result(user_id,result)

        write_json(
            "outputs/recommendations.json",
            [rec.to_dict() for rec in result]
        )

    except Exception:
        print("error")

if(__name__=="__main__"):
    main()
