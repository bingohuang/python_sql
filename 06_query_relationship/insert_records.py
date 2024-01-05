from db_init import engine, department, employee
import sqlalchemy

with engine.connect() as conn:
    join = employee.join(department, department.c.id == employee.c.department_id)

    # query = sqlalchemy.select(join).where(department.c.name == 'it')
    # query = sqlalchemy.select(employee).select_from(join).where(department.c.name == 'it')
    query = sqlalchemy.select(department).select_from(join).where(employee.c.name == 'bingo')

    print(conn.execute(query).fetchall())