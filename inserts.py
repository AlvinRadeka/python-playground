from datetime import date

from base import Base, engine, Session

from model.actor import Actor
from model.contact_details import ContactDetails
from model.movie import Movie
from model.stuntman import Stuntman


#Initialize DB
#Base.metadata.create_all(engine)

session = Session()

movie1 = Movie("The Dark Knight Rises", date(2012, 7, 20))

actor1 = Actor("Christian Bale", date(1974, 1, 30))

movie1.actors = [actor1]

contact1 = ContactDetails("433 555 4353", "East Hollywood, CA", actor1)

stuntman1 = Stuntman("", False, actor1)

session.add(movie1)

session.add(contact1)

session.add(stuntman1)

session.commit()
session.close()
