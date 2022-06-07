from waapi import WaapiClient
from pprint import pprint
import object_data

# wwise_data = object_data.WwiseObjectData()


class WwiseObject:

    def __init__(self, name, object_type, parent):
        # self.data = object_data.WwiseObjectData()
        self.name = name
        self.object_type = object_type
        self.parent = parent
        self.new_object_id = ""
        self.client = WaapiClient()

    def get_info(self, data):
        requested_info = object_data.WwiseObjectData().get_object_data(data, self.new_object_id)
        # requested_info = wwise_data.get_object_data(data, self.new_object_id)
        # requested_info = self.data.get_object_data(data, self.new_object_id)
        return requested_info

    def create_object(self):
        args = {
            # "parent": "\\Actor-Mixer Hierarchy\\Default Work Unit",
            "parent": self.parent,
            "type": self.object_type,
            "name": self.name
        }

        new_object = self.client.call("ak.wwise.core.object.create", args)
        self.new_object_id = str(new_object.get('id'))
        self.client.disconnect()

if __name__ == '__main__':
    #amp = WwiseObject('Wwise Tone Generator', 'SourcePlugin')
    #amp.create_object()
    #pprint(amp.get_info('all'))
    #pprint(object_data.get_selected_object_id())

    pass


