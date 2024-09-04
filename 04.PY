# aqui é a declaração dos valores
sp =(float(67.83643))
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
outros = float(19.84953)
total = float(sp + rj + mg + es + outros)

print(f'total: {total:.3f}')

# calculo da porcentagem
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
poutros = ((outros/total)*100)

# aqui eu printei os valores utilizando f-strings com a formatação de casas decimais
print(f'Porcentagem de SP {psp:.2f}%')
print(f'Porcentagem de RJ {prj:.2f}%')
print(f'Porcentagem de MG {pmg:.2f}%' )
print(f'Porcentagem de ES {pes:.2f}%' )
print(f'Porcentagem de OUTROS {poutros:.2f}%')