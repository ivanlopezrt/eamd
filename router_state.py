import librouteros as lr
from librouteros.query import Key
import json

def blocked_chatgpt():
    myJSON = json.load(open('mydata.json'))

    api = lr.connect(username=myJSON['user'], password='ilm2017.dpm', host='192.168.1.1')
    print(api.path())
    name = Key('src-address-list')
    disabled = Key('disabled')
    chain = Key('chain')
    comment= Key('comment')

    for row in api.path('/ip/firewall/raw').select(name, disabled,chain,comment).where(comment=='chatgpt3'):
        return row['disabled']

    raise Exception('La regla chatgpt3 no está definida para este aula')

    api.close()


print(blocked_chatgpt())