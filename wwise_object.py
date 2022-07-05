from waapi import WaapiClient
from pprint import pprint
import object_data



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
        self.client.disconnect()
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

    def generate_temp_structure(self, suffix, path):
        name = self.name
        parent = self.parent
        temp_wu_id = self.object_id
        temp_source = TempSource(name, parent, suffix, temp_wu_id, path)


class TempSource(WwiseObject):

    def __init__(self, name, parent, suffix, temp_wu_id, path):
        self.suffix = suffix
        self.temp_wu_id = temp_wu_id
        self.path = path
        super(TempSource, self).__init__(name, parent)
        print(f"{name}Source class created, suffix is: {suffix}, parent's ID is: {self.temp_wu_id}, path is {path}")
        # Run when Instantiating a new Temp Source Class
        self.new_source = self.create_temp_source(f"{name}_{suffix}")

    def create_temp_source(self, name):
        if self.suffix == "Loop":
            isloop = True
        else:
            isloop = False

        args = {
            "importOperation": "createNew",
            "default": {},
            "imports": [
                {
                    "importLanguage": "SFX",
                    "@Volume": "1",
                    "@IsLoopingEnabled": isloop,
                    "objectPath": f"{self.path}\\<Sound SFX>{name}",
                    "audioFile": "C:\\Users\\andme\\music.wav",
                }
            ]
        }

        temp_source = self.client.call("ak.wwise.core.audio.import", args)
        temp_source_id = temp_source["objects"][1]["id"]
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


