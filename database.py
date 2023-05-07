import sqlite3

def create_user_table():
    conn = sqlite3.connect('optibiz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL,
                 password TEXT NOT NULL,
                 organization_id INTEGER NOT NULL,
                 FOREIGN KEY (organization_id) REFERENCES organizations(id))''')
    conn.commit()
    conn.close()

def create_organization_table():
    conn = sqlite3.connect('optibiz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS organizations
                 (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 address TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 email TEXT NOT NULL,
                 password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Add more tables for projects, inventory, tasks, and reports

if __name__ == '__main__':
    create_user_table()
    create_organization_table()