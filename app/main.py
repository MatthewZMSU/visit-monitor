from typing import Annotated

from fastapi import FastAPI, Request, Depends
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import sessionmaker, Session

from .config import postgres_database_settings
from .database import Visits

app = FastAPI()

def get_session():
    engine = create_engine(postgres_database_settings.database_url)
    session_maker = sessionmaker(bind=engine)
    with session_maker() as session:
        yield session


@app.get("/")
def root():
    return "Hello, World!"


@app.get("/visits")
def get_visits(request: Request, session: Session = Depends(get_session)):
    stmt = select(Visits).where(Visits.ip == request.client.host)
    visits = session.execute(stmt).scalars()
    return {"message": f"Your visits: {[repr(visit) for visit in visits]}"}


@app.put("/visits")
def remember_visit(request: Request, session: Annotated[Session, Depends(get_session)]) -> dict:
    visit = Visits(ip=request.client.host)
    session.add(visit)
    session.commit()
    return {"message": "Your visit remembered!"}


@app.delete("/visits")
def delete_visits(request: Request, session: Session = Depends(get_session)) -> dict:
    stmt = delete(Visits).where(Visits.ip == request.client.host)
    session.execute(stmt)
    session.commit()
    return {"message": "Your visits deleted!"}
