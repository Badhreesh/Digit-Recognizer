const canvas = document.querySelector('#canvas');
const width = canvas.width;
const height = canvas.height;

// Define a canvas conteXt object
const ctx = canvas.getContext('2d');
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.lineWidth = 15;
ctx.strokeStyle = "#fff";

let isDrawing = false;
let lastX = 0;
let lastY = 0;

function draw(e){
  // stop the function if they are not mouse down
  if(!isDrawing) return;

  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.stroke();
  [lastX, lastY] = [e.offsetX, e.offsetY];
}

canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseover', () => isDrawing = false);

let clearButton = document.querySelector( "#clear-button" );

clearButton.addEventListener( "click", function() {
    ctx.clearRect( 0, 0, width, height );
    ctx.fillStyle="black";
    ctx.fillRect(0, 0, width, height);

});
/*
(function()
{
  let canvas = document.querySelector( "#canvas" );
  let context = canvas.getContext( "2d" );
  canvas.width = 280;
  canvas.height = 280;
  let Mouse = { x: 0, y: 0 };
  let lastMouse = { x: 0, y: 0 };
  context.fillStyle="black";
  context.fillRect(0,0,canvas.width,canvas.height);
  context.color = "white";
  context.lineWidth = 15;
    context.lineJoin = context.lineCap = 'round';

  debug();
  canvas.addEventListener( "mousemove", function( e )
  {
    lastMouse.x = Mouse.x;
    lastMouse.y = Mouse.y;
    Mouse.x = e.pageX - this.offsetLeft;
    Mouse.y = e.pageY - this.offsetTop;
  }, false );
  canvas.addEventListener( "mousedown", function( e )
  {
    canvas.addEventListener( "mousemove", onPaint, false );
  }, false );
  canvas.addEventListener( "mouseup", function()
  {
    canvas.removeEventListener( "mousemove", onPaint, false );
  }, false );
  let onPaint = function()
  {
    context.lineWidth = context.lineWidth;
    context.lineJoin = "round";
    context.lineCap = "round";
    context.strokeStyle = context.color;

    context.beginPath();
    context.moveTo( lastMouse.x, lastMouse.y );
    context.lineTo( Mouse.x, Mouse.y );
    context.closePath();
    context.stroke();
  };
  function debug()
  {

    /* CLEAR BUTTON */
    /*
    let clearButton = $( "#clearButton" );

    clearButton.on( "click", function()
    {

        context.clearRect( 0, 0, 280, 280 );
        context.fillStyle="black";
        context.fillRect(0,0,canvas.width,canvas.height);

    });

    /* LINE WIDTH */
    /*
    let slider = document.getElementById("myRange");
    let output = document.getElementById("sliderValue");
    output.innerHTML = slider.value;
    slider.oninput = function() {
      output.innerHTML = this.value;
      context.lineWidth = $( this ).val();
    }

    $( "#lineWidth" ).change(function()
    {
      context.lineWidth = $( this ).val();
    });
  }
}());

*/
