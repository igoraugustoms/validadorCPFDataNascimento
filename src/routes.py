"""
    Este arquivo contem as rotas utilizadas pela API

    @autor Igor Augusto
    09/04/2022

"""

from flask import Flask, request
from funcoes import valida_data, valida_CPF, calcula_idade, gera_resposta

app = Flask("validadorCPF")

@app.route("/validador", methods=["POST"])
def valida_usuario():
    body = request.get_json()

    mensagem_CPF = "Valido"
    mensagem_data_nascimento = "Valido"
    status = 200

    if "CPF" not in body or not valida_CPF(body["CPF"]):
        # return geraResponde(400, "Falha ao enviar parametro CPF")
        mensagem_CPF = "Invalido (CPF digitado incorretamente (11 numeros)"
        status = 400
    if "aniversario" not in body or not valida_data(body["aniversario"]):
        # return geraResponde(400, "Falha ao enviar parametro data de aniversario")
        mensagem_data_nascimento = "Invalido (formato de data DD/MM/YYYY)"
        status = 400
        idade = "Data invalida"
    else:
        idade = calcula_idade(body["aniversario"])

    return gera_resposta(status, mensagem_CPF, mensagem_data_nascimento,  idade)


app.run()
