from sqlalchemy import Column, Integer, String
from database import Base

class Investor(Base):
    """
    Represents an investor in the database.

    This class corresponds to the 'investors' table in the database and stores 
    information about individual investors.
    """
    __tablename__ = 'investors'

    id = Column(Integer, primary_key=True)
    investor_name = Column(String)
    investory_type = Column(String)
    investor_country= Column(String)
    investor_date_added= Column(String)
    investor_last_updated= Column(String)
    commitment_asset_class= Column(String)
    commitment_amount= Column(Integer)
    commitment_currency= Column(String)
