from model.actor import Actor
from model.contact_details import ContactDetails
from model.movie import Movie

from base import Session
from datetime import date

session = Session()
movies = session.query(Movie).all()
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

recent_movies = session.query(Movie).filter(Movie.release_date > date(2012, 1, 1)).all()
print('\n### Recent movies:')
for movie in recent_movies:
    print(f'{movie.title} was released after 2012')
print('')

the_rock_movies = session.query(Movie).join(Actor, Movie.actors).filter(Actor.name == 'Dwayne Johnson').all()
print('\n### Movies starring The Rock:')
for movie in the_rock_movies:
    print(f'The Rock starred in {movie.title}')
print('')

glendale_stars = session.query(Actor).join(ContactDetails).filter(ContactDetails.address.ilike('%glend%')).all()
print('### Actors that live in Glendale:')
for actor in glendale_stars:
    print(f'{actor.name} has a house in Glendale')
print('')
