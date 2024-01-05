import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://flask:flask-2024@8.136.89.212/test_db',
    echo=True)

# create table
meta_data = sqlalchemy.MetaData()

department = sqlalchemy.Table(
    "department", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
)

employee = sqlalchemy.Table(
    "employee", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("department_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("department.id"), nullable=False),
)

meta_data.create_all(engine)