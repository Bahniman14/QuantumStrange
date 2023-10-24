let crsr = document.querySelector("#cursor");
let blur = document.querySelector("#cursor-blur");

document.addEventListener("mousemove", function (dets){
    crsr.style.left = dets.x + "px";
    crsr.style.top = dets.y + "px";
    blur.style.left = dets.x - 250 + "px";
    blur.style.top = dets.y - 250 + "px";
  });

  async function display_QuantumResult() {
  
  const response = await fetch(`http://127.0.0.1:8000/result/`);
  if (response.ok) {
          const data = await response.json();
          const quantum_result = document.getElementById('quantum_result');
          const note = document.getElementById('note');
          quantum_result.innerText = `comparions needed: ${data.result}`;
          let speedupFactor = 256 / data.result;
          speedupFactor = speedupFactor.toFixed(3);
          note.innerHTML = `Quantum algorithm is working ${speedupFactor} times faster than Classical algorithm. <br> Note: As many times you compute, Quantum algorithm can show different results for the probabilistic nature of quantum computing`;
      } else {
          alert("Error fetching data from server.");
      }
    }
 function display_ClassicalResult(){
  const classical_result = document.getElementById('classical_result');
  classical_result.innerHTML = `comparions needed: 256`
 }
function smoothClick01() {
    const connectElement = document.querySelector('.conect');
    connectElement.classList.toggle('clicked');
    display_QuantumResult();
    display_ClassicalResult();
}
function smoothClick00() {
    const connectElement = document.querySelector('.conect');
    connectElement.classList.toggle('clicked');

}
