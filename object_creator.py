from waapi import WaapiClient
from pprint import pprint

new_object_id = ''

client = WaapiClient()


def create_object():
    global new_object_id
    args = {
        "parent": "\\Actor-Mixer Hierarchy\\Default Work Unit",
        "type": "Sound",
        "name": "Boom"
    }

    new_object = client.call("ak.wwise.core.object.create", args)
    new_object_id = str(new_object.get('id'))

    # pprint(new_object)
    # pprint(new_object.keys())
    # pprint(new_object.items())
    # pprint(new_object_id)


def get_object_id():
    args = {
        # "from": {"path": ['\\Actor-Mixer Hierarchy\\Default Work Unit']},
        # "from": {"ofType": ["Sound"]}
        "from": {"id": [new_object_id]}
    }

    options = {
        "return": ['id', 'name', 'type', 'filePath']
    }

    object_info = client.call('ak.wwise.core.object.get', args, options=options)
    pprint(object_info)


def debug():
    print("AMP")
    # print(new_object_id)


if __name__ == '__main__':
    create_object()
    get_object_id()


client.disconnect()
