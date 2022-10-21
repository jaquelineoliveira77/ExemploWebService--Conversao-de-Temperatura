from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/convert/<tempC>', methods=['GET'])
def C2F(tempC):
    tempF = float(tempC) * (9/5) + 32
    return jsonify({'Web Service para a conversao de uma temperatura de Celsius para Fahrenheit! Resultado Fahrenheit':tempF})

if __name__ == "__main__":
    app.run()
