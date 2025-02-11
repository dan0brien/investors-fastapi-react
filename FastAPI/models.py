from database import Base
from sqlalchemy import Column, Integer, String

class Investor(Base):
    __tablename__ = 'investors'

    id = Column(Integer, primary_key=True)#, index=True, autoincrement=True) #
    investor_name = Column(String)#, primary_key=True)
    investory_type = Column(String)
    investor_country= Column(String)
    investor_date_added= Column(String)
    investor_last_updated= Column(String)
    commitment_asset_class= Column(String)
    commitment_amount= Column(Integer)
    commitment_currency= Column(String)