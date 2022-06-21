import time

from waapi import WaapiClient
from pprint import pprint
import object_data

# wwise_data = object_data.WwiseObjectData()


class WwiseObject:

    def __init__(self, name, parent):
        # self.data = object_data.WwiseObjectData()
        self.name = name
        self.parent = parent
        self.object_id = ""
        self.client = WaapiClient()

    def get_info(self, data):
        requested_info = object_data.WwiseObjectData().get_object_data(data, self.object_id)
        # requested_info = wwise_data.get_object_data(data, self.new_object_id)
        # requested_info = self.data.get_object_data(data, self.new_object_id)
        return requested_info

    def create_object(self, object_type):
        args = {
            "parent": self.parent,
            "type": object_type,
            "name": self.name,
        }

        new_object = self.client.call("ak.wwise.core.object.create", args)
        # self.object_id = str(new_object.get('id'))
        self.object_id = new_object["id"]
        self.client.disconnect()
        return self.object_id

    def set_property(self, object, property, value):
        args = {
            "object": object,

            "property": property,

            "value": value
        }

        self.client.call("ak.wwise.core.object.setProperty", args)
        self.client.disconnect()

    def generate_temp_structure(self, suffix):
        name = self.name
        parent = self.parent
        temp_wu_id = self.object_id
        temp_source = TempSource(name, parent, suffix, temp_wu_id)
        #temp_source.generate_temp_structure("MY_Suffix")


class TempSource(WwiseObject):

    def __init__(self, name, parent, suffix, temp_wu_id):
        self.suffix = suffix
        self.temp_wu_id = temp_wu_id
        super(TempSource, self).__init__(name, parent)
        print(f"{name}Source class created, suffix is: {suffix}, parent's ID is: {self.temp_wu_id}")
        self.create_temp_source(f"{name}_{suffix}", self.temp_wu_id)

    def create_temp_source(self, name, parent):

        if self.suffix == "Loop":
            isloop = True
        else:
            isloop = False

        args = {
            "parent": parent,
            "name": name,
            "type": "Sound",
            "@IsLoopingEnabled": isloop
        }

        temp_source = self.client.call("ak.wwise.core.object.create", args)
        temp_source_id = temp_source["id"]
        self.client.disconnect()

        return temp_source_id

        # actor mixer hierarchy
        # DONE create work unit under selected parent
        # DONE create one shot sound object
        # DONE create lp sound object
        # import audio for both objects

        # stretch goal, give the option to add attenuation

        # event tab
        # add work unit under
        # crete events


if __name__ == '__main__':
    pass


