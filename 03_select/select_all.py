from db_init import engine, person_table

with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)

    # 1
    for row in result_set:
        print(row[0])
        print(row.name)

    # 2
    result = result_set.fetchall()
    print(result)

    # 3
    row = result_set.fetchone()
    print(row)
