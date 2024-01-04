import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://flask:flask-2024@rm-bp1c94s9654848q1mno.mysql.rds.aliyuncs.com/test_db',
    echo=True)

meta_data = sqlalchemy.MetaData()

person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
)

meta_data.create_all(engine)
