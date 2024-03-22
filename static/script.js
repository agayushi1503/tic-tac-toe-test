
const cells = document.querySelectorAll('.cell');

cells.forEach(cell => {
  cell.addEventListener('click', handleClick);
});

function handleClick(event) {
  const row = event.target.dataset.row;
  const col = event.target.dataset.col;

  const player = 'X';

  fetch('/process_move', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ row, col, player })
  })
  .then(response => response.json())
  .then(data => {
    if (data.winner) {
      alert(`${data.winner} wins!`);
    } else if (data.draw) {
      alert('Draw!');
    } else {
      // Update the UI
      event.target.innerHTML = player;
    }
  });
}
