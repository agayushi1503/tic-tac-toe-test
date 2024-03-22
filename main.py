
from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.logger.setLevel(logging.INFO)

board = [['', '', ''], ['', '', ''], ['', '', '']]

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/process_move', methods=['POST'])
def process_move():
    row = int(request.form['row'])
    col = int(request.form['col'])
    player = request.form['player']

    if board[row][col] == '':
        board[row][col] = player
        winner = check_winner()

        if winner:
            return render_template('index.html', board=board, winner=winner)
        elif check_draw():
            return render_template('index.html', board=board, draw=True)

    return redirect(url_for('index'))

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None

def check_draw():
    for row in board:
        for cell in row:
            if cell == '':
                return False

    return True

if __name__ == '__main__':
    app.run(debug=True)
