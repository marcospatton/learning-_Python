import calendar

def CalendarioTexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2023,6)
    print(txtCalendario)
CalendarioTexto()



def CalendarioHTML():
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHTML.formatmonth(2023,6)
    print(htmlCalendario)
CalendarioHTML()