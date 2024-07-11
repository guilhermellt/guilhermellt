
comandas = []

def produtos(itens):
    itens={'PILSEN 300ml':9,
           'IPA 300ml':15,
           'PILSEN 600ml':13,
           'IPA 600ml':20}
    return itens
def consultar(item):
    itens = produtos(item)
    if item in itens:
        return item
    else:
        print('Item nao encontrado')
def comanda(numero):
    cod_comandas={'01':1,
                  '02':2,
                  '03':3,
                  '04':4,
                  '05':5,
                  '06':6,
                  '07':7,
                  '08':8,
                  '09':9,
                  '10':10,
                  '11':11,
                  '12':12,
                  '13':13,
                  '14':14,
                  '15':15,
                  '16':16,
                  '17':17,
                  '18':18,
                  '19':19,
                  '20':20}
    if numero in cod_comandas:
        return comanda
def registro_comanda(numero_comanda):
    
    itens_comanda=[]

    item = input('Qual item deseja? ')
    item = consultar(item)
    itens_comanda.append(item)
    if item in itens_comanda:print(f'Item adicionado a comanda {numero_comanda}')
    else:print('Item nao encontrado')
    comandas.append(numero_comanda,item)
    comandas.append(numero_comanda)

opc = ''
while opc != 'SAIR':
    print('-------Sistema_Cativa-------')
    com = input("Qual o numero da comanda? ")
    numero = comanda(com)
    registro_comanda(numero)

