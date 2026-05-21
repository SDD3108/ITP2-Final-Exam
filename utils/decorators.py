def safe_file(func): 
    def wrapper(*args,**kwargs): 
        try: 
            return func(*args,**kwargs) 
        except FileNotFoundError: 
            print("error") 
            return None 
        except ValueError: 
            print("error") 
            return None 
    return wrapper