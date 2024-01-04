from db_init import engine, person_table

with engine.connect() as conn:
    delete = person_table.delete().where(person_table.c.id == 4)
    conn.execute(delete)
    conn.commit()
