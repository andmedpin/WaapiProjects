from waapi import WaapiClient
from pprint import pprint
import object_data as wdata
import wwise_object as wobject


if __name__ == '__main__':

    # Create a child Object of selected Work Unit
    parent_object_id = wdata.get_selected_object_id()
    print(parent_object_id)

    temp_obj = wobject.WwiseObject("Temp3", parent_object_id)
    temp_id = temp_obj.create_object("WorkUnit")
    print(temp_id)
    temp_obj.generate_temp_structure("Loop")
    temp_obj.generate_temp_structure("OneShot")
