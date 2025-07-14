from flask import Flask, render_template

app = Flask(__name__)

# Tu menú recursivo, con submenús como diccionarios anidados
menu = {
    "Inicio": {},
    "Géneros": {
        "Acción": {
            "GTA V": {},
            "God of War": {},
            "Devil May Cry 5": {}
        },
        "Anime": {
            "Dragon Ball FighterZ": {},
            "Naruto Storm 4": {},
            "One Piece Warriors 4": {}
        },
        "Carreras": {
            "Forza Horizon 5": {},
            "Gran Turismo 7": {},
            "Need for Speed Heat": {}
        }
    },
    "Requisitos": {
        "All": {},
        "Altos Requisitos": {},
        "Medios Requisitos": {},
        "Pocos Requisitos": {}
    },
    "Programas": {
        "Emuladores": {},
        "Software": {}
    }
}

@app.route("/")
def index():
    return render_template("menu.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
