# import csv
from fastapi import FastAPI, HTTPException, Depends

from typing import Annotated, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from models import Investor
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
)

# TODO do we need class Congif: orm_mode=True

class InvestorBase(BaseModel):
    # id = int # Column(Integer, primary_key=True, index=True, autoincrement=True)
    # investor_name: str
    investory_type: str
    investor_country: str
    investor_date_added: str
    investor_last_updated: str
    commitment_asset_class: str
    commitment_amount: int
    commitment_currency: str

    # class Config:
    #     orm_mode = True

class InvestorViewBase(BaseModel):
    investor_name: str
    investory_type: str
    total_commitment_amount: int

class InvestorModel(InvestorBase):
    id: int

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


# async def populate_table(db):
#     # Create the table if it doesn't exist
#     # Base.metadata.create_all(bind=engine)

# # Load the CSV file into a DataFrame
   
#     # df = 

# # Convert the DataFrame to a list of dictionaries
#     data = df.to_dict(orient='records')
#     for record in data:
#         investor = Investor(**record.dict())
#         db.add(investor)

#     # Commit the changes
#         db.commit()

#     # Refresh the session
#     db.refresh()


models.Base.metadata.create_all(bind=engine)

df = pd.read_csv('../data.csv')
print(df)
df.to_sql('investors', con=engine, if_exists='replace', index=True, index_label='id')


# Investor Name,Investory Type,Investor Country,Investor Date Added,Investor Last Updated,Commitment Asset Class,Commitment Amount,Commitment Currency
# column_mapping = {
#     'Investor Name': 'investor_name',
#     'Investory Type': 'investory_type',
#     'Investor Country': 'investor_country',
#     'Commitment Asset Class': 'commitment_asset_class',
#     'Commitment Amount': 'commitment_amount',
#     'Commitment Currency': 'commitment_currency',
#     'Investor Date Added': 'investor_date_added',
#     'Investor Last Updated':'investor_last_updated',
#     'Commitment Asset Class': 'commitment_asset_class'
#     }
    # Add the other columns accordingly
# db = get_db()

# df = pd.read_csv('../data.csv')
# df = df.rename(columns=column_mapping)
# # print(df)
# data = df.to_dict(orient='records')
db = SessionLocal()
# # session = get_db()
# for record in data:
#     print(record)
#     investor=Investor(**record)
#     db.add(investor)
# db.commit()
# db.close()
# populate_table(db)
# Read the CSV file and insert data into the database
# with open("../data.csv", mode='r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # Skip the header row
#     next(csv_reader)
#     for row in csv_reader:
#         db_row = models.Investor(**row)
#         db.add(db_row)
#     db.commit()
# db.close()





# Define your table schema
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS investors (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     investor_name TEXT,
#     investory_type TEXT,
#     investor_country TEXT,
#     investor_date_added TEXT,
#     investor_last_updated TEXT,
#     commitment_asset_class TEXT,
#     commitment_amount INTEGER,
#     commitment_currency TEXT
# )
# '''
# db.execute(create_table_query)
# db.commit()

# Define the CSV file path
# CSV_FILE_PATH = '../data.csv'

# # Read the CSV file and insert data into the database
# with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # Skip the header row
#     next(csv_reader)
#     for row in csv_reader:
#         db.execute('''
#             INSERT INTO investors (
#                 investor_name, investory_type, investor_country, 
#                 investor_date_added, investor_last_updated, 
#                 commitment_asset_class, commitment_amount, commitment_currency
#             ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row[0], row[1], row[2], row[3], row[4], row[5], int(row[6]), row[7]))
#     db.commit()

# # Close the connection
# db.close()



@app.get("/investors", response_model=List[InvestorViewBase]) # might want a new type
async def read_investors(db: db_dependency, skip: int=0, limit: int = 100):
    # investors = db.query(models.Investor).offset(skip).limit(limit).all()
    investors=db.query(
        # Investor.id,
        Investor.investor_name,
        Investor.investory_type,
        func.sum(Investor.commitment_amount).label('total_commitment_amount')
    ).group_by(
        # Investor.id, 
        Investor.investor_name
        #, Investor.investory_type
    ).offset(skip).limit(limit).all()
    return investors


## TODO single investor portfolio
@app.get("/investor/{investor_name}", response_model=List[InvestorModel]) # might want a new type
async def read_investors(investor_name: str, db: db_dependency):#, skip: int=0, limit: int = 100):
    investor = db.query(models.Investor).filter(Investor.investor_name == investor_name).all()
    # investors=db.query(
    #     # Investor.id,
    #     Investor.investor_name,
    #     Investor.investory_type,
    #     Investor.
    #     func.sum(Investor.commitment_amount).label('total_commitment_amount')
    # ).group_by(
    #     # Investor.id, 
    #     Investor.investor_name
    #     #, Investor.investory_type
    # ).offset(skip).limit(limit).all()
    # response = [
    #     {
    #         "investor_name": investor.investor_name,
    #         "investory_type": investor.investory_type,
    #         "total_commitment_amount": investor.commitment_amount
    #     }
    #     for _ in investor
    # ]
    
    return investor