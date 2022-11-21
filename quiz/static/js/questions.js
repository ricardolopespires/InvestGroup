
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


//what happen when 'Continue' Button Will Click
continueBtn.addEventListener("click", () => {
    quiz.style.display = "block";
    guide.style.display = "none";

    loadData();

});



let index = 0;
let progress = 0;
let total = 0;



async function call_api(id, question, answer, score, completed, data) {

    console.log('Api called')

    console.log(id, question, answer, score, completed, data)
    const rawResponse = await fetch('quiz/api/create/user/answer/', {

        method: 'POST',
        headers: {

            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": '{{ csrf_token }}'
            },

        body: JSON.stringify({

            csrfmiddlewaretoken: '{{ csrf_token }}' ,
            id: id,
            question: question,
            answer: answer,
            score: score,
            completed:completed,
            data: data,

            })


        }).then(result => result.json())

            .then(data => {
            console.log(data)

            var elements = document.querySelectorAll('.percent')
            var progres = document.querySelectorAll('.progress')
            
            for(var i =0;i<elements.length;i++){

                elements[i].textContent = data.data[i] + '%'
                progres[i].style = `--w:${data.data[i]};`

               }
            })
            // const content = await rawResponse.json();

            // console.log(content);

        }




var d = new Date();
var datestring = d.getDate()  + "-" + (d.getMonth()+1) + "-" + d.getFullYear() + " " + d.getHours() + ":" + d.getMinutes();



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

    total = MCQS.questions[index].length


}


option1.addEventListener('click', ()=>{

  if( index !== total -1){ 

        id = create_UUID();
        question = questionText.innerText;
        answer = option1.innerText;
        score = 0; 
        completed = true;       
        data = datestring;
        call_api(id, question, answer, score, completed, data)
        index++;
        loadData();


        

          

    } else {
        
        quiz.style.display = "none";
        result.style.display = "block";

        points.innerHTML = `Parabens`;
        
        };
})


option2.addEventListener('click', ()=>{

  if( index !== total -1){

        question_uid =  questionText.innerText;
        answer_uid = option2.innerText;
        call_api(question_uid,answer_uid) 
        index++;
        loadData();

    } else {
        
        quiz.style.display = "none";
        result.style.display = "block";

        points.innerHTML = `Parabens`;
        
        };
})


option3.addEventListener('click', ()=>{

  if( index !== total -1){

        question_uid =  questionText.innerText;
        answer_uid = option3.innerText;
        call_api(question_uid,answer_uid) 
        index++;
        loadData();

    } else {
        
        quiz.style.display = "none";
        result.style.display = "block";

        points.innerHTML = `Parabens`;
        
        };
})

