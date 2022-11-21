

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






function fazGet(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send()
    return request.responseText

}




function fazPost(url, body) {
    console.log("Body=", body)
    let request = new XMLHttpRequest()
    request.open("POST", url, true)
    request.setRequestHeader("Content-type", "application/json")
    request.send(JSON.stringify(body))

    request.onload = function() {
        console.log(this.responseText)
    }

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


