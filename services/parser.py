from models.user import RegularUser,AdminUser
from models.item import Item
from utils.validators import is_valid_item_id

def parse_users(data):
    users=[]

    for(row) in data:
        role=row.get("role","regular")

        if(role=="admin"):
            user=AdminUser(
                row["user_id"],
                row.get("name","no name"),
                row.get("liked_items",[])
            )
        else:
            user=RegularUser(
                row["user_id"],
                row.get("name","no name"),
                row.get("liked_items",[])
            )

        users.append(user)

    return users

def parse_items(data):
    items=[]

    for(row) in data:
        item_id=row["id"]

        if(is_valid_item_id(item_id)):
            items.append(
                Item(
                    item_id,
                    row.get("title","no title"),
                    row.get("genre","unknown")
                )
            )

    return items