from datetime import datetime
startTime = datetime.now()

from os import system
system('cls')


import http.client, urllib.parse, json




conn		= http.client.HTTPSConnection("www.bitstamp.net")

conn.request("POST", '/api/ticker/')
response	= conn.getresponse()
res = response.read().decode()
conn.close()

bitstamp = json.loads(res)

print(bitstamp['last'])







conn		= http.client.HTTPSConnection("api.nicehash.com")

location	= [0, 1]

dat = []



algo		= open('algos.txt').readlines()

for i in range(len(algo)):
	algo[i] = algo[i].strip().split('	= ')
	print(algo[i])





conn.request("POST", '/api?method=buy.info')
response	= conn.getresponse()
res = response.read().decode()
conn.close()

scale = json.loads(res)

print()
print(scale['result']['algorithms'])
print()
for i in scale['result']['algorithms']:
	print(i['min_limit'], '	', i['speed_text'])
print(scale['result']['down_time'])
print(scale['result']['static_fee'])
print(scale['result']['min_amount'])
print(scale['result']['dynamic_fee'])





print()
print()
print('algo id	', 'algo price	', 'algo speed	')
print()



algoPrices = []







for i in location:
	conn.request("POST", '/api?method=stats.global.current' + '&location=' + str(i))
	response	= conn.getresponse()
	res = response.read().decode()
	conn.close()
	dat.append(json.loads(res))

	algoPrices.append([])

	for j in dat[i]['result']['stats']:
		algoPrices[i].append([j['price'], j['speed']])

		print(j['algo'], '	', j['price'], '	', j['speed'])

	print()
	print()
print()
print()
print()

print(algoPrices[0][28])





def getOrders(l, al):
	orders	= {'price': [], 'accepted_speed' : [], 'size' : []}
	hash	= 0.0

	print()

	print('/api?method=orders.get' + '&location=' + str(l) + '&algo=' + str(al))
	conn.request("POST", '/api?method=orders.get' + '&location=' + str(l) + '&algo=' + str(al))

	response	= conn.getresponse()
	print(response.status, response.reason)
	data = response.read().decode()
	conn.close()

	result = json.loads(data)

	print()
	print()


	for i in result['result']['orders']:
		if float(i['accepted_speed']):
			orders[			'price'].append(i['price'])
			orders['accepted_speed'].append(i['accepted_speed'])
			# print(i['price'], '	', i['accepted_speed'], '	')

	print()

	for i in range(len(orders['price'])):
		if orders['accepted_speed'][i]:

			# print(float(algoPrices[l][al][1]) / 10)
			if float(orders['accepted_speed'][i]) > (float(algoPrices[l][al][1]) / 2.5):			#40%
				orders['size'].append('5')
			elif float(orders['accepted_speed'][i]) > (float(algoPrices[l][al][1]) / 4):			#25%
				orders['size'].append('4')
			elif float(orders['accepted_speed'][i]) > (float(algoPrices[l][al][1]) / 10):			#10%
				orders['size'].append('3')
			elif float(orders['accepted_speed'][i]) > (float(algoPrices[l][al][1]) / 25):			#4%
				orders['size'].append('2')
			elif float(orders['accepted_speed'][i]) > (float(algoPrices[l][al][1]) / 40):			#2.5%
				orders['size'].append('1')
			else:																	#<10%
				orders['size'].append('0')
			# print(orders['price'][i], '	', orders['accepted_speed'][i], '	', orders['size'][i])
	# print(orders)
	# print(len(orders['price']))


	for i in range(len(orders['price'])-1, -1, -1):

		if hash > (float(algoPrices[l][al][1]) / 4):
			print(hash)
			break

		print(orders['price'][i], '	', orders['accepted_speed'][i], '	', orders['size'][i])

		if orders['size'][i] == '0':
			hash += float(orders['accepted_speed'][i])

		elif orders['size'][i] == '1':
			hash += float(orders['accepted_speed'][i])

		elif orders['size'][i] == '2':
			hash += float(orders['accepted_speed'][i])

		elif orders['size'][i] == '3':
			hash += (float(orders['accepted_speed'][i]) / 15)
			break

		elif orders['size'][i] == '4':
			hash += (float(orders['accepted_speed'][i]) / 8)
			break

		elif orders['size'][i] == '5':
			hash += (float(orders['accepted_speed'][i]) / 4)
			break



	print()
	print(hash)
	print()

	return hash, orders['price'][i]

av = 0




# for loc in result:
	# for alg in loc:
		# wo = 0
		# for ord in alg['result']['orders']:
			# if ord['alive']:
				# if ord['workers']:
					# if ord['accepted_speed']:
						# wo += ord['workers']
						# print(wo)
						# print(ord)
		# if wo:
			# algoPrices[result.index(loc)][loc.index(alg)].append(float(algoPrices[result.index(loc)][loc.index(alg)][1]) / wo)
			# print(algoPrices[result.index(loc)][loc.index(alg)])
		# print()
		# print()
		# print()

# print(result[0][5])


if __name__ == '__main__':
	print(getOrders(0, 28))

	print(datetime.now() - startTime)

