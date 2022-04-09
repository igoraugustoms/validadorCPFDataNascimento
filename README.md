# API validadora de CPF e idade

### Objetivo do projeto
<p> O objetivo é criar uma API usando Flask. Ela recebe como input um JSON contendo os campos CPF e data de nascimento (DD/MM/YYYY). O retorno é também um JSON, mas informando se o CPF é válido, se a data é válida, a idade atual da pessoa e o status de sucesso ou não.  
</p>

### Tecnologias e ferramentas usadas durante desenvolvimento
- ``Python``
- ``Flask``
- ``Pycharm``
- ``Postman``

### Como rodar e testar
<p>
O primeiro passo para testar é ter uma versão do Python 3 instalada na máquina, além de executar o pip install flask.

Com o projeto devidamente baixado na sua máquina, os arquivos funcoes.py e routes.py devem ser salvos na mesma pasta.

Feito isso, pode-se rodar o arquivo routes.py. 

</p>

<img src="src\to_readme\executa_python.jpg">

<p>
A próxima etapa é abrir o postman para fazer as requisições. No caso, o método será o POST e enviaremos no body um JSON com o CPF e a data de nascimento, conforme a imagem abaixo. O endereço é o http://127.0.0.1:5000/validador

<img src="src\to_readme\sucesso.jpg">

No nosso exemplo, o status foi o 200 e a operação ocorreu com sucesso, ou seja, os dois parâmetros enviados foram válidos. 

O validador aceita CPFs com e sem caracteres (ponto e traço). No entanto, se menos de 11 números forem enviados no CPF, é enviada uma mensagem de erro.

<img src="src\to_readme\cpf_invalido.jpg">

A mesma mensagem é disparada se ocorrer o envio de um CPF cujos dois dígitos verificadores não baterem com o esperado.
<img src="src\to_readme\cpf_incorreto.jpg">

Com relação a data, o projeto aceita strings no formato DD/MM/YYYY. Há uma verificação de datas inválidas. 
<img src="src\to_readme\data_invalida.jpg">

Um ponto importante é que devolvemos a idade atual conforme a data de nascimento enviada. Para este programa, limitou-se a idade do usuário a 120 anos.

<img src="src\to_readme\limite_idade.jpg">

</p>

##### Desenho de plataforma de dados
<p>
Um desenho de arquitetura de dados na GCP também esta disponibilizado nesta pasta com o nome desenho.pdf.
</p>
