



class User:
    def __init__(self, data):
        self.id = data['id']
        self.profile = data['profile']
        self.friends = data['friends']
        self.favorites = data['favorites']
        self.history = data['history']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']