import calendar

def imprimeMes():
    for mes in calendar.month_name:
        print(mes)

        for dia in calendar.day_name:
            print(dia)
imprimeMes()