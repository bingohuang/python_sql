from db_init import engine, person_table

with engine.connect() as conn:
    # update all
    # update = person_table.update().values(address="hangzhou xihu")
    # update where
    update = person_table.update().values(address="hangzhou yuhang").where(person_table.c.id == 1)
    conn.execute(update)
    conn.commit()
