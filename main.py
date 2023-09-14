from fastapi import FastAPI, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError

from db import crud, models, schemas
from db.database import SessionLocal, engine


app = FastAPI()

# db connection for every request
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


@app.post('/api', response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
  if type(person.name) is not str:
    raise HTTPException(
      status_code=400,
      detail="The person's name can ONLY be a string"
    )
  else:
    return crud.create_person(db=db, person=person)


@app.get('/api/{person_id}', response_model=schemas.Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
  try:
    db_person = crud.get_person(db=db, person_id=person_id)
    assert db_person is not None
  except OperationalError:
    raise HTTPException(
      status_code=500,
      detail='Problem with database'
    )
  except AssertionError:
    raise HTTPException(
      status_code=404,
      detail='Person not found'
    )
  else:
    return db_person


@app.put('/api', status_code=204)
def update_person(person: schemas.Person, response: Response, db: Session = Depends(get_db)):
  try:
    crud.update_person(db=db, person=person)
  except AttributeError:
    # create a person instance without the id
    per = schemas.PersonCreate(name=person.name)
    # change status code to indicate that the person was created
    response.status_code = status.HTTP_201_CREATED
    # return the new person created
    return create_person(person=per, db=db)
  else:
    db_person = crud.get_person(db=db, person_id=person.id)
    if db_person.name != person.name:
      raise HTTPException(
        status_code=400,
        detail='Person Update unsuccessful'
      )
    else:
      return {}


@app.delete('/api/{person_id}', status_code=204)
async def delete_person(person_id: int, db: Session = Depends(get_db)):
  try:
    crud.delete_person(db=db, person_id=person_id)
  except UnmappedInstanceError:
    raise HTTPException(
      status_code=404,
      detail='The person you are trying to delete does not exist'
    )
  else:
    # check to see if person is still in database
    try:
      db_person = crud.get_person(db=db, person_id=person_id)
    except OperationalError:
      return {}
    else:
      raise HTTPException(
        status_code=400,
        detail='The person was not deleted'
      )
