from models.user import RegularUser,AdminUser

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