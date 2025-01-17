from fastapi import FastAPI , Depends ,status,  Response

from Blogpage import models
from Blogpage import schemas
from Blogpage.database import engine , Sessionlocal
from sqlalchemy.orm import Session



app = FastAPI()

    
models.base.metadata.create_all(engine)


def get_db():
    db = Sessionlocal()
    try:
        yield db 

    finally:
        db.close()    


@app.post('/blogpost')
def create_blog(request: schemas.blog , db : Session = Depends(get_db) ):
    new_blog = models.blog(title = request.title , body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
 

@app.get('/blogpost/{id}') 
def showpage(id ,response: Response,  db : Session = Depends(get_db) ):
    blogs = db.query(models.blog).filter(models.blog.id == id).first()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { 'details': f"blog with id {id} not found"}
    return blogs

@app.delete('/blog/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def delete(id ,  db : Session = Depends(get_db) ):
    db.query(models.blog).filter(models.blog.id == id). delete(synchronize_session=False)
    db.commit()
    return { "message": "deleted"}



@app.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.blog, db: Session = Depends(get_db)):
    db_blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not db_blog:
        return {"message": "Blog not found"}
    
    db_blog.title = request.title
    db_blog.body = request.body
    db.commit()
    db.refresh(db_blog)
    
    return db_blog
   

        
    

