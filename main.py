import random
from flask import Flask
from jikanpy import Jikan

'''
episodes
series
movies
genres
'''




def get_anime():
    mood_selection = input("What're you in the mood for? (Series / Movies / Surprise Me!)")
    # genre_selection 
    anime_selection = input( "Please enter a genre. Generate random anime?" )
    options = [
        "adventure",
        "action",
        "romance",
        "psycological thriller"

        # include api of different genres?

    ]
    
    selection = ''
    while True:
        if mood_selection.lower == 'series':
            print("You've selected series!")
        else:
            print("You've selected movies!")



def get_manga():
    book_selection = input("What're you interested in? (Light Novel / Comics / Surprise Me!)")
    # genre_selection 
    manga_selection = input( "Please enter a genre. Generate random manga?" )
    options = [
        

        
    ]

    if book_selection.lower == 'light novel':
        pass
    elif 