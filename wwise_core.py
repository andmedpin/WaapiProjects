from waapi import WaapiClient
from pprint import pprint
import object_data as wdata
import wwise_object as wobject

#client = WaapiClient()

if __name__ == '__main__':

    # Create a child Object of selected Work Unit
    parent_object_id = wdata.get_selected_object_id()

    temp_object = wobject.WwiseObject("Temp", parent_object_id)
    temp_id = temp_object.create_object("WorkUnit")

    loop_sound = temp_object.generate_temp_structure("Loop")
    oneShot_sound = temp_object.generate_temp_structure("OneShot")

    WaapiClient().call("ak.wwise.core.project.save")
    WaapiClient().disconnect()






