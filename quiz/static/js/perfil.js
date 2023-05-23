

let start = document.querySelector("#start");

//guide Section
let guide = document.querySelector("#guide");
let exit = document.querySelector("#exit");
let continueBtn = document.querySelector("#continue");

//Quiz Section
let quiz = document.querySelector("#quiz");
let time = document.querySelector("#time");

//question Section
let questionNo = document.querySelector("#questionNo");
let questionText = document.querySelector("#questionText");

//Multiple Choices Of Questions
let option1 = document.querySelector("#option1");
let option2 = document.querySelector("#option2");
let option3 = document.querySelector("#option3");
let option4 = document.querySelector("#option4");

//correct and next Button
let total_correct = document.querySelector("#total_correct");
let next_question = document.querySelector("#next_question");

//Result Section
let respostas = document.querySelector("#total");
let result = document.querySelector("#result");
let points = document.querySelector("#answer");
let quit = document.querySelector("#quit");
let pontuacao = document.querySelector('#pontuacao');
let startAgain = document.querySelector("#startAgain");

//Get All 'H4' From Quiz Section (MCQS)
let choice_que = document.querySelectorAll(".choice_que");


let index = 0;
let timer = 0;
let interval = 0;
let total = 0
let A = 0;
let B = 0;
let C = 0;
let D = 0;
//total points
let correct = 0;

//store Answer Value
var usuario = "";



//what happen when 'Start' Button Will Click
start.addEventListener("click", () => {
    start.style.display = "none";
    guide.style.display = "block";
});

//what happen when 'Exit' Button Will Click
exit.addEventListener("click", () => {
    start.style.display = "block";
    guide.style.display = "none";
});


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






async function updateUsuario(usuario, dados){    


    var csrf_token = readCookie('csrftoken');
    let url = "http://localhost:8000/quiz/accounts/" + usuario + "/perfil/"
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



async function loadUsuario(usuario){

     console.log('Verificando os dados do usuario '+ usuario)
    let response = await fetch("http://localhost:8000/quiz/accounts/"+ usuario + "/detail/")
    .then((response) => response.json())
    .then(dados =>{


        dados['perfil'] = true

        console.log(dados)
        updateUsuario(usuario, dados);
        
    })
}



async function updatePerfil(id, dados){

    console.log('Gerando o perfil do  investidor')   

    var csrf_token = readCookie('csrftoken');
    let url = "http://localhost:8000/quiz/perfil/usuario/update/"+ id + "/"
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



async function loadPerfil(usuario, correct){


    let response = await fetch("http://localhost:8000/quiz/perfil/usuario/list/")
    .then((response) => response.json())

    .then((data) =>{

            let moderado = data[0];
            let dinamico = data[1];
            let agressivo = data[2];
            let conservador = data[3];


           
            if(correct >  conservador.minimum && correct <  conservador.maximum ){

                pontuacao.innerHTML = "Conservador";
                pontuacao.style.color = "#00e600";

                //Enviando os dados para o banco de dados
                conservador['usuario'] = [usuario];

                //Atualizando a perfil do usuário  
                updatePerfil(conservador.id, conservador);


            }else if(correct > moderado.minimum && correct < moderado.maximum){
                
                pontuacao.innerHTML = "Moderado";
                pontuacao.style.color = "#ffff00";

                //Enviando os dados para o banco de dados
                moderado['usuario'] = [usuario];
                console.log([usuario])

                //Atualizando a perfil do usuário  
                updatePerfil(moderado.id, moderado);

            }else if(correct > dinamico.minimum && correct < dinamico.maximum){

                pontuacao.innerHTML = "Dinâmico";
                pontuacao.style.color = "#ff9933";

                //Enviando os dados para o banco de dados
                dinamico['usuario'] = [usuario];

                //Atualizando a perfil do usuário  
                updatePerfil(dinamico.id, dinamico);

            }else if(correct > agressivo.minimum && correct < agressivo.maximum){

                pontuacao.innerHTML = "Agressivo";
                pontuacao.style.color = "#ff3300";

                //Enviando os dados para o banco de dados
                agressivo['usuario'] = [usuario];

                //Atualizando a perfil do usuário  
                updatePerfil(agressivo.id, agressivo);

            }

    } )   
}





//Creating Timer For Quiz Timer Section

let countDown = () => {
    if (timer === 60) {
        index;
        for (i = 0; i <= 3; i++) {
            choice_que[i].classList.add("disabled");
        }
        clearInterval(interval);
    } else {
        timer++;
        time.innerText = timer;
    }
}

//setInterval(countDown,1000);


async function loadData(){


    let response = await fetch('http://localhost:8000/api/perfil/questions/list/')
    .then((response) => response.json())
    .then((MCQS) => {

        respostas.innerText = MCQS.questions.length;
        points.innerText = index;

        total = MCQS.questions.length;

        questionNo.innerText = index + 1 + ". ";
        questionText.innerText = MCQS.questions[index].question;   

        option1.innerText = MCQS.questions[index].choice1;
        option2.innerText = MCQS.questions[index].choice2;
        option3.innerText = MCQS.questions[index].choice3;
        option4.innerText = MCQS.questions[index].choice4;

        A = MCQS.questions[index].A;
        B = MCQS.questions[index].B;
        C = MCQS.questions[index].C;
        D = MCQS.questions[index].D;


        //usuario 
        usuario = MCQS.questions[index].usuario
     



        //    timer start
        timer = 0;


    });

}



loadData();

//what happen when 'Continue' Button Will Click
continueBtn.addEventListener("click", () => {



    quiz.style.display = "block";
    guide.style.display = "none";

    interval = setInterval(countDown, 1000);
    
    //    remove All Active Classes When Continue Button Will Click

    choice_que.forEach(removeActive => {
        removeActive.classList.remove("active");
    })



   
});




option1.addEventListener('click', ()=>{

  if( index !== total -1 ){



        correct = correct + A;
        index++;        
        loadData();
          

          

    } else {
        
        loadPerfil(usuario,correct);
        quiz.style.display = "none";
        result.style.display = "block";

        // Atualizando a conclusão do questionário
        loadUsuario(usuarios);


        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/dashboard/manager/";
        }, 5000);

        

  
        };
})


option2.addEventListener('click', ()=>{

  if( index !== total -1){

        correct = correct + B;
        index++;
        loadData();
       

    } else {
        
        loadPerfil(usuario, correct);
        quiz.style.display = "none";
        result.style.display = "block";

        // Atualizando a conclusão do questionário
        loadUsuario(usuarios);

        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/dashboard/manager/";
        }, 5000);


        

        
        };
})


option3.addEventListener('click', ()=>{

  if( index !== total -1){

        correct = correct + C;
        index++;
        loadData();

    } else {

        loadPerfil(usuario, correct);
        quiz.style.display = "none";
        result.style.display = "block";

        // Atualizando a conclusão do questionário
        loadUsuario(usuario);

        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/dashboard/manager/";
        }, 5000);




        
        };
})



option4.addEventListener('click', ()=>{

  if( index !== total -1){

        correct = correct + D;
        index++;
        loadData();

    } else {
        
        loadPerfil(usuario, correct);
        quiz.style.display = "none";
        result.style.display = "block";


        // Atualizando a conclusão do questionário
        loadUsuario(usuario);

        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/dashboard/manager/";
        }, 5000);


      
        };
})


