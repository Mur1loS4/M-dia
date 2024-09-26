from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validar_notas", methods=['POST'])
def validar_notas():
    nome_aluno = request.form["nome_aluno"]
    nota_1 = float(request.form["nota_1"])
    nota_2 = float(request.form["nota_2"])
    nota_3 = float(request.form["nota_3"])
    
    media = (nota_1 + nota_2 + nota_3) / 3 

    if media >= 7:
        status = "aprovado"
    elif media >= 3:
        status = "recuperação"
    else:
        status = "reprovado"

    caminho_arquivo = 'models/notas.txt'

    # Salvando os dados no arquivo
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome_aluno};{nota_1};{nota_2};{nota_3};{media};{status}\n")

    return redirect("/")

@app.route("/consulta")
def consultar_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            if len(item) == 6:
                notas.append({
                    'nome': item[0],
                    'nota_1': item[1],
                    'nota_2': item[2],
                    'nota_3': item[3],
                    'media':  item[4],
                    'status': item[5],
                })  

    return render_template("consulta_notas.html", prod=notas)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
