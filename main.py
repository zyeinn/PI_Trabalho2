from functions import *
import sys

def menu():
    try:
        print(f"""--=== Marcações ===--
[1] Criar Reserva
[2] Verificar Marcações
[3] Eliminar Reserva
[4] Eliminar Toda as Reservas
[0] Sair
--========================--
{datetime.now().strftime("%d-%m-%Y")}
Marcações para Hoje: {reservastoday()}""")
        opcao = int(input('~> '))
        return opcao
    except ValueError:
        print('[!] Nenhum inteiro válido! Por favor, tente de novo... ')

def controlar_menu(option):
    if option == 1:
        addReserva() # Chama a função addReserva
        clear()
    elif option == 2:
        getreserva() # Chama a função addReserva
        clear()
    elif option == 3:
        removereserva() # Chama a função addReserva
        clear()
    elif option == 4:
        safemode = input('[!] Digite \'y\' para confirmar!\n~> ').lower() # Pergunta ao Utilizador se quer realmente sair do programa
        if safemode == 'y':
            delete_all_db() # Chama a função Delete_all_db
            clear()
            print('[!] Marcações Eliminadas!')
    elif option == 0:
        safemode = input('[!] Digite \'y\' para confirmar!\n~> ').lower() # Pergunta ao Utilizador se quer realmente sair do programa
        if safemode == 'y':
            print('[-] Saindo...')
            sys.exit()
    else:
        print('[!] Opção Invalida!')

while True:
    controlar_menu(menu())