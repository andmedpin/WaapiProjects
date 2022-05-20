from waapi import WaapiClient
from pprint import pprint

# Variables
client = WaapiClient()


def get_selected_object_id():
    # Get user's selected object data in Wwise

    selected_object = client.call('ak.wwise.ui.getSelectedObjects')

    selected_object_id = str(selected_object.get('objects')[0].get('id'))
    return selected_object_id


def get_object_data(data):
    args = {
        # "from": {"path": ['\\Actor-Mixer Hierarchy\\Default Work Unit']},
        # "from":  {"ofType": ["Sound"]},
        "from": {"id": [get_selected_object_id()]}
    }

    options = {
        "return": ['id', 'filePath', 'parent', 'name', 'type', 'notes']
    }

    object_data = client.call("ak.wwise.core.object.get", args, options=options)

    match data:
        case "id":
            return object_data.get('return')[0].get('id')

        case "name":
            return object_data.get('return')[0].get('name')

        case "type":
            return object_data.get('return')[0].get('type')

        case "parent":
            return object_data.get('return')[0].get('parent')

        case "notes":
            return object_data.get('return')[0].get('notes')

        case "all":
            return object_data.get('return')[0]


if __name__ == '__main__':

    requested_data = "name"
    pprint(f"Object's {requested_data}: {get_object_data(requested_data)}")

client.disconnect()
