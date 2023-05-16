






async function loaPerfil(usuario, total){


	let response = await fetch("http://localhost:8000/quiz/profile/financial/perfil/list/")
	.then((response) => response.json())

	.then((data) =>{

			let arrojado = data[0];
			let agressivo = data[1];
			let conservador = data[2];
			let moderado = data[3];

			if(total >  conservador.minimum && total <  conservador.maximum ){

				console.log("O seu perfil de investidor é Conservador");

			}else if(total > moderado.minimum && total < moderado.maximum){
				
				console.log("O seu perfil de investidor é Moderado");

			}else if(total > arrojado.minimum && total < arrojado.maximum){

				console.log("O seu perfil de investidor é Arrojado");
			}else if(total > agressivo.minimum && total < agressivo.maximum){

				console.log("O seu perfil de investidor é Agressivo");

			}

	} )   
}



export default {loaPerfil};


