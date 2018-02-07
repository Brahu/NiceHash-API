from datetime import datetime
startTime = datetime.now()

from os import system
system('cls')


import http.client, urllib.parse, json


conn		= http.client.HTTPSConnection("api.nicehash.com")

location	= [0, 1]

dat = []






algo		= open('algos.txt').readlines()

for i in range(len(algo)):
	algo[i] = algo[i].strip().split('	= ')
for i in algo:
	print(i)

print()
print()
print('algo id	', 'algo price	', 'algo speed	')
print()

result = [[], []]
for i in algo:
	result[0].append(i[0])
	result[1].append(i[0])


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
print()

print(algoPrices[1][29])

for l in location:
	for al in algo:

		print('/api?method=orders.get' + '&location=' + str(l) + '&algo=' + str(al[0]))
		conn.request("POST", '/api?method=orders.get' + '&location=' + str(l) + '&algo=' + str(al[0]))

		response	= conn.getresponse()
		print(response.status, response.reason)
		data = response.read().decode()
		conn.close()

		result[l][int(al[0])] = json.loads(data)

av = 0

for loc in result:
	for alg in loc:
		wo = 0
		for ord in alg['result']['orders']:
			if ord['alive']:
				if ord['workers']:
					if ord['accepted_speed']:
						wo += ord['workers']
						# print(wo)
						# print(ord)
		if wo:
			algoPrices[result.index(loc)][loc.index(alg)].append(float(algoPrices[result.index(loc)][loc.index(alg)][1]) / wo)
			print(algoPrices[result.index(loc)][loc.index(alg)])
		print()
		print()
		print()

# print(result[0][5])

print(datetime.now() - startTime)
