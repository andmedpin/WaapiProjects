from waapi import WaapiClient
from pprint import pprint

# Variables
client = WaapiClient()
wwise_core = "ak.wwise.core"


args = {
    "from": {"path": ['\\Actor-Mixer Hierarchy\\Default Work Unit']},
    #"from" :  {"ofType" : ["Sound"]}
}

options = {
    "return": ['id', 'name','type', "filePath"]
}

result = client.call(f"{wwise_core}.object.get", args, options = options)

pprint(result)

client.disconnect()