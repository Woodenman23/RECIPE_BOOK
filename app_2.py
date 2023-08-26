from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(bind=engine)


@dataclass
class Person(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredient_string = Column(String)


Session = sessionmaker(bind=engine)
session = Session()
p = Person(name="John", age=30)
session.add(p)
session.commit()
