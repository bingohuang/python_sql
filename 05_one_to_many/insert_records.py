from db_init import engine, department, employee

with engine.connect() as conn:
    conn.execute(department.insert(), [
        {"name": "hr"},
        {"name": "it"},
    ])

    conn.execute(employee.insert(), [
        {"department_id": 1, "name": "bingo"},
        {"department_id": 1, "name": "qingo"},
        {"department_id": 2, "name": "he"},
        {"department_id": 2, "name": "yi"},
    ])

    conn.commit()