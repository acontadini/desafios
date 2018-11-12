# Dasafio 1 Strings Parte 2 Intermediário desenvolvido por Andrey Contadini Veiga

#Variaveis Utilizadas no projeto

cont = 0
aux = 0
ini = 0
fim = 40
limite = 10000
linhas = []
texto = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n And God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day."

if (len(texto)>limite): # O desafio exigia um limite de comprimento para o texto, esse 'if' encerra o programa caso esse limite seja excedido'''
    exit(-1)


for cont in range(len(texto)):
    letra = texto[cont]
    if letra == " " and cont == fim:
        linhas.append(texto[ini:fim])
        ini = fim + 1
        fim = fim + 40
    if letra != " " and cont == fim:
        while letra != " ":
            cont = cont - 1
            letra = texto[cont]
        aux = cont
        linhas.append(texto[ini:aux])
        ini = aux + 1
        fim = aux + 40
    cont = cont + 1

for linha in linhas :
    print(linha.ljust(40))
