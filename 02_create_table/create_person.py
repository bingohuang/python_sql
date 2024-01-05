import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://flask:flask-2024@8.136.89.212/test_db',
    echo=True)

meta_data = sqlalchemy.MetaData()

person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
)

## create table
meta_data.create_all(engine)

## insert a record
# person_insert = person.insert()
# print(person_insert)
# insert_bingo = person_insert.values(name="Bingo", birthday="1989-01-01")
#
# with engine.connect() as conn:
#     result = conn.execute(insert_bingo)
#     print(result.inserted_primary_key_rows)
#     conn.commit()

## insert multiple records
person_insert = person.insert()
with engine.connect() as conn:
    conn.execute(person_insert, [
        {"name": "bingo1", "birthday": "2024-01-01"},
        {"name": "bingo2", "birthday": "2025-01-01"},
        {"name": "bingo3", "birthday": "2026-01-01"},
    ])
    conn.commit()
