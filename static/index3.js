const xCoord = document.getElementById("xCoord");
const yCoord = document.getElementById("yCoord");

document.addEventListener("mousemove", (event) => {
  xCoord.innerText = `X: ${event.clientX}`;
  yCoord.innerText = `Y: ${event.clientY}`;
});