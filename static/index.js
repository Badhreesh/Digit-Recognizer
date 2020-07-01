const canvas = document.querySelector('#canvas');
const msg = document.querySelector('.msg');
const width = canvas.width;
const height = canvas.height;

let result = document.querySelector('#result');
let original_text = result.textContent;

const ctx = canvas.getContext('2d');
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.lineWidth = 10;
ctx.strokeStyle = "#fff";

let isDrawing = false;
let lastX = 0;
let lastY = 0;

let draw_called = false;

function draw(e){
  // stop the function if the mouse is not down
  if(!isDrawing) return;

  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.stroke();
  [lastX, lastY] = [e.offsetX, e.offsetY];
  draw_called = true;
}

canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseover', () => isDrawing = false);

let clearButton = document.querySelector("#clear-button");

clearButton.addEventListener( "click", function() {
    ctx.clearRect( 0, 0, width, height );
    ctx.fillStyle="black";
    ctx.fillRect(0, 0, width, height);
    draw_called = false;
    result.innerHTML = original_text;
});

let predictButton = document.querySelector("#predict-button");

predictButton.addEventListener("click", function() {
    let dataURL = canvas.toDataURL();

    if (!draw_called) {
      msg.classList.add('error');
      msg.innerHTML = 'Please draw a digit first';
      setTimeout(() => msg.innerHTML = "", 2000);
    }
    else {
    document.getElementById('data').value = dataURL;
    let fd = new FormData(document.forms["form1"]);

    let xhr = new XMLHttpRequest({mozSystem: true});
    xhr.open('POST', 'predict', true);

    xhr.onreadystatechange = function () {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        result.innerHTML = xhr.responseText;
      }
    }
    xhr.send(fd);
  }
});
