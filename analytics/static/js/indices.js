const request = require('request');
const cheerio = require('cheerio');


request('https://www.investing.com/indices/major-indices', function(err, res, body){

	if(err) console.log('Erro: ' + err);
	var $ = cheerio.load(body);

	$('.datatable_table__D_jso tr').each(function() {

		var percent = $(this).find('.table-browser_col-chg-pct__68CzJ tr').text().trim();

		console.log(percent)
	});



});