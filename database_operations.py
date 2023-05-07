import sqlite3

def database_operations():
    # Connect to database
    with sqlite3.connect('example.db') as conn:
        # Create a cursor
        c = conn.cursor()

        # Create a table
        create_table = '''CREATE TABLE users
                        (id INTEGER PRIMARY KEY,
                         name TEXT,
                         email TEXT,
                         age INTEGER)'''

        # Execute the create table statement
        try:
            c.execute(create_table)
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

        # Insert a row
        insert_row = '''INSERT INTO users
                        (name, email, age)
                        VALUES
                        (?, ?, ?)'''

        # Execute the insert row statement
        try:
            c.execute(insert_row, ('John Doe', 'johndoe@example.com', 30))
        except sqlite3.Error as e:
            print(f"Error inserting row: {e}")

        # Commit the changes
        conn.commit()

database_operations()