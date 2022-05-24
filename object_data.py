from waapi import WaapiClient
from pprint import pprint


# Utilities #

def get_selected_object_id():
    client = WaapiClient()
    # Get user's selected object data in Wwise
    selected_object = client.call('ak.wwise.ui.getSelectedObjects')

    selected_object_id = str(selected_object.get('objects')[0].get('id'))
    client.disconnect()
    return selected_object_id


# Classes   #

class WwiseObjectData:
    def __init__(self):
        self.client = WaapiClient()

    def get_object_data(self, data, object_id):
        args = {
            "from": {"id": [object_id]}
        }

        options = {
            "return": ['id', 'filePath', 'parent', 'name', 'type', 'notes']
        }

        object_data = self.client.call("ak.wwise.core.object.get", args, options=options)

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

            case "path":
                return object_data.get('return')[0].get('filePath')

            case "all":
                return object_data.get('return')[0]
        self.client.disconnect()

    def debug(self, data):
        pprint(data)
        self.client.disconnect()


if __name__ == '__main__':
    pass
