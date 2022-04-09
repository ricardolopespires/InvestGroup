












def adicionar(dados):

	api = get_object_or_404(API, nome = 'CoinMarketCap')
	api_id = api.id

				if query:

					parameters = {
					'start': str(query),
					'limit':'1',							
					'convert':'BRL'
					}

				else:
					parameters = {											
					'convert':'BRL'
					}

				headers = {
				'Accepts': 'application/json',
				'X-CMC_PRO_API_KEY': api.api_key,
				}
				session = Session()
				session.headers.update(headers)
				
				response = session.get(url, params=parameters)
				data_crypto = json.loads(response.text)


	tags_objs = []
	plataforma_objs = []
	blockchain_objs = []
					
					

	#Para as tags
	tags_list = [ x for x in data_crypto['data'][0]['tags'] ]

	try:
		for tag in tags_list:
			a, created = Tag.objects.get_or_create(nome = tag)
			tags_objs.append(a)
		except:
			pass


	#Gerando código do ativo
	codigo_blockchain = str(uuid4()).split('-')[4]

	try:
		for blockchain in API.objects.filter(id = api_id):
			blockchain_slug = slugify(blockchain.nome)
		 a, created = Blockchain.get_or_create( 
			id = codigo_blockchain, nome = blockchain.nome, slug = blockchain_slug,
			logo = blockchain.image,
			)
		blockchain_objs.append(a)
	except:
		pass		


	#Para as tags
	plataform_list = data_crypto['data'][0]['platform']

	#Gerando código do ativo
	codigo_plataforma = str(uuid4()).split('-')[4]

	try:
		for plataforma in plataform_list:
			plataforma_slug = slugify(plataforma)
			a, created = Plataforma.objects.get_or_create(
				id = codigo_plataforma, nome = plataforma,
				slug = plataforma_slug, simbolo = data_crypto['data'][0]['symbol'],
				token_address = " ", qr_code = " " )

			plataforma_objs.append(a)
	except:
		pass



	m, created = Cripto.objects.get_or_create(

		id  = data_crypto['data'][0]['symbol'],						
		logo = " ",
		nome = data_crypto['data'][0]['name'],
		slug = data_crypto['data'][0]['slug'],
		codigo = data_crypto['data'][0]['id'],					
		preco = data_crypto['data'][0]['quote']['BRL']['price'],
		volume = data_crypto['data'][0]['quote']['BRL']['price'],
		capitalizacao = data_crypto['data'][0]['max_supply'],
		diluicao = data_crypto['data'][0]['quote']['BRL']['fully_diluted_market_cap'],
		classificacao = data_crypto['data'][0]['cmc_rank'],
		circulacao = data_crypto['data'][0]['circulating_supply'],
		maximo = data_crypto['data'][0]['max_supply'],
		total = data_crypto['data'][0]['total_supply'],
		data_da_emissao = data_crypto['data'][0]['date_added'],
		periodo = 0,
		preço_da_emissao = 0,
		data_listagem = data_crypto['data'][0]['date_added'],
		updated = datetime.now(),
		num_market_pairs = data_crypto['data'][0]['num_market_pairs'],			
		last_updated = data_crypto['data'][0]['last_updated'],
		market_cap = data_crypto['data'][0]['quote']['BRL']['market_cap'],
		market_cap_dominance = data_crypto['data'][0]['quote']['BRL']['market_cap_dominance'],
		percent_change_1h = data_crypto['data'][0]['quote']['BRL']['percent_change_1h'],
		percent_change_24h = data_crypto['data'][0]['quote']['BRL']['percent_change_24h'],
		percent_change_30d = data_crypto['data'][0]['quote']['BRL']['percent_change_30d'],
		percent_change_60d = data_crypto['data'][0]['quote']['BRL']['percent_change_60d'],
		percent_change_7d = data_crypto['data'][0]['quote']['BRL']['percent_change_7d'],
		percent_change_90d = data_crypto['data'][0]['quote']['BRL']['percent_change_90d'],
		volume_24h = data_crypto['data'][0]['quote']['BRL']['volume_24h'],
		volume_change_24h = data_crypto['data'][0]['quote']['BRL']['volume_24h'],
		)



	m.tags.set(tags_objs)
	m.blockchain.set(blockchain_objs)
	m.plataforma.set(plataforma_objs)


	for tag in tags_objs:
		tag.cryptos.add(m)
		tag.save()


	for blockchain in blockchain_objs:
		blockchain.cryptos.add(m)
		blockchain.save()

	for plataforma in  plataforma_objs:
		plataforma.cryptos.add(m)
		plataforma.save()

	m.save()


	return render(request, 'crypto/manager/index.html',{ 'month':month,'data_crypto':data_crypto })
							


	