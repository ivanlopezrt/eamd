import librouteros as lr
from librouteros.query import Key
import json


def block(what='chatgpt3'):
    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]

    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]

    try:
        api = lr.connect(username=myJSON['user'], password=myJSON['password'], host=myJSON['IP'])
        name = Key('src-address-list')
        disabled = Key('disabled')
        chain = Key('chain')
        comment = Key('comment')
        exists_rule=false
        for row in api.path('/ip/firewall/raw').select(name, disabled, chain, comment).where(comment == what):
            api.path('/ip/firewall/raw').update(row['.id'], disabled='no')
            exists_rule=true

        if not exists_rule:
            raise Exception('La regla '+what+' no está definida para este aula')

        api.close()
    except:
        raise Exception('No se pudo conectar al router')

def isBlocked(what='chatgpt3'):
    myJSON = json.load(open('mydata.json'))
    myJSON=myJSON['credentials'][0]

    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]

    try:
        api = lr.connect(username=myJSON['user'], password=myJSON['password'], host=myJSON['IP'])
        name = Key('src-address-list')
        disabled = Key('disabled')
        chain = Key('chain')
        comment = Key('comment')

        for row in api.path('/ip/firewall/raw').select(name, disabled, chain, comment).where(comment == what):
            return not row['disabled']

        raise Exception('La regla '+what+' no está definida para este aula')

        api.close()

    except Exception as e:
        raise Exception('No se pudo conectar al router: '+str(e))


