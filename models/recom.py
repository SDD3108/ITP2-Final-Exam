class Recommendation:
    def __init__(self,item,score,reasons):
        self.item=item
        self.score=score
        self.reasons=reasons
    
    def to_dict(self):
        return {
            "item_id": self.item.item_id,
            "title": self.item.title,
            "genre": self.item.genre,
            "score": self.score,
            "why": self.reasons
        }
