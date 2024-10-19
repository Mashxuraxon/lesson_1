import sqlite3

db = sqlite3.connect('auto.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS auto(
               marka TEXT,
               color TEXT,
               year INTEGER,
               price INTEGER,
               photo TEXT
               )
''')


async def add_to_db(marka,color,year,price,probeg,sellers_num,photo):
    cursor.execute('''
INSERT INTO auto(marka,color,year,price,photo)
                   VALUES(?,?,?,?,?)

''',(marka,color,year,price,photo))
    db.commit()
    

# add_to_db(marka='Cobalt',coor='black',year=2023,price=12000,
#           photo='AgACAgIAAxkBAAIETWcOPHo-_2rSPaZDDIzqj2Lbfa8DAALY4jEb9DJ4SLJwH6p5Ae7_AQADAgADcwADNgQ')


async def show_autos():
    cursor.execute('SELECT * FROM auto')
    return cursor.fetchall()

# print(show_autos())