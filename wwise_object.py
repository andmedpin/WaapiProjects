from waapi import WaapiClient
from pprint import pprint
import object_data

# Variables
#client = WaapiClient()
#wwise_data = object_data.ObjectData()


class WwiseObject:

    def __init__(self, name):
        self.client = WaapiClient()
        #self.data = object_data.WwiseObjectData()
        self.name = name
        self.new_object_id = ""

    def get_info(self, data):
        requested_info = object_data.WwiseObjectData().get_object_data(data, self.new_object_id)
        #requested_info = self.data.get_object_data(data, self.new_object_id)
        return requested_info

    def create_object(self):

        args = {
            "parent": "\\Actor-Mixer Hierarchy\\Default Work Unit",
            "type": "Sound",
            "name": self.name
        }

        new_object = self.client.call("ak.wwise.core.object.create", args)
        self.new_object_id = str(new_object.get('id'))
        self.client.disconnect()


if __name__ == '__main__':
    #amp_s = WwiseObject('amp_s')
    #amp_s.create_object()
    #pprint(amp_s.get_info('all'))
    amp = WwiseObject('andres')
    amp.create_object()
    pprint(amp.get_info('type'))



