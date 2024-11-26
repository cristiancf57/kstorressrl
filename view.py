import consultas
import insert

print('\nPROFESIONES')
resultado = consultas.profesiones()
for row in resultado:
    print(row)

print('\nPROFESIONES')
resultado = consultas.cargos()
for row in resultado:
    print(row)
