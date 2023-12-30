from flask import Flask, render_template, json
from utils import MethodsUtils as methodsUtils
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.secret_key = 'teste'
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET'])
def home():

    jogos = []
    jogos.append(Jogo("25/07/2023 21:30", 1, 2, "CORINTHIANS", "SÃO PAULO",
                 "NEO QUIMICA ARENA", "NEO QUIMICA ARENA", "COPA DO BRASIL 2023", "SEMIFINAL", False))
    jogos.append(Jogo("30/07/2023 11:00", 0, 0, "SÃO PAULO", "BAHIA",
                 "MORUMBI", "MORUMBI", "BRASILEIRÃO 2023", "11", True))
    jogos.append(Jogo("03/08/2023 11:00", 1, 0, "SAN LORENZO", "SÃO PAULO",
                 "ARGENTINA", "ARGENTINA", "SULAMERICANA 2023", "OITAVAS DE FINAL ", False))
    jogos.append(Jogo("10/08/2023 11:00", '', '',  "SÃO PAULO", "SAN LORENZO",
                 "MORUMBI", "MORUMBI", "SULAMERICANA 2023", "OITAVAS DE FINAL ", False))
    return render_template("poc.html", lstJogos=jogos)


class Jogo:
    def __init__(self, dataHoraJogo, golsVisitante, golsCasa, timeCasa, timeVisitante, estadio, localJogo, campeonato, fase, temRodada):
        self.dataHoraJogo = dataHoraJogo
        self.golsVisitante = golsVisitante
        self.golsCasa = golsCasa
        self.timeCasa = timeCasa
        self.timeVisitante = timeVisitante
        self.estadio = estadio
        self.localJogo = localJogo
        self.campeonato = campeonato
        self.fase = fase
        self.temRodada = temRodada

if __name__ == '__main__':
    methodsUtils.initComponentes(app)
    app.run(debug=True)
