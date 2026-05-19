class Item:
    def __init__(self,item_id,title,genre):
        self._item_id=item_id
        self._title=title
        self._genre=genre;
    
    def item_id(self):
        return self._item_id
    
    def title(self):
        return self._title
    
    def genre(self):
        return self._genre
    def to_dict(self):
        return {
            "id": self._item_id,
            "title": self._title,
            "genre": self._genre
        }
