from sqlalchemy.orm import Session

from . import models, schemas

def get_person(db: Session, person_id: int):
  return db.query(models.Person).filter(models.Person.id == person_id).first()


def get_persons(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.PersonCreate):
  db_person = models.Person(name=person.name)
  db.add(db_person)
  db.commit()
  db.refresh(db_person)
  return db_person


def update_person(db: Session, person: schemas.PersonCreate):
  db_person = db.query(models.Person).filter(models.Person.id == person.id).first()

  db_person.name = person.name
  db.add(db_person)
  db.commit()


def delete_person(db: Session, person_id: int):
  db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
  db.delete(db_person)
  db.commit()


