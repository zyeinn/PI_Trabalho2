from classes import *
from datetime import datetime
import sys
import os
import time

Reserva = Reserva()

def clear():
    time.sleep(3)
    if os.name == 'nt': # Se o sistema operational for windows, escreve 'cls' no terminal
        os.system('cls')

def horario():
    print("""--== Horário ==--
[1] 19:30
[2] 20:00
[3] 20:30
[4] 21:00
[5] 21:30
[6] 22:00""")
    option = int(input('Option: '))

    if option == 1:
        time = '19:30'
    elif option == 2:
        time = '20:00'
    elif option == 3:
        time = '20:30'        
    elif option == 4:
        time = '21:00'
    elif option == 5:
        time = '21:30'
    elif option == 6:
        time = '22:00'
    return time

def sendReserva(data):
        con = Reserva.connect_db()
        tmax = Reserva.checktime(con, data.time, data.date)
        if Reserva.num_table_max > tmax:
            data.num_table = int(tmax) + 1
            Reserva.insert_db(con, data)
            Reserva.close_db(con)
            return True
        else:
            Reserva.close_db(con)
            return False

def addReserva():
        print("--== Adicionar Reserva ==--")
        name = input('[?] Nome: ')
        phone = input('[?] Nº Telefone: ')
        while len(str(phone)) != 9:
            print('[!] O número de telefone que forneceu não tem o comprimento adequado!')
            phone = int(input('[?] Nº Telefone: '))
        
        num_people = int(input('[?] Total de Pessoas (MAX: 5 por Mesa): '))
        while num_people > 5:
            print('[!] Total de Pessoas por Mesas Ultrapassado!')
            num_people = int(input('[?] Total de Pessoas (MAX: 5 por Mesa): '))
        date = input('[?] Data (dd-mm-yyyy): ')
        
        time = horario()

        person = Person(None, name, phone, num_people, date, time, 1)
        if sendReserva(person) == True:
            print("[+] Reserva Adicionada com Sucesso!")
            print(f"[-] Nome: {name}")
            print(f"[-] Nº Telefone: {phone}")
            print(f"[-] Total de Pessoas: {num_people}")
            print(f"[-] Data de reserva: {date}")
            print(f"[-] Hora: {time}")
        else:
            print ('[!] Não há mais mesas para essa hora!!\n[!] Reserve em outra Hora!!')
            sys.exit()

def getreserva():
        print('--== Verificar Marcações ==--')
        phone = input("[?] Insira o Nº de telefone: ")
        con = Reserva.connect_db()
        cur = con.cursor()
        sql = f"SELECT * FROM reservas WHERE phone = '{phone}'"
        cur.execute(sql)
        fetch = cur.fetchall()
        Reserva.close_db(con)
        print("[!] Apresentando Dados...")
        if not fetch:
                print("[!] A Marcação Não Foi Encontrada!")
        else:
            for f in fetch:
                print("--== Marcação ==--")
                print(f"[-] Nome: {f[1]}")
                print(f"[-] Nº Telefone: {f[2]}")
                print(f"[-] Data: {f[3]}")
                print(f"[-] Hora: {f[4]}")
                print(f"[-] Total de Pessoas: {f[5]}")
                print(f"[-] Nº Da Mesa: {f[6]}")

def removereserva():
    print("--== Eliminar Reserva ==--")
    phone = input('[?] Insira o Nº Telefone para remover a reserva: ')
    safemode = input('[!] Digite \'y\' para confirmar!\n~> ').lower()
    if safemode == 'y':
        con = Reserva.connect_db()
        cur = con.cursor()
        sql = f"DELETE FROM reservas where phone = '{phone}'"
        cur.execute(sql)
        con.commit()
        Reserva.close_db(con)
        print('[!] Marcação Eliminada!')
    else:
        print('[!] Operação Cancelada!')

def delete_all_db():
    con = Reserva.connect_db() 
    Reserva.delete_db(con)
    Reserva.close_db(con)

def reservastoday():
    con = Reserva.connect_db() 
    cur = con.cursor()
    date = datetime.now().strftime("%d-%m-%Y")
    sql = f"SELECT COUNT(*) FROM reservas WHERE date = '{date}'"
    cur.execute(sql)
    fetch = cur.fetchone()
    return fetch[0] 
    