
from flask import Flask, render_template, request, redirect, url_for, flash
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Set up logging
logging.basicConfig(filename='tictactoe.log', level=logging.INFO)

game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = 'X'

@app.route('/')
def index():
    return render_template('index.html', game_board=game_board, current_player=current_player)

@app.route('/make_move', methods=['POST'])
def make_move():
    row = int(request.form['row'])
    col = int(request.form['col'])
    if game_board[row][col] == ' ':
        game_board[row][col] = current_player
        logging.info(f'{current_player} moved to row {row}, column {col}')
        if check_win(game_board, current_player):
            flash(f'{current_player} wins!')
            return redirect(url_for('index'))
        elif check_draw(game_board):
            flash('Draw!')
            return redirect(url_for('index'))
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            return redirect(url_for('index'))
    else:
        flash('Invalid move!')
        return redirect(url_for('index'))

def check_win(board, player):
    # Check rows
    for row in board:
        if all(x == player for x in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all(all(x != ' ' for x in row) for row in board)

if __name__ == '__main__':
    app.run(debug=True)
