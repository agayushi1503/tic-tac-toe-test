
function makeMove(row, col) {
  const data = {
    row: row,
    col: col
  };

  fetch('/make_move', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    window.location.reload();
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
