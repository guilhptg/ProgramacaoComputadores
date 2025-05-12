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
    \n
    1. Cadastrar Curriculos
    2. Listar todos os currículos
    3. Buscar currículo por nome
    4. Atualizar currículo
    5. Excluir currículo
    0. Sair
    \n
        ''')

    menu_principal = str(input('\nEscolha alguma das funções: ')).strip().lower()

    if menu_principal == '0':
        break

    # Função cadastrar
    if menu_principal == '1':

        # Nome - validação de vazio
        while True:
            nome_completo = str(input('\nDigite o nome completo: ').strip().title())

            while nome_completo == '':
                print('O nome não pode estar vazio!')
                nome_completo = str(input('Digite o nome completo: ').strip().title())
                
                if nome_completo:
                    break
            break
        
        # Validação de idade -> Int
        for tentativa in range(3):
            idade = str(input('Digite sua idade: ' if tentativa == 0 else f'Tentativa {tentativa + 1} - Digite sua idade: ')).strip().lower()
            if idade.isdigit():
                break

        formacao_academica = str(input('Digite sua formação acadêmica: ')).strip().title()
        if formacao_academica == '':
            formacao_academica = '--'

        experiencia_profissional = str(input('Digite sua experiencia profissional: ')).strip().title()
        if experiencia_profissional == '':
            experiencia_profissional = '--'

        registro_completo = {
            'nome':nome_completo, 
            'idade': idade, 
            'formacao_academica': formacao_academica, 
            'experiencia_profissional': experiencia_profissional
            }

        print('\nConfira se seus dados estão corretos\n')

        confirmar_save = str(input('Deseja salvar ? (S/n)'))

        # Validação de dados
        if confirmar_save.strip().lower().startswith('n'):
            sair = str(input('Quer continuar ? (S/n)'))
            if sair.strip().lower().startswith('n'):
                break
        else:
            #Registro de currículo na lista
            lista_curriculos.append(registro_completo)


    # Função Listar todos os currículos
    if menu_principal == '2':
        if len(lista_curriculos) > 0:
            print('\n\nLista de Currículos Cadastrados\n')
            print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))
        else:
            print('\n\nNão há curriculos cadastrados')


    # Função Busca de Currículo por nome
    if menu_principal == '3':
        if len(lista_curriculos) > 0:
            nome_busca = str(input('Digite o nome para busca: ')).strip().lower()
            for curriculo in lista_curriculos:
                if nome_busca in str(curriculo['nome']).lower():
                    print(curriculo['nome'])
                    print(f'Curriculo encontrado !')
                    print(tabulate([curriculo], headers='keys', tablefmt='grid'))

        else:
            print('\n\nNão há curriculos cadastrados')

    # Função Atualizar currículo
    if menu_principal == '4':
        nome_atualizar = str(input('Digite o nome do curriculo que deseja atualizar: ').lower().strip())
        for curriculo in lista_curriculos:
            if nome_atualizar in curriculo['nome'].lower():
                print('Currículo encontrado:')
                print(tabulate([curriculo], headers='keys', tablefmt='grid'))
                
                campo = input('Qual campo deseja atualizar? (nome / idade / formacao_academica / experiencia_profissional): ').strip().lower()
                if campo in curriculo:
                    novo_valor = input(f'Digite o novo valor para {campo}: ')
                    curriculo[campo] = novo_valor.capitalize()
                    print('Currículo atualizado com sucesso!')
                else:
                    print('Campo inválido.')
                break
        else:
            print('Currículo não encontrado.')

        pass

    if menu_principal == '5':
        # Função Excluir currículo
        if len(lista_curriculos) > 0:
            nome_excluir = str(input('Digite o nome do currículo que deseja excluir: ').strip().lower())
            for i, curriculo in enumerate(lista_curriculos):
                if nome_excluir in curriculo['nome']:
                    lista_curriculos.pop(i)
                    print('\nUsuário excluído !\n')
        else:
            print('\n\nNão há curriculos cadastrados')
            

    # Validação para vazio
    if menu_principal == '':
        sair = str(input('Precione 0 sair ou ENTER para continuar: '))
        if sair.strip().lower().startswith('0'):
            break

    else:
        continue




print('Sistema encerrado')
# print(lista_curriculos)
# print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))



#TODO exportar para um arquivo .xmlx