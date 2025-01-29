from sqlalchemy import create_engine
DATABASE_URL = "sqlite:///telegram_analytics.db"
engine = create_engine(DATABASE_URL)
