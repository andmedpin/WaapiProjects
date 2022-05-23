from waapi import WaapiClient
from pprint import pprint
import object_data

# Variables
client = WaapiClient()
wwise_data = object_data.ObjectData()

class WwiseObject:

    def __init__(self, name):
        self.name = name
        self.new_object_id = ""
        self.info = wwise_data

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
    #amp_s = WwiseObject('amp_s')
    #amp_s.create_object()
    #pprint(amp_s.get_info('all'))
    pprint(wwise_data.debug())

client.disconnect()
