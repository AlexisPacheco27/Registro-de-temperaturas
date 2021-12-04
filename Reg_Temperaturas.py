from datetime import date
from datetime import datetime

def encabezado():
    titulo = 'NO.' + '   ' + 'FECHA' + '         ' + 'TEMPERATURA (°C)'
    print(titulo)

def imp_menu():
    print('REGISTRO DE TEMPERATURA')
    print('1 -> Ingresar nueva temperatura')
    print('2 -> Mostrar temperaturas')
    print('3 -> Mostrar temperatura minima')
    print('4 -> Mostrar temperatura maxima')
    print('5 -> Salir')

def new_temp(temp_reg):
    con = 0
    temp = input('Digite la temperatura:')
    if con == '0':
        newlist_temp = [temp]
        con = 1
        return newlist_temp
    else:
        temp_reg.append(temp)
        return temp_reg

def gen_fecha(gen_fech):
    today = date.today()
    gen_fech.append(today)
    return gen_fech

def view_temp(l_fec, l_temp):
    encabezado()
    for i in range(0, len(l_temp)):
        print(str(i+1) + '     ' + str(l_fec[i]) + '        ' + str(l_temp[i]) + '°C')

def cal_tempMin(l_temp):
    l_temp.sort()
    print('LA MENOR TEMPERATURA REGISTRADA ES:')
    print(str(l_temp[0]) + '°C \n')

def cal_tempMax(l_temp):
    l_temp.sort()
    print('LA MAYOR TEMPERATURA REGISTRADA ES:')
    print(str(l_temp[-1]) + '°C \n')
    

def main():
    imp_menu()
    salida = True
    list_temp = []
    list_fech = []
    while salida != False:
        opcion = input("\nElige una opcion:")
        if opcion == '1':
            list_temp = new_temp(list_temp)
            list_fech = gen_fecha(list_fech)
            print('REGISTRO DE TEMPERATURA EXITOSO \n')
        if opcion == '2':
            view_temp(list_fech, list_temp)
            print('FIN DE REGISTRO DE TEMPERATURAS REGISTRAS \n')
        if opcion == '3':
            cal_tempMin(list_temp)
        if opcion == '4':
            cal_tempMax(list_temp)
        if opcion == '5':
            salida = False 


main()