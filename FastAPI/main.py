from typing import Annotated, List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlalchemy.orm import Session
from pydantic import BaseModel
import pandas as pd

from database import SessionLocal, engine
import models
from models import Investor


app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
)


class InvestorBase(BaseModel):
    """
    Represents the base model for an investor with essential attributes.

    This class is used to define the basic structure of an investor,
    and commitment details.
    """
    id: int
    investor_name: str
    investory_type: str
    investor_country: str
    commitment_asset_class: str
    commitment_amount: int
    commitment_currency: str


class InvestorSummary(BaseModel):
    """
    Represents a summary of an investor's commitments.
    """
    investor_name: str
    investory_type: str
    total_commitment_amount: int
    commitment_currency: str


def get_db():
    """
    Provides a database session for the duration of a request.

    This function yields a database session, `db`, from `SessionLocal()` and 
    ensures that the session is closed properly after the request is completed. 
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)

# Read in data from data.csv
df = pd.read_csv('../data.csv')
df.columns = [
    'investor_name',
    'investory_type',
    'investor_country',
    'investor_date_added',
    'investor_last_updated',
    'commitment_asset_class',
    'commitment_amount',
    'commitment_currency'
    ]
df.to_sql('investors', con=engine, if_exists='replace', index=True, index_label='id')

# Annotate DbDependency to provide a database session via dependency injection
DbDependency = Annotated[Session, Depends(get_db)]


@app.get("/investors_summary/", response_model=List[InvestorSummary])
async def investors_summary(db: DbDependency):
    """
    Asynchronously retrieves a summary of investors from the database.

    This function queries the database for a summary of investors, 
    grouping them by their names. It returns a list of investors with 
    their names, types, total commitment amounts, and commitment currencies.
    """
    investors=db.query(
        Investor.investor_name,
        Investor.investory_type,
        func.sum(Investor.commitment_amount).label('total_commitment_amount'),
        Investor.commitment_currency
    ).group_by(
        Investor.investor_name
    ).all()
    return investors


@app.get("/investor/{investor_name}/", response_model=List[InvestorBase])
async def get_investor(investor_name: str, db: DbDependency):
    """
    Asynchronously retrieves individual investor information from the database.

    This function queries the database for an investor with the specified name 
    and returns the corresponding investor information.
    """
    investor = db.query(models.Investor).filter(Investor.investor_name == investor_name).all()
    return investor
