from db_init import engine, person_table
from sqlalchemy.sql import and_, or_

# by one
with engine.connect() as conn:
    query = person_table.select().where(person_table.c.birthday > '1989-01-01')
    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)


# by multiple where
with engine.connect() as conn:
    query = person_table.select().where(person_table.c.birthday > '1989-01-01').where(person_table.c.id <= 3)
    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)

# by multiple where with and, or
with engine.connect() as conn:
    query = person_table.select().where(
        or_(
            person_table.c.name == 'Bingo',
            and_(
                person_table.c.birthday > '1989-01-01',
                person_table.c.id < 3
            )
        )

    )
    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)
