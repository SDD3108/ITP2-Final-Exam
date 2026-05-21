import re 
 
def is_valid_item_id(item_id): 
    pattern=r"^movie[0-9]+$" 
    return re.match(pattern,item_id) is not None 
 
def validate_users(users): 
    if(len(users)<2): 
        raise ValueError("error") 
 
    ids=set() 
 
    for(user) in users: 
        if(user.user_id in ids): 
            raise ValueError("error") 
 
        ids.add(user.user_id)