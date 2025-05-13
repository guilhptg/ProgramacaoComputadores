'''

Aplicação para Registro de Currículo

Funções:

1. Cadastrar Curriculos
2. Listar todos os currículos
3. Buscar currículo por nome
4. Atualizar currículo
5. Excluir currículo
0. Sair

run on terminal 

python main.py to run aplication

'''

from tabulate import tabulate

#TODO abrir arquivo .xlxs

# Lista para armazenar todos os currículos
lista_curriculos = []
indice = 0

mapeamento_campos = {
    'nome': 'nome',
    'idade': 'idade',
    'formacao': 'formacao_academica',
    'experiencia': 'experiencia_profissional'
}

while True:
    print('''
    \n
    1. Cadastrar Curriculos
    2. Listar todos os currículos
    3. Buscar currículo por nome
    4. Atualizar currículo
    5. Excluir currículo
    0. Sair
        ''')

    menu_principal = str(input('\nEscolha alguma das funções: ')).strip().lower()

    if menu_principal == '0':
        break

    # Função cadastrar
    elif menu_principal == '1':

        # Nome - validação de vazio
        nome_completo = ''
        while nome_completo == '':
            nome_completo = str(input('\nDigite o nome completo: ').strip().title())
            if nome_completo == '':
                print('O nome não pode estar vazio!')
                
        # Validação de idade -> Int
        idade = ''
        tentativa = 0
        while not idade.isdigit() and tentativa < 3:
            idade = str(input('Digite sua idade: ' if tentativa == 0 else f'\nTentativa {tentativa} !!\n \nDigite sua idade: ')).strip().lower()
            if idade.isdigit():
                break
            print('\nTentativa inválida, use apenas núnemros.')
            tentativa += 1
        if not idade.isdigit():
            print('Falha no registro. Voltando ao menu principal. ')
            continue

        # Formação acadêmica 
        formacao_academica = str(input('Digite sua formação acadêmica: ')).strip().title()
        if formacao_academica == '':
            formacao_academica = 'NULL'

        # Experiência profissional
        print('Escrva no modelo \n\n| Cargo - Empresa |\n\nSe desejar sair digite "fim".')
        experiencia_profissional = []
        while True:
            experiencia = str(input('- ')).strip().title()
            if experiencia.lower() == 'fim':
                if len(experiencia_profissional) == 0:
                    print('Você deve adicionar pelo menos uma experiência.')
                    continue
                break
            elif experiencia != '':
                experiencia_profissional.append(experiencia)

        indice += 1
        registro_completo = {
            'indice': indice,
            'nome':nome_completo, 
            'idade': idade, 
            'formacao_academica': formacao_academica, 
            'experiencia_profissional': experiencia_profissional
            }

        print('\nConfira se seus dados estão corretos\n')
        confirmar_save = str(input('Deseja salvar ? (S/n)')).strip().lower()
        # Validação de dados
        if not confirmar_save.startswith('n'):
            lista_curriculos.append(registro_completo)

    # Função Listar todos os currículos
    elif menu_principal == '2':
        if len(lista_curriculos) > 0:
            print('\n\nLista de Currículos Cadastrados\n')
            print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))
        else:
            print('\n\nNão há curriculos cadastrados')


    # Função Busca de Currículo por nome
    elif menu_principal == '3':
        if len(lista_curriculos) > 0:
            nome_busca = str(input('\nDigite o nome para busca: ')).strip().lower()
            for curriculo in lista_curriculos:
                if nome_busca in str(curriculo['nome']).lower():
                    print(f'\nCurriculo encontrado !\n\n')
                    print(tabulate([curriculo], headers='keys', tablefmt='grid'))
        else:
            print('\n\nNão há curriculos cadastrados')

    # Função Atualizar currículo
    elif menu_principal == '4':
        if len(lista_curriculos) > 0:
            consultar_lista = str(input('\nDeseja consultar a lista ? (s/N) ')).strip().lower()

            if 's' in consultar_lista:
                print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))

            nome_atualizar = str(input('\nDigite o nome do curriculo que deseja atualizar ou índice: ').lower().strip())
            if nome_atualizar:
                for curriculo in lista_curriculos:
                    if nome_atualizar in curriculo['nome'].lower() or nome_atualizar == str(curriculo['indice']):
                        print('Currículo encontrado:')
                        print(tabulate([curriculo], headers='keys', tablefmt='grid'))
                        
                        campo = input('Qual campo deseja atualizar? (nome / idade / formacao / experiencia): ').strip().lower()
                        
                        if campo in mapeamento_campos:
                            if campo == 'experiencia':
                                print('Digite novamente as experiências ("fim" para terminar):')
                                nova_experiencia = []
                                while True:
                                    exp = str(input('- ')).strip().title()
                                    if exp.lower() == 'fim':
                                        if len(nova_experiencia) == 0:
                                            print('Voce deve adicionar ao menos uma experiência.')
                                            continue
                                        break
                                    elif exp != '':
                                        nova_experiencia.append(exp)
                                        curriculo[mapeamento_campos[campo]] = nova_experiencia
                                print('\nCurrículo atualizado com sucesso!')
                            else:
                                novo_valor = input(f'Digite o novo valor para {campo}: ')
                                curriculo[mapeamento_campos[campo]] = novo_valor.capitalize()
                                print('\nCurrículo atualizado com sucesso!')
                        else:
                            print('\nCampo inválido.')
                        break
                    else:
                        print('Nome não cadastrado')
            else:
                print('\nNenhum nome selecionado\nVoltando ao menu principal')
        else:
            print('\nNão há currículos cadastrados.')

    elif menu_principal == '5':
        # Função Excluir currículo
        if len(lista_curriculos) > 0:
            # Consulta
            consultar_lista = str(input('\nDeseja consultar a lista ? (s/N) ')).strip().lower()

            if 's' in consultar_lista:
                if len(lista_curriculos) > 0:
                    print('\n\nLista de Currículos Cadastrados\n')
                    print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))
                else:
                    print('\n\nNão há curriculos cadastrados')

            # Tratamento de busca não sucedida
            while True:
                nome_excluir = str(input('\nDigite o nome do currículo que deseja excluir: ').strip().lower())
                if nome_excluir == '':
                    nome_excluir = '--'

                for i, curriculo in enumerate(lista_curriculos):
                    if nome_excluir in str(curriculo['nome']).lower():
                        print('\nUsuário encontrado !\n')
                        print(tabulate([curriculo], headers='keys', tablefmt='grid'))
                        deseja_excluir = str(input('\nDeseja excluir ? (S/n): '))
                        if deseja_excluir.strip().lower().startswith('n'):
                            break
                        else:
                            lista_curriculos.pop(i)
                            print('\nUsuário excluído !')
                            break
                    else:
                        print('\nNome não encontrado !!! \nRedirecionado para o menu.')
                        
                break
        else:
            print('\n\nNão há curriculos cadastrados')


    # Validação para vazio
    elif menu_principal == '':
        sair = str(input('Precione 0 sair ou ENTER para continuar: '))
        if sair.strip().lower().startswith('0'):
            break

    else:
        continue


print('\nSistema encerrado')
# print(lista_curriculos)
# print(tabulate(lista_curriculos, headers='keys', tablefmt="grid"))



#TODO exportar para um arquivo .xlxs