from urllib.request import *
from json import *
from requests import *
from sys import argv
# from matplotlib import pyplot as plt
# # import termplotlib as tpl
# # import gnuplotlib as gpl
# import asciichartpy as asc
# import termplotlib as tpl
# import numpy as np
import plotext as tplt

# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x) + x
# fig = tpl.figure()
# fig.plot(x, y, width=60, height=20)
# fig.show()

# def get_json(url):
# 	with urlopen(url) as response:
# 		html = response.read()
# 	htmlstr = html.decode("utf-8")
# 	return loads(htmlstr)


def get_new_cases()	:
	# response_daily = get('https://disease.sh/v3/covid-19/states/California?yesterday=1')
	# json = response_daily.json()
	# print(json['todayCases'])

	days = 360
	if len(argv) > 1:
		days = int(argv[1]) + 1
	if days > 120:
		day_tick = 30
	else:
		day_tick = 10
	response_last_month = get('https://disease.sh/v3/covid-19/nyt/states/California?lastdays=' + str(days))
	month_json = response_last_month.json()

	case_list = [day['cases'] for day in month_json]
	date_list = [-i for i in range(len(case_list),0,-1)]
	date_list.pop(0)
	# print(case_list)
	new_cases = [case_list[i+1] - case_list[i] for i in range(len(case_list) - 1)]
	# print(new_cases)

	tplt.plot(date_list, new_cases,fillx=True)
	tplt.title("California's New Covid Cases")
	tplt.xlabel('Days Ago')
	tplt.xticks([i for i in date_list if i%day_tick == 0])
	tplt.ylabel('New Cases')
	tplt.ylim(0, max(new_cases))
	tplt.show()

	# tplt.plot(new_cases[-30:])
	# tplt.title("California's New Covid Cases, Last Month")
	# tplt.xlabel('Day')
	# tplt.ylabel('New Cases')
	# tplt.show()
	# print(asc.plot(new_cases, {'height':15}))
	# asc.show()




















	# py_data = data.loads()
	# print(py_data[0])
	# data = loads(json)
	# for line in json:
	# 	print(line)
	# features = data['features']
	# newquakes = []
	# for feature in features:
	# 	newquake = quake_from_feature(feature)
	# 	# print(newquake)
	# 	# for quake in quakes:
	# 	# 	print(newquake == quake)  
	# 	if newquake not in quakes:
	# 		newquakes.append(newquake)
	# return newquakes

if __name__ == '__main__':
	get_new_cases()