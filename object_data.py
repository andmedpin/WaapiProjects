from waapi import WaapiClient
from pprint import pprint

# Variables
client = WaapiClient()


class ObjectData:
    def __init__(self):
        pass

    def get_selected_object_id(self):
        # Get user's selected object data in Wwise
        selected_object = client.call('ak.wwise.ui.getSelectedObjects')

        selected_object_id = str(selected_object.get('objects')[0].get('id'))
        return selected_object_id

    def get_object_data(self, data, object_id):
        args = {
            "from": {"id": [object_id]}
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

            case "path":
                return object_data.get('return')[0].get('filePath')

            case "all":
                return object_data.get('return')[0]

    def debug(self):
        pprint(self)


class WwiseObject:

    def __init__(self, name):
        self.name = name
        self.new_object_id = ""
        self.info = ObjectData()

    def get_info(self, data):
        return self.info.get_object_data(data, self.new_object_id)

    def create_object(self):

        args = {
            "parent": "\\Actor-Mixer Hierarchy\\Default Work Unit",
            "type": "Sound",
            "name": self.name
        }

        new_object = client.call("ak.wwise.core.object.create", args)
        self.new_object_id = str(new_object.get('id'))


if __name__ == '__main__':
    #amp_sound = WwiseObject("amp")
    #amp_sound.create_object()
    #pprint(amp_sound.get_info('all'))
    pass

client.disconnect()
