/*
 simple file to make using html5 canvases simpler and more readable

 i would be ok with using canvases directly but i don't want to force
 people to learn canvases just to read my tutorial
 */

function CanvasWrapper(canvasId) {
  var canvas = document.getElementById(canvasId);
  this.width = canvas.width;
  this.height = canvas.height;
  var events = [];
  var ctx = canvas.getContext("2d")   // TODO: is using same context for everything like this bad?

  function addKeyHandler(original, eventCreator) {
    var oldHandler = original || function(){};
    return function (evt) {
      if (document.activeElement !== canvas) {
        return oldHandler(evt);
      }

      // prevent scrolling with arrow keys so the demo can use them
      if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].indexOf(evt.key) >= 0) {
        evt.preventDefault();
      }
      events.push(eventCreator(evt));
    }
  }
  document.onkeydown = addKeyHandler(document.onkeydown, function(evt) {
    return { type: 'keydown', key: evt.key };
  });
  document.onkeyup = addKeyHandler(document.onkeyup, function(evt) {
    return { type: 'keyup', key: evt.key };
  });

  this.getEvents = function() {
    var res = events;
    events = [];
    return res;
  }

  this.drawRectangle = function(left, top, width, height, color) {
    ctx.beginPath();
    ctx.rect(left, top, width, height);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.closePath();
  }

  this.fill = function(color) {
    ctx.clearRect(0, 0, this.width, this.height);   // doesn't accept colors
    ctx.beginPath();
    ctx.rect(0, 0, this.width, this.height);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.closePath();
  }

  this.drawLine = function(x1, y1, x2, y2, color) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.strokeStyle = color;
    ctx.stroke();
    ctx.closePath();
  }

  this.drawCircle = function(centerx, centery, radius, color) {
    ctx.beginPath();
    ctx.arc(centerx, centery, radius, 0, 2*Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.closePath();
  }
}


function runRepeatedly(callback) {
  function run() {
    callback();
    window.requestAnimationFrame(run);
  }
  run();
}
