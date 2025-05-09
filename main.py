'''
Processos

Abre o app de registro
Solicita o nome_completo
Solitata a idade
Solitata a formacao_academica
Solitata a experiencia_profissional


Aplicação para Registro de Currículo

Funções:

1. Cadastrar Curriculos
2. Listar todos os currículos
3. Buscar currículo por nome
4. Atualizar currículo
5. Excluir currículo
0. Sair

'''
from tabulate import tabulate


#TODO abrir arquivo .xmlx

# Lista para armazenar todos os currículos
lista_curriculos = []

while True:
    print('''
    1. Cadastrar Curriculos
    2. Listar todos os currículos
    3. Buscar currículo por nome
    4. Atualizar currículo
    5. Excluir currículo
    0. Sair
        ''')
    menu_principal = str(input('Escolha alguma das funções: ')).strip().lower()


    # Função cadastrar
    print(menu_principal)
    if menu_principal == '1':

        nome_completo = input('Digite o nome completo: ')
        for tentativa in range(3):
            idade = input('Digite sua idade: ' if tentativa == 0 else f'Tentativa {tentativa + 1} - Digite sua idade: ')
            if idade.isdigit():
                break
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

        #Registro de currículo na lista
        if confirmar_save.strip().lower().startswith('s'):
            lista_curriculos.append(registro_completo)


        else:
            sair = str(input('Deseja sair: (0)'))
            if sair.strip().lower().startswith('0'):
                break
    

    # Listar todos os currículos
    if menu_principal == '2':
        print('Lista de Currículos cadastrados')
        print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))
        voltar = input('Voltar para o menu principal ? (S/n)').strip().lower()
        if voltar == 's':
            continue
        else:
            break


    # Busca de Currículo por nome
    if menu_principal == '3':
        nome_busca = input('Digite o nome para busca: ')
        for curriculo in lista_curriculos:
            print(curriculo)


print('Sistema encerrado')
print(lista_curriculos)
print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))



#TODO exportar para um arquivo .xmlx