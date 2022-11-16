
from sqlalchemy import Column, Integer, Float, Date, String, Boolean, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os

def Load_Data(file_name):
    df = pd.read_csv(file_name, delimiter = ',', header=1, low_memory=False)
    data = list(df.values)
    return data

Base = declarative_base()

class crime(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'crime'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False) 
    dateVar = Column(VARCHAR(100))
    xCord = Column(Float)
    yCord = Column(Float)
    description = Column(VARCHAR(100))
    inside = Column(VARCHAR(100))
    weapon = Column(VARCHAR(100))
    post = Column(Integer)
    gender = Column(VARCHAR(100))
    age = Column(Integer)
    race = Column(VARCHAR(100))
    eth = Column(VARCHAR(100))
    dist = Column(VARCHAR(100))
    neigh = Column(VARCHAR(100))
    prem = Column(VARCHAR(100))
    vri = Column(VARCHAR(100))




if __name__ == "__main__":

    #Create the database
    engine = create_engine('sqlite:///' + os.path.dirname(os.path.realpath(__file__)) + "/crime.db")
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    try:
        file_name = os.path.dirname(os.path.realpath(__file__)) + "/Proj_data/crime.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv
        data = Load_Data(file_name)

        for i in data:
            record = crime(**{
                'xCord' : i[0],
                'yCord' : i[1],
                'id' : i[2],
                'dateVar' : i[3],
                'description' : i[4],
                'inside' : i[5],
                'weapon' : i[6],
                'post' : i[7],
                'gender' : i[8],
                'age' : i[9],
                'race' : i[10],
                'eth' : i[11],
                'dist' : i[12],
                'neigh' : i[13],
                'prem' : i[14],
                'vri' : i[15]
            }
            )
                
            s.add(record) #Add all the records
        s.commit() #Attempt to commit all the records
    
    
    #except:
    #    s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
