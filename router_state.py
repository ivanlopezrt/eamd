import librouteros as lr
from librouteros.query import Key
import json

def blocked_chatgpt():
    myJSON = json.load(open('mydata.json'))
    myJSON=myJSON['credentials'][0]


    api = lr.connect(username=myJSON['user'], password=myJSON['password'], host=myJSON['IP'])
    print(api.path())
    name = Key('src-address-list')
    disabled = Key('disabled')
    chain = Key('chain')
    comment= Key('comment')

    for row in api.path('/ip/firewall/raw').select(name, disabled,chain,comment).where(comment=='chatgpt3'):
        return not row['disabled']

    raise Exception('La regla chatgpt3 no está definida para este aula')

    api.close()


def blocked(what='chatgpt3'):
    myJSON = json.load(open('mydata.json'))
    myJSON=myJSON['credentials'][0]