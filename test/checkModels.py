import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.user import RegularUser,AdminUser
from models.item import Item
from models.recom import Recommendation

user=RegularUser(1,"ali",["movie1","movie2"])

print(user.user_id)
print(user.name)
print(user.liked_items)
print(user.get_role())

admin=AdminUser(2,"admin",["movie3"])

print(admin.user_id)
print(admin.name)
print(admin.get_role())
print(admin.can_manage())

item=Item("movie1","dark road","action")

print(item.item_id)
print(item.title)
print(item.genre)

rec=Recommendation(item,1,["user 2 liked it"])

print(rec.item.item_id)
print(rec.score)
print(rec.reasons)

print("models ok")