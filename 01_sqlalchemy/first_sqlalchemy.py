import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://flask:flask-2024@8.136.89.212/test_db',
    echo=True)

conn = engine.connect()

query = sqlalchemy.text('SELECT * FROM students')

result_set = conn.execute(query)

for row in result_set:
    print(row)

conn.close()

engine.dispose()
