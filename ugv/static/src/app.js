document.addEventListener("keyup", function (event) {
  if (event.key == "ArrowLeft") {
    // console.log("left");
    document.location.href = "/left";
  }
  if (event.key == "ArrowRight") {
    // console.log("right");
    document.location.href = "/right";
  }
  if (event.key == "ArrowUp") {
    // console.log("up");
    document.location.href = "/forward";
  }
  if (event.key == "ArrowDown") {
    // console.log("down");
    document.location.href = "/backward";
  }
  if (event.key == " ") {
    // console.log("down");
    document.location.href = "/stop";
  }
});