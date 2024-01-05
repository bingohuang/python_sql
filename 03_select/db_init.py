import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://flask:flask-2024@8.136.89.212/test_db',
    echo=True)

# create table
meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
)

meta_data.create_all(engine)