# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pandas as pd
from sqlalchemy import text


def get_products_dataframe():
    # Create engine using the `grocery.sqlite` database file

    engine = create_engine("sqlite:///../grocery.sqlite")
    
    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(autoload_with=engine)

    # Print all of the classes mapped to the Base
    # Base.classes.keys()
    
    session = Session(engine)
    session = Session(bind=engine)

    #query = session.query(Table_Name).filter(Table_Name.language != 'english')
    query = session.query(text("* FROM products"))

    df = pd.read_sql(query.statement, engine)

    session.close()
    return df
    

    
# Function to add dataframe to products table
def addTo_products_dataframe(product_df):
     # Create engine using the `demographics.sqlite` database file
    engine = create_engine("sqlite:///../grocery.sqlite")

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(autoload_with=engine)

    # Print all of the classes mapped to the Base
    #Base.classes.keys()

    with Session(engine) as session:
        product_df.to_sql(name='products',con=engine.raw_connection(), if_exists='append',index=False)
        session.commit()

