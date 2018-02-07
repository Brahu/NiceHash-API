from os import system
system('cls')

def XmlToJSONNicehash(niceAlgo, niceHashrate, nicePower):
	path = "C:/Users/tomek/AppData/Roaming/AwesomeMiner/ConfigData.xml"

	import xml.etree.ElementTree as ET
	import json

	tree = ET.ElementTree(file=path)
	root = tree.getroot()

	for profile in root.iter('ProfitProfile'):
		des	= str(profile.find('Description').text)

		if des	== 'NiceHashRate':

			for algo in profile.iter('AlgorithmSettings'):
				Enabled			= json.loads(algo.find('Enabled').text)
				if Enabled:
					# print('Enabled		:', Enabled)
					Algorithm		= str(algo.find('Algorithm').text)
					# print('Algorithm	:', Algorithm)
					if Algorithm	== niceAlgo:
						for hashrate in algo.iter('HashrateValue'):
							hashrate.text = str(niceHashrate)
							# print('HashrateValue	:', hashrate.text)
						# for metric in algo.iter('Metric'):
							# metric.text = 'Giga'
							# print('Metric	:', metric.text)
						for power in algo.iter('Power'):
							power.text = str(nicePower)
							# print('Power	:', power.text)

					# print()

	tree.write(path)

if __name__ == '__main__':
	XmlToJSONNicehash('Blake2s', 100, 100)
