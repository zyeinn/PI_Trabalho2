import psycopg2

class Person:
    id = int()
    name = str()
    phone = str()
    num_people = str()
    date = str()
    time = str()
    num_table = int()

    def __init__(self, id, name, phone, num_people, date, time, num_table):
        self.id = id
        self.name = name
        self.phone = phone
        self.num_people = num_people
        self.date = date
        self.time = time
        self.num_table = num_table

class Reserva:

    num_table_max = 2

    def connect_db(self):
        con = psycopg2.connect(host = 'localhost' , database = 'PI' , user = 'postgres' , password = '#########')
        return con
    
    def insert_db(self, con, person):
        cur = con.cursor()
        sql =  f"INSERT INTO reservas (name, phone, date, time, num_people, num_table) VALUES ('{person.name}', '{person.phone}', '{person.date}', '{person.time}', '{str(person.num_people)}', '{str(person.num_table)}')"
        cur.execute(sql)
        con.commit()
    
    def delete_db(self, con):
        cur = con.cursor()
        sql = "DELETE FROM reservas" # Apagar os dados da Tabela
        cur.execute(sql)
        con.commit()

    def all_data_db(self, con):
        cur = con.cursor()
        cur.execute('SELECT * FROM reservas') # Returna os valores todos da Base de Dados
        fetch = cur.fetchall()
        for f in fetch:
            print(f[1], f[2], f[3], f[4], f[5], f[6], seq = ' ')
    
    def close_db(self, con):
        con.close()

    def checktime(self, con, time, date):
        cur = con.cursor()
        sql = f"SELECT COUNT(*) FROM reservas WHERE time = '{time}' and date = '{date}'" # Esta query irá apresentar o numero de reservas
        cur.execute(sql)
        fetch = cur.fetchone()
        return fetch[0]
        