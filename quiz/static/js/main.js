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
let option4 = document.querySelector("#option4");

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

//total points
let correct = 0;

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


//Creating Timer For Quiz Timer Section

let countDown = () => {
    if (timer === 20) {
        choice_que[MCQS[index].answer].classList.add("correct");
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






let loadData = () => {
    let data = fazGet('http://localhost:8000/quiz/api/questions/list/');
    let MCQS = JSON.parse(data);

    total = MCQS.questions.length

    questionNo.innerText = index + 1 + ". ";
    questionText.innerText = MCQS.questions[index].question;   

    option1.innerText = MCQS.questions[index].choice1;
    option2.innerText = MCQS.questions[index].choice2;
    option3.innerText = MCQS.questions[index].choice3;
    option4.innerText = MCQS.questions[index].choice4;

    //    timer start
    timer = 0;


}


option1.addEventListener("click", () => {

    if( index !== total -1){


        index++;
        correct++
        loadData();

      
        } else {
        
        quiz.style.display = "none";
        result.style.display = "block";
        points.innerHTML = `Você acertou ${correct} de ${total}`;
        
        }

    })


option2.addEventListener("click", () => {

    if( index !== total -1){

        index++;
        correct++
        loadData();

        total_correct.innerHTML = `${correct} de ${total} Perguntas`;

        } else {
        
        quiz.style.display = "none";
        result.style.display = "block";
        points.innerHTML = `Você acertou ${correct} de ${total}`;
        
        }

    })


option3.addEventListener("click", () => {

    if( index !== total -1){

        index++;
        correct++
        loadData();

        total_correct.innerHTML = `${correct} de ${total} Perguntas`;

        } else {
        
        quiz.style.display = "none";
        result.style.display = "block";

        points.innerHTML = `Você acertou ${correct} de ${total}`;
        
        }

    })

//what happen when 'Continue' Button Will Click
continueBtn.addEventListener("click", () => {
    quiz.style.display = "block";
    guide.style.display = "none";


    correct++

    loadData();

    

    //    remove All Active Classes When Continue Button Will Click

    

    
});


////what happen when 'Next' Button Will Click
next_question.addEventListener("click", () => {
    //    if index is less then MCQS.length
    if (index !== total - 1) {
        index++;
               //question
        
        //result
        total_correct.innerHTML = `${correct} de ${total} Perguntas`;
        clearInterval(interval);
        interval = setInterval(countDown, 1000);
    } 
    for (i = 0; i <= 3; i++) {
        choice_que[i].classList.remove("disabled");
    }
})

//what happen when 'Quit' Button Will Click
quit.addEventListener("click", () => {
    window.location.reload();
});

//Start Again When 'Start Again' Button Will Clicked
startAgain.addEventListener("click", () => {
    window.location.reload();
});







