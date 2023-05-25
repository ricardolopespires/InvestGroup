


let fixa = document.querySelector("#fixa");
let repetir = document.querySelector("#repetir");
var start = document.getElementById("fixa-repetir");



function calcular() {

    var valor = parseFloat(document.getElementById('valor').value, 10);
    var observacao = document.getElementById('observacao');
    var categoria = document.getElementById('categorias').value;
    var resume = document.getElementById('resumo-categoria');
    var vt = document.getElementById('resumo-valor');
    var moeda = document.getElementById('moeda');
    var cotacao = document.getElementById('cotacao');
    var forma = document.getElementById('forma');
    var conversao = document.getElementById('conversao');
    var resultado = document.getElementById('resultado');
    var total = document.getElementById('total');
    var valor_total = document.getElementById('valor-total');


    var fromCurrency = document.querySelector(".select").value;

    const toCurrency = 'BRL'

    

  if(fromCurrency == toCurrency){

    observacao.value = `${'R$'} ${valor}`;
    resume.innerHTML = categoria;
    vt.innerHTML = `${'R$'} ${valor}`;
    moeda.innerHTML = toCurrency;
    cotacao.innerHTML = `${'R$'} ${valor}`;
    forma.innerHTML = "O valor é na mesma moeda";
    conversao.innerHTML = 0;
    resultado.value = valor;
    total.innerHTML = toCurrency;
    valor_total.innerHTML = `${'R$'} ${valor}`;



  }else{

    let url = `https://v6.exchangerate-api.com/v6/f98031f8ef206b0ae84d79df/latest/${fromCurrency}`;
     // fetching api response and returning it with parsing into js obj and in another then method receiving that obj
    fetch(url).then(response => response.json()).then(result =>{
        let exchangeRate = result.conversion_rates[toCurrency]; // getting user selected TO currency rate
        let totalExRate = (valor * exchangeRate).toFixed(2); // multiplying user entered value with selected TO currency rate
        observacao.value = `${valor} ${fromCurrency} = ${totalExRate} ${toCurrency}`;
        resume.innerHTML = categoria;
        vt.innerHTML = `${fromCurrency} ${valor}`;
        moeda.innerHTML = toCurrency;
        cotacao.innerHTML = `${fromCurrency} ${valor}`;
        forma.innerHTML = "O valor é na mesma moeda";
        conversao.innerHTML = `${exchangeRate}`;
        total.innerHTML = toCurrency;
        resultado.value = `${totalExRate}`;
        valor_total.innerHTML = `${fromCurrency} ${totalExRate}`;




    }).catch(() =>{ // if user is offline or any other error occured while fetching data then catch function will run
        observacao.innerText = "algo deu errado";
    });


    } 
  }





fixa.addEventListener('click', ()=>{

if($('#fixa').css('display') === 'none')

        {
            start.style.display = 'block'
            start.style.display = 'none'

        }
        else
        {
            start.style.display = 'none'

        }


})


repetir.addEventListener('click', ()=>{


        if($('#fixa-repetir').css('display') === 'none')
        {
            start.style.display = 'block'
            fixa.style.display = 'none'

        }
        else
        {
            start.style.display = 'none'

        }

    
})