import sqlite3

def upgrade_hyderabad_db():
    conn = sqlite3.connect('hyderabad_map.db')
    cursor = conn.cursor()

    # Clear old data to start fresh
    cursor.execute('DROP TABLE IF EXISTS edges')
    cursor.execute('DROP TABLE IF EXISTS nodes')

    # Recreate Tables
    cursor.execute('CREATE TABLE nodes (id INTEGER PRIMARY KEY, lat REAL, lon REAL, name TEXT)')
    cursor.execute('CREATE TABLE edges (u INTEGER, v INTEGER, length REAL)')

    # 10 Major Hyderabad Landmarks
    nodes = [
        (101, 17.3616, 78.4747, "Charminar"),
        (102, 17.4062, 78.4691, "Birla Mandir"),
        (103, 17.4239, 78.4738, "Hussain Sagar / Tank Bund"),
        (104, 17.4399, 78.4983, "Secunderabad Station"),
        (105, 17.4483, 78.3915, "HITEC City"),
        (106, 17.3833, 78.4011, "Golconda Fort"),
        (107, 17.4178, 78.3431, "ISB / Gachibowli"),
        (108, 17.4933, 78.3914, "JNTU KPR"),
        (109, 17.3700, 78.5670, "LB Nagar"),
        (110, 17.4120, 78.4430, "Banjara Hills")
    ]
    cursor.executemany('INSERT INTO nodes VALUES (?, ?, ?, ?)', nodes)

    # Road Network (Connecting the dots)
    # format: (From, To, Approx Distance in KM)
    edges = [
        (101, 102, 5.0), # Charminar to Birla Mandir
        (102, 103, 2.1), # Birla Mandir to Tank Bund
        (103, 104, 3.5), # Tank Bund to Secunderabad
        (102, 110, 4.2), # Birla Mandir to Banjara Hills
        (110, 105, 6.5), # Banjara Hills to HITEC City
        (105, 107, 5.8), # HITEC City to Gachibowli
        (105, 108, 5.1), # HITEC City to JNTU
        (106, 110, 5.5), # Golconda to Banjara Hills
        (101, 109, 10.2),# Charminar to LB Nagar
        (106, 107, 7.2)  # Golconda to Gachibowli
    ]
    cursor.executemany('INSERT INTO edges VALUES (?, ?, ?)', edges)

    conn.commit()
    conn.close()
    print("✅ Database Upgraded: 10 Landmarks and Road Network added!")

if __name__ == "__main__":
    upgrade_hyderabad_db()