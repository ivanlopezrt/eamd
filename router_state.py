import librouteros as lr
from librouteros.query import Key
import json


class InexistingRuleException(Exception):
    """Raised when the rule to enable/disable does not exist"""
    pass

def change_state(what='chatgpt3',blocked=True):
    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]

    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]


    api = lr.connect(username=myJSON['user'], password=myJSON['password'], host=myJSON['IP'])
    name = Key('src-address-list')
    disabled = Key('disabled')
    chain = Key('chain')
    comment = Key('comment')
    id=Key('.id')
    exists_rule=False
    for row in api.path('/ip/firewall/raw').select(name,  disabled, chain, comment,id ).where(comment == what):
        params={'.id':row['.id'], 'disabled':not blocked}
        api.path('/ip/firewall/raw').update(**params)
        print(what+".blocked="+str(blocked))
        exists_rule=True

    if not exists_rule:
        raise InexistingRuleException('La regla '+what+' no está definida para este aula')
        api.close()
        return
    api.close()

def isBlocked(what='chatgpt3'):
    myJSON = json.load(open('mydata.json'))
    myJSON=myJSON['credentials'][0]

    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]


    api = lr.connect(username=myJSON['user'], password=myJSON['password'], host=myJSON['IP'])
    name = Key('src-address-list')
    disabled = Key('disabled')
    chain = Key('chain')
    comment = Key('comment')

    for row in api.path('/ip/firewall/raw').select(name, disabled, chain, comment).where(comment == what):
        return not row['disabled']

    raise InexistingRuleException('La regla '+what+' no está definida para este aula')
    api.close()



