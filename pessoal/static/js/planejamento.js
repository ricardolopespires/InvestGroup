var renda = '';
var button = document.querySelector("#button");
let atual = document.querySelector('#atual');
let basica = document.querySelector('#basica'); 
let vida = document.querySelector('#vida'); 
let investimento = document.querySelector('#investimento'); 
let rentabilidade = document.querySelector('#rentabilidade');
let objectivo = document.querySelector('#objectivo');    






function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}






async function planejamento(dados){

	
    var csrf_token = readCookie('csrftoken');

    let url = "create/"
    let response = await fetch(url,{

        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrf_token

        },
        body:JSON.stringify(dados)

    }).then(resp => resp.json())
    .then(data =>{

        console.log(data)
    })
}


let usuario = fetch('usuario/')
    .then(response => {
      // valida se a requisição falhou
      if (!response.ok) {
        return new Error('falhou a requisição') // cairá no catch da promise
      }

      // verificando pelo status
      if (response.status === 404) {
        return new Error('não encontrou qualquer resultado')
      }

      // retorna uma promise com os dados em JSON
      return response.json()
    })

function uuid4() {
  return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
    (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
  );
}



button.addEventListener('click', ()=>{

	renda = document.querySelector("#renda");		

  	if( renda.value > 0){

  		atual.innerHTML = renda.value;
  		atual.style.left = "40px;"
  		atual.style.color = "#33cc33"

  		basica.innerHTML = renda.value / 2
  		basica.style.color = "#33cc33"

  		vida.innerHTML = renda.value / 3
  		vida.style.color = "#33cc33"

  		investimento.innerHTML = renda.value / 5
  		investimento.style.color = "#33cc33"

        codigo = uuid4();

  		dados ={

  			"id":codigo,
  			"renda":parseFloat(renda.value),
  			"despesa":renda.value / 2,
  			"estilo":renda.value / 3,
  			"investir":parseFloat(renda.value / 5), 			
			"active":true,
			
  		}

  		

  	}

})



