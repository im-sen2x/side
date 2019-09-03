from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        # initialize session variables
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "Play X Here"

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/win/<string:turn>/<string:winner>/<string:message>")
def win(turn, winner, message):
    print("Wib2?")
    return render_template("winner.html", game=session["board"], turn=session["turn"], message=message)

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    def check_win():
        
        if session["board"][0][0] == session["board"][0][1] == session["board"][0][2] and (session["board"][0][0] == "O" or session["board"][0][0] == "X") and (session["board"][0][1] == "O" or session["board"][0][1] == "X") and (session["board"][0][2] == "O" or session["board"][0][2] == "X"):
            return (True, session["board"][0][0], f"{session['board'][0][0]} Wins!")
        elif session["board"][1][0] == session["board"][1][1] == session["board"][1][2] and (session["board"][1][0] == "O" or session["board"][1][0] == "X") and (session["board"][1][1] == "O" or session["board"][1][1] == "X") and (session["board"][1][2] == "O" or session["board"][0][2] == "X"):
            return (True, session["board"][1][0], f"{session['board'][1][0]} Wins!")
        elif session["board"][2][0] == session["board"][2][1] == session["board"][2][2] and (session["board"][2][0] == "O" or session["board"][2][0] == "X") and (session["board"][2][1] == "O" or session["board"][2][1] == "X") and (session["board"][2][2] == "O" or session["board"][2][2] == "X"):
            return (True, session["board"][2][0], f"{session['board'][2][0]} Wins!")
        elif session["board"][0][0] == session["board"][1][0] == session["board"][2][0] and (session["board"][0][0] == "O" or session["board"][0][0] == "X") and (session["board"][1][0] == "O" or session["board"][1][0] == "X") and (session["board"][2][0] == "O" or session["board"][2][0] == "X"):
            return (True, session["board"][0][0], f"{session['board'][0][0]} Wins!")    
        elif session["board"][0][1] == session["board"][1][1] == session["board"][2][1] and (session["board"][0][1] == "O" or session["board"][0][1] == "X") and (session["board"][1][1] == "O" or session["board"][1][1] == "X") and (session["board"][2][1] == "O" or session["board"][2][1] == "X"):
            return (True, session["board"][0][1], f"{session['board'][0][1]} Wins!")
        elif session["board"][0][2] == session["board"][1][2] == session["board"][2][2] and (session["board"][0][2] == "O" or session["board"][0][2] == "X") and (session["board"][1][2] == "O" or session["board"][1][2] == "X") and (session["board"][2][2] == "O" or session["board"][2][2] == "X"):
            return (True, session["board"][0][2], f"{session['board'][0][2]} Wins!")
        elif session["board"][0][0] == session["board"][1][1] == session["board"][2][2] and (session["board"][0][0] == "O" or session["board"][0][0] == "X") and (session["board"][1][1] == "O" or session["board"][1][1] == "X") and (session["board"][2][2] == "O" or session["board"][2][2] == "X"):
            return (True, session["board"][0][0], f"{session['board'][0][0]} Wins!")
        elif session["board"][2][0] == session["board"][1][1] == session["board"][0][2] and (session["board"][2][0] == "O" or session["board"][2][0] == "X") and (session["board"][1][1] == "O" or session["board"][1][1] == "X") and (session["board"][0][2] == "O" or session["board"][0][2] == "X"):
            return (True, session["board"][2][0], f"{session['board'][2][0]} Wins!")
        else:
            print("t9")
            return (False, None, None)
    
    # return "Played a move
    
    if session["turn"] == "Play X Here":
        session["board"][row][col] = "X" 
        session["turn"] = "Play O Here"
    else:
        session["board"][row][col] = "O" 
        session["turn"] = "Play X Here"

    w, letter, message = check_win()
    print(w)
    if w:
        print("Wib1?")
        # return redirect(url_for('hello_guest',guest = name))
        print(message, w)
        return redirect(url_for("win", turn=session["turn"], winner=w, message=message))

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.run()


