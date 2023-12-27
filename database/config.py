import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

load_dotenv()

POSTGRES_URL = os.environ.get("POSTGRES_URL", None)
engine = create_engine(POSTGRES_URL)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
