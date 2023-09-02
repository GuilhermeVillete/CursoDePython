
nome = input('Digite seu nome :')
idade = input('Digite sua idade :')

if nome and idade:#TRUE

    print(f'seu nome é {nome}')
    print(f'seu nome invetido é {nome[::-1]}')

    if ' ' in nome:
        print('seu nome contem espaço')
    else:
        print('seu nome não contem espaço')

    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é : {nome[0]}')
    print(f'a ultima letra do seu nome é : {nome[-1]}')

else:
    print('Você não digitou os campos solicitados')
    