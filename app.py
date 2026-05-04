import os
from flask import Flask, render_template, request, redirect, url_for, session

from game.game_manager import GameManager
from game.player import Player
from game.game_config import GameConfig, Difficulty


# 🔥 FORZAR RUTAS CORRECTAS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates")
)

# 🔐 NECESARIO PARA SESSION (IDIOMA)
app.secret_key = "clave_secreta"


# 🔥 Variables globales
game: GameManager | None = None
current_player_index = 0


# 🌍 CAMBIAR IDIOMA
@app.route("/set_language/<lang>")
def set_language(lang):
    session["lang"] = lang
    return "", 204
def t(es, en):
    return en if session.get("lang") == "en" else es

app.jinja_env.globals.update(t=t)


# 🟢 INICIO
@app.route("/")
def inicio():
    return render_template("inicio.html")


# 🟢 MENÚ
@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/manual")
def manual():
    return render_template("manual.html")


@app.route("/configuracion")
def configuracion():
    return render_template("configuracion.html")


# 🟢 INICIAR JUEGO
@app.route("/start", methods=["POST"])
def start():
    global game, current_player_index

    players_names = request.form.getlist("players")
    players_names = [p for p in players_names if p.strip() != ""]

    if len(players_names) < 3:
        return "Error: mínimo 3 jugadores"

    difficulty = request.form.get("difficulty") or "Fácil"
    rounds = int(request.form.get("rounds") or 2)

    players = [Player(name) for name in players_names]

    diff_map = {
        # Español
        "Actuales": Difficulty.EASY,
        "Leyendas": Difficulty.MEDIUM,
        "Todos": Difficulty.HARD,

        # Inglés
        "Current": Difficulty.EASY,
        "Legends": Difficulty.MEDIUM,
        "All": Difficulty.HARD
    }

    config = GameConfig(
        number_of_players=len(players),
        rounds=rounds,
        difficulty=diff_map[difficulty]
    )

    game = GameManager(players, config)
    assert game is not None

    game.start_round()
    current_player_index = 0

    return redirect(url_for("palabra"))


# 🟢 MOSTRAR PALABRA
@app.route("/palabra")
def palabra():
    global game, current_player_index

    if game is None or game.current_round is None:
        return redirect(url_for("inicio"))

    player = game.players[current_player_index]
    word = game.current_round.word

    return render_template("palabra.html", player=player, word=word)


# 🟢 SIGUIENTE JUGADOR
@app.route("/siguiente", methods=["POST"])
def siguiente():
    global game, current_player_index

    if game is None:
        return redirect(url_for("inicio"))

    current_player_index += 1

    if current_player_index >= len(game.players):
        current_player_index = 0
        return redirect(url_for("resultado"))

    return redirect(url_for("palabra"))


# 🟢 RESULTADO
@app.route("/resultado")
def resultado():
    global game

    if game is None or game.current_round is None:
        return redirect(url_for("inicio"))

    impostor_name = game.current_round.impostor.name

    return render_template("resultado.html", impostor=impostor_name)


# 🟢 EJECUTAR APP
if __name__ == "__main__":
    app.run(debug=True)