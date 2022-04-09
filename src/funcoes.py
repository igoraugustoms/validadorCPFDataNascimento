"""
    Este arquivo contem as funcões necessarias para serem importadas durante o desenvolvimento
    de quaisquer outros projetos. Funções implementadas:

    - valida_data(aniversario) -> Recebe uma string DD/MM/YYYY e informa se data é válida. Datas futuras ao
    dia de hoje são consideradas invalidas

    - valida_CPF(CPF) -> Recebe uma string e valida CPF. CPFs que caracteres "." e "-" tem esses caracteres
    removidos

    - calcula_idade(nascimento) -> Recebe uma string DD/MM/YYYY e devolve a idade. Se for uma data invalida,
    o retorno é a mensagem "data invalida". Limita a idade em 120 anos.

    - gera_resposta(status,mensagem_CPF,  mensagem_nascimento,  idade) -> monta o Json que sera retornado pela API

    @autor Igor Augusto
    Data 09/04/2022


"""

from datetime import datetime, date
import re


def valida_data(aniversario):
    x = re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", aniversario)
    valido = True
    if x is None:
        valido = False
    else:
        hoje = date.today()
        nascimento = datetime.strptime(aniversario, '%d/%m/%Y').date()
        if (nascimento - hoje).days >= 0 or (hoje - nascimento).days / 365 > 120:
            valido = False
        else:
            day, month, year = aniversario.split('/')
            try:
                datetime(int(year), int(month), int(day))
            except ValueError:
                valido = False
    return valido



def valida_CPF(CPF):
    CPF = re.sub('[.-]', '', CPF)
    match = re.match("^[0-9]{11}", CPF)
    valido = True
    if match == None:
        valido = False
    else:
        valor = 0
        for num in range(1, 10):
            valor += num * int(CPF[num - 1])
        digito1 = valor % 11
        if digito1 == 10:
            digito1 = 0

        valor2 = 0
        for num in range(0, 9):
            valor2 += num * int(CPF[num])
            if num == 8:
                valor2 += 9 * digito1
        digito2 = valor2 % 11
        if digito2 == 10:
            digito2 = 0

        if digito1 != int(CPF[9]) or digito2 != int(CPF[10]):
            valido = False
    return valido


def calcula_idade(nascimento):
    nascimento = datetime.strptime(nascimento, '%d/%m/%Y').date()
    hoje = date.today()
    try:
        aniversario = nascimento.replace(year=hoje.year)
    except ValueError:
        aniversario = nascimento.replace(year=hoje.year,
                                      month=nascimento.month + 1, day=1)

    if (nascimento - hoje).days >= 0:
        return "Invalido"
    elif aniversario > hoje:
        return hoje.year - nascimento.year - 1
    else:
        return hoje.year - nascimento.year


def gera_resposta(status,mensagem_CPF,  mensagem_nascimento,  idade):
    resposta = {}
    resposta["status"] = status
    resposta["CPF"] = mensagem_CPF
    resposta["Data"] = mensagem_nascimento
    resposta["idade"] = idade
    return resposta

