document.getElementById('classifyButton').addEventListener('click', function() {
    var url = document.getElementById('url').value;
  
    if (url) {
      fetch('http://127.0.0.1:5000/classify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('result').textContent = `The URL '${data.url}' is classified as: ${data.classification}`;
      })
      .catch(error => {
        document.getElementById('result').textContent = 'Error: ' + error.message;
      });
    } else {
      document.getElementById('result').textContent = 'Please enter a valid URL.';
    }
  });
  