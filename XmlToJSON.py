from os import system
system('cls')

def XmlToJSONNicehash(niceAlgo, niceHashrate, nicePower, niceMetric):
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
							if niceMetric == 'PH':
								hashrate.text = str(niceHashrate) * 1000
							else:
								hashrate.text = str(niceHashrate)
							# print('HashrateValue	:', hashrate.text)
						for metric in algo.iter('Metric'):
							if (niceMetric == 'kH') or (niceMetric == 'kSol')':
								metric.text = 'Kilo'
							if (niceMetric == 'MH') or (niceMetric == 'MSol'):
								metric.text = 'Mega'
							if (niceMetric == 'GH') or (niceMetric == 'GSol'):
								metric.text = 'Giga'
							if niceMetric == 'TH':
								metric.text = 'Tera'
							if niceMetric == 'PH':
								metric.text = 'Tera'
							# print('Metric	:', metric.text)
						for power in algo.iter('Power'):
							power.text = str(nicePower)
							# print('Power	:', power.text)

					# print()

	tree.write(path)

if __name__ == '__main__':
	XmlToJSONNicehash('Blake2s', 100, 8666.96*0.0000137, 'kH')

# 1000W == 1$
# 0.0137
# 69.33568

# 1000W	== 24$
# ?		== 0.118737352$