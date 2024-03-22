
from flask import Flask, render_template, request, redirect, url_for, flash
import logging

app = Flask(__name__)
app.secret_key = 'yoursecretkey'
logging.basicConfig(level=logging.DEBUG)

game_board = [['', '', ''], ['', '', ''], ['', '', '']]
player1_turn = True
winner = None

@app.route('/')
def index():
    return render_template('index.html', game_board=game_board, player1_turn=player1_turn, winner=winner)

@app.route('/make_move', methods=['POST'])
def make_move():
    x = int(request.form['x'])
    y = int(request.form['y'])

    if not is_valid_move(x, y):
        flash('Invalid move')
        return redirect(url_for('index'))

    make_move(x, y, player1_turn)
    player1_turn = not player1_turn

    winner = get_winner()
    if winner:
        flash(f'{winner} wins!')
        return redirect(url_for('index'))

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global game_board, player1_turn, winner
    game_board = [['', '', ''], ['', '', ''], ['', '', '']]
    player1_turn = True
    winner = None
    return redirect(url_for('index'))

def is_valid_move(x, y):
    return game_board[x][y] == ''

def make_move(x, y, player):
    game_board[x][y] = player

def get_winner():
    for row in game_board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]

    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] and game_board[0][col] != '':
            return game_board[0][col]

    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != '':
        return game_board[0][0]

    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != '':
        return game_board[0][2]

    return None

if __name__ == '__main__':
    app.run(debug=True)
