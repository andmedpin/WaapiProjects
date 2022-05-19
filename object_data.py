from waapi import WaapiClient
from pprint import pprint

# Variables
client = WaapiClient()


def get_selected_object_id():
    # Get user's selected object data in Wwise

    selected_object = client.call('ak.wwise.ui.getSelectedObjects')

    selected_object_id = str(selected_object.get('objects')[0].get('id'))
    return selected_object_id


def get_object_data():
    args = {
        # "from": {"path": ['\\Actor-Mixer Hierarchy\\Default Work Unit']},
        # "from":  {"ofType": ["Sound"]},
        "from": {"id": [get_selected_object_id()]}
    }

    options = {
        "return": ['id', 'filePath', 'parent', 'name', 'type', 'notes']
    }

    object_data = client.call("ak.wwise.core.object.get", args, options=options)

    return object_data


if __name__ == '__main__':
    data_list = get_object_data().get('return')[0]

    print(f'Object\'s ID: {data_list.get("id")}')
    print(f'Object\'s Name: {data_list.get("name")}')
    print(f'Object\'s Type: {data_list.get("type")}')
    print(f'Object\'s Parent: {data_list.get("parent")}')
    print(f'Object\'s Notes: {data_list.get("notes")}')


client.disconnect()
