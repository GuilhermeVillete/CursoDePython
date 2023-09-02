"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_str = input('Digite um numero:')
# numero_int = int(numero_str)

# if numero_int == 0 or 2 or 4 or 6 or 8:
#     print('O numero que você digitou é par ')
#     print(id(numero_int))
#     print(type(numero_int))
# elif numero_int == 1 or 3 or 5 or 7 or 9:
#     print('O numero que você digitou é impar')
#     print(id(numero_int))
#     print(type(numero_int))
# else :
#     print('Escrava um numero válido')
#     print(id(numero_int))
#     print(type(numero_int))




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#entrada = input('Digite o horario: ')


# if entrada.isdigit :
#     entrada_int = int(entrada)
#     print('Sua entrada agora é um numero inteiro')

# if entrada == 0 <= 12 :
#     print('Bom dia!')
# if entrada == 12 <- 17 :
#     print('Boa tarde!!')
# if entrada == 18 <= 23 :
#     print('Boa noite!!!')

# else:
#       ('Você não digitou um valor valido, tente novamente')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Digite um horario: ')


# try :

#     if entrada == 12 >= 0 :
#      print('Bom dia!')
#     if entrada == 18 >= 12 :
#      print('Bom dia!')
#     if entrada == 23 >= 18 :
#       print('Bom dia!')

# except :
#     print('Digite um valor valido')    


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite seu nome: ')
entrada_int = int(entrada)
    
if entrada_int < 4 :
    print('Seu nome é muito curto')
elif entrada_int > 5 <= 6 :
    print('Se nome tem um tamanho normal')
elif entrada_int >= 6 : 
    print('Seu nome é um nome grande')
else:
    print('Você não digitou um horario valido')


