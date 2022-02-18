from flask import Flask, render_template

app = Flask(__name__)
#route -> Arthurbalabala.com/
# funçao -> o que eu quero exibir na pagina


@app.route("/")
def arthur():
    return render_template("arthur.html")

@app.route("/Dança")
def dança():
    return render_template("dança.html")

# colocar o site no ar
if __name__== "__main__":
     app.run(debug=True)
