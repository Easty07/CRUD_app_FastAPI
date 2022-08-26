from fastapi import FastAPI, Depends, HTTPException
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session


# Create the database
Base.metadata.create_all(engine)

#  Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Initialize app
app = FastAPI()

# fakeDatabase = {
#     1:{'task':'Clean car'},
#     2:{'task':'Write blog'},
#     3:{'task':'Read book'},
# }

@app.get("/")
def getItems(session:Session = Depends(get_session)):
    #return ['Item 1', 'Item 2', 'Item 3']
    items = session.query(models.Item).all()
    return items

@app.get("/{id}", response_model=schemas.Stu)
def getItem(id:int, session:Session = Depends(get_session)):

    # get the students item with the given id
    item = session.query(models.Item).get(id)

    # check if students item with given id exists. If not, raise exception and return 404 not found response
    if not item:
        raise HTTPException(status_code=404, detail=f"Students item with id {id} not found")

    return item

#option 1
# @app.post("/")
# def addItem(task:str):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task":task}
#     return fakeDatabase

#option 2
@app.post("/", response_model=schemas.Stu)
def addItem(item:schemas.Item, session:Session = Depends(get_session)):
    #newId = len(fakeDatabase.keys()) + 1

    # create an instance of the student database model
    item = models.Item(task = item.task)

    # add it to the session and commit it
    session.add(item)
    session.commit()
    session.refresh(item)

    #fakeDatabase[newId] = {"task":item.task}
    return item

#option 3
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task":body['task']}
#     return fakeDatabase


@app.put("/{id}", response_model=schemas.Stu)
def updateItem(id:int, item:schemas.Item, session:Session = Depends(get_session)):

    # get the students item with the given id
    itemObj  = session.query(models.Item).get(id)

    # update students item with the given task (if an item with the given id was found)
    if itemObj:
        itemObj.task = item.task
        session.commit()

    # check if students item with given id exists. If not, raise exception and return 404 not found response
    if not itemObj:
        raise HTTPException(status_code=404, detail=f"Students item with id {id} not found")

    #fakeDatabase[id]['task'] = item.task
    return itemObj


@app.delete("/{id}")
def deleteItem(id:int, session:Session = Depends(get_session)):

    # get the students item with the given id
    itemObj  = session.query(models.Item).get(id)

    # if students item with given id exists, delete it from the database. Otherwise raise 404 error
    if itemObj:
        session.delete(itemObj)
        session.commit()
        return 'Item was deleted...'
    else:
        raise HTTPException(status_code=404, detail=f"Students item with id {id} not found")

    # return None



    # session.delete(itemObj)
    # session.commit()
    # session.close()

    # #del fakeDatabase[id]
    # return 'Item was deleted...'
