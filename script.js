const formulario = document.getElementById("formulario")

const lista = document.getElementById("lista")

let funcionarios = []

formulario.addEventListener("submit,", function (event){
    event.preventDefault();
    
    const nome = document.getElementById("nome").value; 
    const cargo = document.getElementById("cargo").value;
    const matricula = document.getElementById("matricula").value;

    const funcionario = {
        nome: nome,
        cargo: cargo,
        matricula: matricula
    };
}
)

funcionarios.push(funcionario);
mostrarFuncionarios();

formulario.reset()

function mostrarFuncionarios(){
    lista.innerHTML = "";

    funcionarios.forEach(function(funcionario){
        lista.innerHTML += `

        <div class = "funcionario">
        <h3>${funcionario.nome}</h3>
        <h3>${funcionario.cargo}</h3>
        <h3>${funcionario.matricula}</h3>
    })
        </div>
         `;
     });
}
