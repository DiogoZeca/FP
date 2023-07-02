#inicio = 6:52                 412m
#+1km  ----> +10min === 7:02   422m
#+3km -----> +18min === 7:20   440m
#volta = 07:20
#-4km -----> 40min === 8:00    480m

temp_inicial = (6 * 60) + 52
fim_1km = temp_inicial + 10 
fim_corrida = fim_1km + (3 * 6)

volta = fim_corrida + (4 * 10)

hora_chegada = volta / 60


print("Chega a casa às",hora_chegada,"horas.")