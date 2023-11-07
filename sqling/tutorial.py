from dataclasses import dataclass

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("afe", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return (
            f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})"
        )


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

"""person1 = Person(12312, "Mike", "Smith", "M", 35)
session.add(person1)
session.commit()

person2 = Person(12213, "Dave", "Anderson", "M", 57)
person3 = Person(22545, "Mary", "Matthews", "F", 22)
person4 = Person(42545, "Jane", "Jackson", "F", 88)

session.add(person2)
session.add(person3)
session.add(person4)

session.commit()
"""

results = session.query(Person).filter(Person.lastname == "Anderson")
for r in results:
    print(r)
results = session.query(Person).filter(Person.firstname.in_(["Mike", "Dave"]))
for r in results:
    print(r)
