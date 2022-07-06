from waapi import WaapiClient
from pprint import pprint
import object_data
import tkinter as tk
from tkinter import filedialog as fd


# Utilities #

def get_audio_file_path(file_identifier):
    # Import Wave File
    tk.Tk().withdraw()

    filetypes = (
        ('wave Files', '*.wav'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(title=f'Select the {file_identifier} file', initialdir='/', filetypes=filetypes)
    filename = filename.replace("/", "\\")
    return filename


# Classes #

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
        return temp_source.new_source


class TempSource(WwiseObject):

    def __init__(self, name, parent, suffix, temp_wu_id, path):
        self.suffix = suffix
        self.temp_wu_id = temp_wu_id
        self.path = path
        super(TempSource, self).__init__(name, parent)
        print(f"{name}Source class created, suffix is: {suffix}, parent's ID is: {self.temp_wu_id}, path is {path}")
        # Run when Instantiating a new Temp Source Class
        self.new_source = self.create_temp_source(f"{self.name}_{self.suffix}")
        #self.new_event = self.create_temp_event(self.name, self.suffix)

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
                    "audioFile": get_audio_file_path(name),
                    # "audioFile": "C:\\Users\\andme\\music.wav",
                }
            ]
        }

        temp_source = self.client.call("ak.wwise.core.audio.import", args)
        temp_source_id = temp_source["objects"][1]["id"]
        self.client.disconnect()

        return temp_source_id

    def create_temp_event(self, name, suffix):

        print(f"{name}_____name")
        print(f"{suffix}_____suffix")
        print(f"{self.new_source}_____source id")

        args = {
            "parent": "\\Events",
            "type": "WorkUnit",
            "name": f"{name}",
            "onNameConflict": "merge",
            
            "children": [
                {
                    "type": "Event",
                    "name": f"{suffix}_Play",
                    "children": [
                        {
                            "name": "",
                            "type": "Action",
                            "@ActionType": 1,
                            "@Target": f"{self.new_source}"
                        }
                    ]
                },
                {
                    "type": "Event",
                    "name": f"{suffix}_Stop",
                    "children": [
                        {
                            "name": "",
                            "type": "Action",
                            "@ActionType": 2,
                            "@Target": f"{self.new_source}"
                        }
                    ]
                }
            ]
        }
        self.client.call("ak.wwise.core.object.create", args)
        self.client.disconnect()


if __name__ == '__main__':
    pass


