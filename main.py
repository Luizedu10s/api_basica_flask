from flask import Flask, make_response, request, jsonify
from bd import Jogadores
# INSTANCIANDO A APLICAÇÃO NA VARIÁVEL APP.
app = Flask(__name__)
# ORDENANDO AS INFORMAÇÕES PARA O CADASTRO NO BD.
app.config['JSON_SORT_KEYS'] = False
# ROTA PARA VER TODOS OS JOGADORES QUE ESTÃO NO BANCO DE DADOS.
@app.route('/jogadores', methods=['GET'])
def get_jogadores():
    # MOSTRANDO OS JOGADORES QUE ESTÃO NO BANCO DE DADOS.
    return make_response(
        jsonify(
            mensagem = 'Lista de jogadores no banco de dados.',
            players = Jogadores
        )
    )
# ROTA PARA ADICIONAR UM NOVO PLAYER NO BANCO DE DADOS.
@app.route('/jogadores', methods=['POST'])
def criar_player():
    jogador = request.json
    Jogadores.append(jogador)
    # REALIZANDO O CADASTRO E MOSTRANDO O BANCO DE DADOS DEPOIS DA ALTERAÇÃO.
    return make_response(
        jsonify(
        mensagem = 'Jogador cadastrado com sucesso!',
        players = Jogadores
    )
)
# EXECUTANDO A APLICAÇÃO>
app.run()