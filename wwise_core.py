from waapi import WaapiClient
from pprint import pprint
import object_data as wdata
import wwise_object as wobject

# file import
#import easygui
#file = easygui.fileopenbox()

if __name__ == '__main__':

    # Variables
    utility_name = "Utility"

    # Create a child Object of selected Work Unit
    parent_object_id = wdata.get_selected_object_id()

    temp_object = wobject.WwiseObject(utility_name, parent_object_id)
    temp_id = temp_object.create_object("WorkUnit")

    # Get Relative Path of the WU for the Sound Object
    obj_data_path = temp_object.get_info("path")

    # Import Audio and Generate Sound Objects
    loop_sound = temp_object.generate_temp_structure("Loop", obj_data_path)
    oneShot_sound = temp_object.generate_temp_structure("OneShot", obj_data_path)

    WaapiClient().call("ak.wwise.core.project.save")
    WaapiClient().disconnect()


