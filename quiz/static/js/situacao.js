

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
let situacao = document.querySelector('#situacao');
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


        dados.situation = true
        updateUsuario(usuario, dados);
        
    })
}



async function updateSituacao(id, usuario){

    console.log('Gerando o perfil do  investidor')   
    var csrf_token = readCookie('csrftoken');
    let url = "http://localhost:8000/quiz/situacao/usuario/update/" + id + "/"


    let response = await fetch(url,{


        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrf_token

        },
        body:JSON.stringify({'id':id,'usuario':[usuario]})

    }).then(resp => resp.json())
    .then(data =>{

        console.log(data)
    })
}



async function loadSituacao(usuario, correct){


    let response = await fetch("http://localhost:8000/quiz/situacao/usuario/list/")
    .then((response) => response.json())

    .then((data) =>{

        

            let endividado = data[0];
            let equilibrado = data[1];
            let investidor = data[2];


            if(correct >=  investidor.minimum && correct <  investidor.maximum ){

                situacao.innerHTML = "Investidor";
                situacao.style.color = "#00e600";

                console.log(correct)

                //Atualizando a situação do usuário               
                updateSituacao(investidor.id, usuario);

                


            }else if(correct >= equilibrado.minimum && correct < equilibrado.maximum){
                
                situacao.innerHTML = "Equilibrado";
                situacao.style.color = "#ffff00";

                console.log(correct)

                //Atualizando a situação do usuário               
                updateSituacao(equilibrado.id, usuario);



                

            }else if(correct >= endividado.minimum && correct < endividado.maximum){

                situacao.innerHTML = "Endividado";
                situacao.style.color = "#ff0000";

                console.log(correct)

                //Atualizando a situação do usuário               
                updateSituacao(endividado.id, usuario);

               

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


    let response = await fetch('http://localhost:8000/quiz/situacao/questions/list/')
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
        

        A = MCQS.questions[index].A;
        B = MCQS.questions[index].B;
        C = MCQS.questions[index].C;
       


        usuario = MCQS.questions[index].user

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
        
        loadSituacao(usuario,correct);
        quiz.style.display = "none";
        result.style.display = "block";

        // Atualizando a conclusão do questionário
        loadUsuario(usuario);

        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/quiz/financial/perfil/";
        }, 5000);


     
        
        
        };
})


option2.addEventListener('click', ()=>{

  if( index !== total -1){

        correct = correct + B;
        index++;
        loadData();

    } else {
        
        loadSituacao(usuario, correct);
        quiz.style.display = "none";
        result.style.display = "block";

        // Atualizando a conclusão do questionário
        loadUsuario(usuario);

        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/quiz/financial/perfil/";
        }, 5000);

    
        
        
        };
})


option3.addEventListener('click', ()=>{

  if( index !== total -1){

        correct = correct + C;
        index++;
        loadData();

    } else {

        loadSituacao(usuario, correct);
        quiz.style.display = "none";
        result.style.display = "block";

        // Atualizando a conclusão do questionário
        loadUsuario(usuario);

        // Redireciona o usuário para dashbaord após cinco segundos
        setTimeout(function() {
            window.location.href = "http://localhost:8000/quiz/financial/perfil/";
        }, 5000);

      
        
        };
})




