from __future__ import print_function

import csv
import json
import urllib.request

startIdx =1
endIdx = 1000
apikey ='7bf86435a44949e08773'


url = 'http://openapi.foodsafetykorea.go.kr/api/'+apikey+'/COOKRCP01/json/'+str(startIdx)+'/'+str(endIdx)

data = urllib.request.urlopen(url).read()
output = json.loads(data)
#print(type(output))
output = json.loads(data)
output = output['COOKRCP01']
output = output['row']
print(output)
print(output[0].keys())
output_file = 'api_Outout.csv'

try:
    with open(output_file, 'w', newline='', encoding='UTF-8')as csvfile:
        writer = csv.DictWriter(csvfile,output[0].keys())
        writer.writeheader()
        for data in output:
            writer.writerow(data)
except:
    print("Error")