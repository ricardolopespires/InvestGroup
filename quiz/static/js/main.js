//Start Section
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


//correct and next Button
let total_correct = document.querySelector("#total_correct");
let next_question = document.querySelector("#next_question");

//Result Section
let result = document.querySelector("#result");
let points = document.querySelector("#points");
let quit = document.querySelector("#quit");
let startAgain = document.querySelector("#startAgain");

//Get All 'H4' From Quiz Section (MCQS)
let choice_que = document.querySelectorAll(".choice_que");


let index = 0;
let total = 0;
let timer = 0;
let interval = 0;
let usuario = " ";
let codigo_id = " ";
//total points
let pontuacao = 0;

//store Answer Value
let UserAns = undefined;

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



//Creating Timer For Quiz Timer Section

let countDown = () => {
    if (timer === 20) {
        choice_que[MCQS[index].answer].classList.add("pontuacao");
        for (i = 0; i <= 3; i++) {
            choice_que[i].classList.add("disabled");
        }
        clearInterval(interval);
    } else {
        timer++;
        time.innerText = timer;
    }
}

 


function fazGet(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send()
    return request.responseText
}



async function createData(dados){

    console.log('Gerando as QuizTaker')

    var csrf_token = readCookie('csrftoken');
    let url = "user/answer/create/"
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



async function updateData(url, dados){

    console.log('Atualização do perfil do usuario')

    var csrf_token = readCookie('csrftoken');    
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




let loadData = () => {
    let data = fazGet('http://localhost:8000/api/questions/list/');
    let MCQS = JSON.parse(data);

   

    total = MCQS.questions.length

    questionNo.innerText = index + 1 + ". ";
    questionText.innerText = MCQS.questions[index].question;   

    option1.innerText = MCQS.questions[index].choice1;
    option2.innerText = MCQS.questions[index].choice2;
    option3.innerText = MCQS.questions[index].choice3;

    usuario = MCQS.questions[index].user

   

    //    timer start
    timer = 0;


}



option1.addEventListener("click", () => {

    if( index !== total -1){


        index++;        
        loadData();

        fetch('http://localhost:8000/api/questions/list/')
        .then(resp => resp.json())
        .then(data => {

            let user = data.questions[index].user
            let id = data.questions[index].question_id
            let score = data.questions[index].A
            let date_finished  = new Date();
            let question = data.questions[index].question_id
            let answer = data.questions[index].choice1_id

            pontuacao = pontuacao + score
            console.log(score)

            let dados = {

                "user":user,"id":id,"score":score,"completed": true,
                "date_finished":date_finished,"question":question,"answer":answer

                }

            createData(dados);

        })

       
      
        } else {
        
        fetch('list/')
        .then(resp => resp.json())
        .then(data => {

           console.log(data[0])
        })

        url = `situacao-update/${codigo_id}/`;

        dados = {"id": `${codigo_id}`,"condicao": " ","description": " ","minimum": ,"maximum": ,"usuario": [ ]}   
        updateData(url, dados)

        points.innerHTML = `Você acertou ${pontuacao} de ${total}`;
        
        }

    })


option2.addEventListener("click", () => {

    if( index !== total -1){

        index++;
        
        loadData();

        fetch('http://localhost:8000/api/questions/list/')
        .then(resp => resp.json())
        .then(data => {

            let user = data.questions[index].user
            let id = data.questions[index].question_id
            let score = data.questions[index].B
            let date_finished  = new Date();
            let question = data.questions[index].question_id
            let answer = data.questions[index].choice1_id

            pontuacao = pontuacao + score
            console.log(score)

            let dados = {

                "user":user,"id":id,"score":score,"completed": true,
                "date_finished":date_finished,"question":question,"answer":answer

                }

            createData(dados);

        })

        } else {
        
        fetch('list/')
        .then(resp => resp.json())
        .then(data => {s

            console.log(data[1].id)
        })

        url = `situacao-update/${codigo_id }/`;
        dados ={'usuario':[usuario]}
        updateData(url, dados)
        points.innerHTML = `Você acertou ${pontuacao} de ${total}`;
        
        }

    })


option3.addEventListener("click", () => {

    if( index !== total -1){

        index++;
        
        loadData();

        fetch('http://localhost:8000/api/questions/list/')
        .then(resp => resp.json())
        .then(data => {

            let user = data.questions[index].user
            let id = data.questions[index].question_id
            let score = data.questions[index].C
            let date_finished  = new Date();
            let question = data.questions[index].question_id
            let answer = data.questions[index].choice1_id

            console.log(score)

            pontuacao = pontuacao + score

            let dados = {

                "user":user,"id":id,"score":score,"completed": true,
                "date_finished":date_finished,"question":question,"answer":answer

                }

            createData(dados);

        })


        } else {
        
        quiz.style.display = "none";
        result.style.display = "block";

        fetch('list/')
        .then(resp => resp.json())
        .then(data => {

           console.log(data[2])
        })

        url = `situacao-update/${codigo_id}/`;
        dados ={'usuario':[usuario]}
        updateData(url, dados);

        points.innerHTML = `Você acertou ${pontuacao} de ${total}`;
        
        }

    })

//what happen when 'Continue' Button Will Click
continueBtn.addEventListener("click", () => {
    quiz.style.display = "block";
    guide.style.display = "none";    

    loadData();  
 
    
});




//what happen when 'Quit' Button Will Click
quit.addEventListener("click", () => {
    window.location.reload();
});

//Start Again When 'Start Again' Button Will Clicked
startAgain.addEventListener("click", () => {
    window.location.reload();
});







