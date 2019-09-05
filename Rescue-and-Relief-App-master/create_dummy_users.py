from app import db,models

user = models.User(username="David Beckhem",email="david@gmail.com",phone="654955575")
status = models.Status(who="vol",help=45,danger=50,latitude=26.180597,longitude=91.670657,disaster="flood",complaints="I am severly injured by this natural calamity pls come and save my family.We urgently need some foodstock to last this week.",us=user)

db.session.add(user)
db.session.add(status)
db.session.commit()
