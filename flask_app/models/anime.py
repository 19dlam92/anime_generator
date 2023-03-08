



class Anime:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.characters = data['characters']
        self.genres = data['genres']
        self.episodes = data['episodes']
        self.series = data['series']
        self.movies = data['movies']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_animes():
        query = '''
                SELECT * FROM animes;
                '''
        results = 


    mood_selection = input("What're you in the mood for? (Series / Movies / Surprise Me!)")
    # genre_selection 
    anime_selection = input("Please enter a genre. Generate random anime?")
    options = [
        "adventure",
        "action",
        "romance",
        "psychological thriller"

        # include api of different genres?

    ]
    
    selection = ''
    while True:
        if mood_selection.lower == 'series':
            print("You've selected series!")
        else:
            print("You've selected movies!")


    @classmethod
    def get_one_anime():
        query = '''
                SELECT * FROM animes
                WHERE id = %(id)s;
                '''
        results = 

