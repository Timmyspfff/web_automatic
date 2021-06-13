import re
import time
import random
import numpy as np
import requests as rq

url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLScQTsGdrI5PfIYUsJC3kdQWJCyMQzYX5RwYlpT-5aennKxsSw/formResponse'
payload = {
    'entry.387343807' : '', #id
    'entry.369163648' : '', #name
    'entry.73088711' : '', #cadre
    
    'entry.1722051741' : '', #1
    'entry.1155660626' : '', #2
    'entry.560113875' : '', #3
    'entry.1688089788' : '', #4
    'entry.1401471979' : '', #5
    'entry.1568630711' : '', #6
    'entry.719295558' : '', #7
    'entry.362554963' : '', #8
    'entry.892083725' : '', #9
    'entry.513656425' : '', #10
    'entry.1798026279' : '', #11
    'entry.1195300752' : '', #12
    'entry.1204202649' : '', #13
    'entry.115600557' : '', #14
    'entry.404724722' : '', #15
    'entry.19683479' : '', #16
    'entry.538141642' : '', #17
    'entry.141883837' : '', #18
    'entry.756993637' : '', #19
    'entry.72749745' : '', #20
    'entry.2046334720' : '', #21
    'entry.1497590471' : '', #22
    'entry.1780914011' : '', #23
    'entry.1209084240' : '', #24
    'entry.462644779' : '', #25
    'entry.1966948704' : '', #26
    'entry.1145846294' : '', #27
    'entry.530965475' : '', #28
    'entry.1017508159' : '', #29
    'entry.2080597283' : '', #31
    'entry.383694655' : '', #32
    'entry.1466927808' : '', #33
    'entry.1108313939' : '', #35
    'entry.552391914' : '', #36
    'entry.1012854127' : '', #37
    'entry.499684835' : '', #38
    'entry.1676840899' : '', #40
    'entry.763742411' : '', #41
    'entry.69293297' : '', #42

    'entry.919606571' : '', #response
    'fvv' : '0',
    'draftResponse' : '[]',
    'pageHistory' : '0',
    'fbzx' : '-4212271211209408115'
}

print('輸入學號')
stuId = input()
print('輸入名字')
stuName = input()

cadres ={
            '1': '無',
            '2': '班代',
            '3': '副班代',
            '4': '學藝股長',
            '5': '總務股長',
            '6': '輔導股長',
            '7': '康樂股長',
            '8': '衛生股長',
            '9': '其他班級幹部',
        }
print(cadres)
print('你擔任的幹部輸入對應的數字')
cadre = cadres.get(input())
print("擔任幹部為:"+cadre)

a = int(input())
b = int(input())

def randseg():
    segment = random.randrange(1,10)
    return segment

period = np.arange(0.5, 5.0, 0.1)
delay = 0  # delay of execution

try:
    payload['entry.387343807'] = stuId
    payload['entry.369163648'] = stuName
    payload['entry.73088711'] = cadre

    payload['entry.1722051741'] = randseg() #1
    payload['entry.1155660626'] = randseg() #2
    payload['entry.560113875'] = randseg() #3
    payload['entry.1688089788'] = randseg() #4
    payload['entry.1401471979'] = randseg() #5
    payload['entry.1568630711'] = randseg() #6
    payload['entry.719295558'] = randseg() #7
    payload['entry.362554963'] = randseg() #8
    payload['entry.892083725'] = randseg() #9
    payload['entry.513656425'] = randseg() #10
    payload['entry.1798026279'] = randseg() #11
    payload['entry.1195300752'] = randseg() #12
    payload['entry.1204202649'] = randseg() #13
    payload['entry.115600557'] = randseg() #14
    payload['entry.404724722'] = randseg() #15
    payload['entry.19683479'] = randseg() #16
    payload['entry.538141642'] = randseg() #17
    payload['entry.141883837'] = randseg() #18
    payload['entry.756993637'] = randseg() #19
    payload['entry.72749745'] = randseg() #20
    payload['entry.2046334720'] = 8 #21
    payload['entry.1497590471'] = randseg() #22
    payload['entry.1780914011'] = randseg() #23
    payload['entry.1209084240'] = randseg() #24
    payload['entry.462644779'] = randseg() #25
    payload['entry.1966948704'] = randseg() #26
    payload['entry.1145846294'] = randseg() #27
    payload['entry.530965475'] = randseg() #28
    payload['entry.1017508159'] = randseg() #29
    payload['entry.2080597283'] = randseg() #31
    payload['entry.383694655'] = randseg() #32
    payload['entry.1466927808'] = randseg() #33
    payload['entry.1108313939'] = randseg() #35
    payload['entry.552391914'] = randseg() #36
    payload['entry.1012854127'] = randseg() #37
    payload['entry.499684835'] = randseg() #38
    payload['entry.1676840899'] = randseg() #40
    payload['entry.763742411'] = randseg() #41
    payload['entry.69293297'] = randseg() #42

    payload['entry.919606571'] = randseg() #response
    res = rq.post(url, data=payload)
    res.raise_for_status()
    if res.status_code == 200 :
        print('Done!')
    else:
        print("time out")
except rq.HTTPError:
    print('HTTP Error!')
 