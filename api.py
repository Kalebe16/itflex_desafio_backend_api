from datetime import datetime, timedelta

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from pytz import timezone

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)

class Certificados(db.Model):
    __tablename__ = "certificados"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    expiration = db.Column(db.Integer)
    created_at = db.Column(db.String, nullable=False)
    updated_at = db.Column(db.String, nullable=True)
    expirated_at = db.Column(db.String, nullable=False)
    

    def __init__(self, username, name, description, expiration, created_at, updated_at, expirated_at):
        self.username = username
        self.name = name
        self.description = description
        self.expiration = expiration
        self.created_at = created_at
        self.updated_at = updated_at
        self.expirated_at = expirated_at

    def to_json(self):
        return {"id": self.id, "username": self.username, "name": self.name, "description": self.description, "expiration": self.expiration, "created_at": self.created_at, "updated_at": self.updated_at, "expirated_at": self.expirated_at}

            
    def __repr__(self):
        return f'Certificados [id:{self.id}, name:{self.name}, username:{self.username}, description:{self.description}, expiration:{self.expiration}, created_at:{self.created_at}, updated_at:{self.updated_at}]'




@app.route("/", methods=['GET'])
def homepage():
    return '<h2>Esta api é um crud para gerenciamento de certificados:</h2>'


# CONSULTAR (TODOS)
@app.route("/certificados", methods=['GET'])
def obter_certificados():
    certificados_objetos = Certificados.query.all()
    certificados_json = [certificado.to_json() for certificado in certificados_objetos]
    return jsonify(certificados_json), 200


# CONSULTAR (ID)
@app.route("/certificados/<int:id>", methods=['GET'])
def obter_certificados_por_id(id):
    try:
        certificado_objeto = Certificados.query.filter_by(id=id).first()
        certificado_json = certificado_objeto.to_json()    
        return jsonify(certificado_json), 200
    except Exception as e:
        print("ERRO", e)
        return jsonify({'mensagem': 'DEU RUIM, ERRO AO CONSULTAR CERTIFICADO'}), 404 



# EDITAR
@app.route('/certificados/<int:id>', methods=['PUT'])
def editar_certificado_por_id(id):
    certificado_objeto = Certificados.query.filter_by(id=id).first()
    body = request.get_json()
    data_edicao = pegar_data_atual()


    try:
        if 'username' in body:
            certificado_objeto.username = body['username']
        if 'name' in body:
            certificado_objeto.name = body['name']
        if 'description' in body:
            certificado_objeto.description = body['description']

        certificado_objeto.updated_at = data_edicao
        db.session.add(certificado_objeto)
        db.session.commit()
        certificado_json = certificado_objeto.to_json()    
        return jsonify(certificado_json), 200

    except Exception as e:
        print('ERRO', e)
        return jsonify({'mensagem': 'DEU RUIM, ERRO AO EDITAR CERTIFICADO'}), 404



# CADASTRAR
@app.route('/certificados', methods=['POST'])
def incluir_novo_certificado():
    try:
        body = request.get_json()
        data_atual = pegar_data_atual()
        dias_para_expirar = body['expiration']
        data_expiracao = data_atual + timedelta(days=dias_para_expirar)
        
        if body['expiration'] < 10 or body['expiration'] > 3650:
            return jsonify({'mensagem': "'expiration' DEVE ESTAR ENTRE 10 E 3650"}), 422
        else:
            certificado = Certificados(username=body['username'], name=body['name'], description=body['description'], expiration=body['expiration'], created_at=data_atual, updated_at="", expirated_at=data_expiracao)
            db.session.add(certificado)
            db.session.commit()
            certificados_objetos = Certificados.query.all()
            certificados_json = [certificado.to_json() for certificado in certificados_objetos]
            return jsonify(certificados_json), 200

    except Exception as e:
        print("ERRO", e)
        return jsonify({'mensagem': 'DEU RUIM, ERRO AO CADASTRAR CERTIFICADO'}), 422


# DELETAR
@app.route('/certificados/<int:id>', methods=['DELETE'])
def excluir_certificado(id):

    try:
        certificado_objeto = Certificados.query.filter_by(id=id).first()
        db.session.delete(certificado_objeto)
        db.session.commit()
        return jsonify({'mensagem': 'CERTIFICADO DELETADO COM SUCESSO!'}), 200

    except Exception as e:
        print("ERRO", e)
        return jsonify({'mensagem': 'DEU RUIM, ERRO AO DELETAR CERTIFICADO'}), 404


#FUNÇÕES SECUNDARIAS
def pegar_data_atual():
    """Pega data e hora do momento atual em que a função é chamada"""

    data_atual = datetime.now()
    data_formato_datetime = datetime(year=data_atual.year, month=data_atual.month, day=data_atual.day, hour=data_atual.hour, minute=data_atual.minute, second=data_atual.second)
    fuso_horario_brasil = timezone('America/Sao_Paulo')
    data_certa_brasil = data_formato_datetime.astimezone(fuso_horario_brasil)
    
    #return datetime.isoformat(date_in_datetime_format)
    return data_certa_brasil



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(port=5000, host='localhost', debug=True)