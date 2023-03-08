



class Manga:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.characters = data['characters']
        self.genres = data['genres']
        self.chapters = data['chapters']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_mangas():
        query = '''
                SELECT * FROM mangas;
                '''
        results = 


        book_selection = input("What're you interested in? (Light Novel / Comics / Surprise Me!)")
        # genre_selection 
        manga_selection = input( "Please enter a genre. Generate random manga?" )
        options = [
            

            
        ]

        # D.R.Y.

        if book_selection.lower == 'light novel':
            pass
        elif book_selection.lower == 'comics':
            pass
        else:
            pass


    @classmethod
    def get_one_manga():
        query = '''
                SELECT * FROM mangas
                WHERE id = %(id)s;
                '''
        results = 