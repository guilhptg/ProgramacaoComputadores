'''
Processos

Abre o app de registro
Solicita o nome_completo
Solitata a idade
Solitata a formacao_academica
Solitata a experiencia_profissional


Aplicação para Registro de Currículo

'''
from tabulate import tabulate


#TODO abrir arquivo .xmlx

# Lista para armazenar todos os currículos
lista_curriculos = []

while True:
    nome_completo = input('Digite o nome completo: ')
    idade = input('Digite sua idade: ')
    if idade.isdigit():
        pass
    else:
        print('Nao é um numero! Digite apenas numero inteiros !!!')
        idade = input('Primeira tentativa:\nDigite sua idade: ')
        if idade.isdigit():
            pass
        else:
            print('Nao é um numero! Digite apenas numero inteiros !!!')
            idade = input('Segunda tentativa:\nDigite sua idade: ')
            if idade.isdigit():
                pass
            else:
                print('Nao é um numero! Digite apenas numero inteiros !!!')
                idade = input('Terceira tentativa:\nDigite sua idade: ')
                if idade.isdigit():
                    pass
                else:
                    print('Nao é um numero! Digite apenas numero inteiros !!!')

    formacao_academica = input('Digite sua formação acadêmica: ')
    experiencia_profissional = input('Digite sua experiencia profissional: ')
    registro_completo = {
        'nome':nome_completo, 
        'idade': idade, 
        'formacao_academica': formacao_academica, 
        'experiencia_profissional': experiencia_profissional
        }

    print('Confira se seus dados estão corretos')
    print(tabulate(lista_curriculos, headers='keys'))
    print(tabulate(registro_completo, headers='keys'))

    confirmar_save = input('Deseja salvar ? (S/n)')
    if continuar.strip().lower().startswith('s'):
        lista_curriculos.append(registro_completo)
    
    continuar = input('Quer cadastrar outro currículo ? (s/N): ')
    if continuar.strip().lower().startswith('s'):
        pass
    else:
        sair = input('Deseja sair: (S//n)')
        if sair.strip().lower().startswith('s'):
            break


print(lista_curriculos)
print(tabulate(lista_curriculos, headers='keys'))

print(nome_completo, idade, formacao_academica, experiencia_profissional)

#TODO exportar para um arquivo .xmlx