
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