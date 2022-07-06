from waapi import WaapiClient
from pprint import pprint
import object_data as wdata
import wwise_object as wobject

if __name__ == '__main__':

    # Variables
    utility_name = "Temp"

    # Create a child Object of selected Work Unit
    parent_object_id = wdata.get_selected_object_id()

    temp_object = wobject.WwiseObject(utility_name, parent_object_id)
    temp_id = temp_object.create_object("WorkUnit")

    # Get Relative Path of the WU for the Sound Object
    obj_data_path = temp_object.get_info("path")

    # Import Audio and Generate Sound Objects
    loop_sound = temp_object.generate_temp_structure("Loop", obj_data_path)
    oneShot_sound = temp_object.generate_temp_structure("OneShot", obj_data_path)

    # Event Hierarchy
    args = {
        "parent": "\\Events",
        "type": "WorkUnit",
        "name": f"{utility_name}",
        "onNameConflict": "merge",
        "children": [
            {
                "type": "Event",
                "name": f"{utility_name}_Loop_Play",
                "children": [
                    {
                        "name": "",
                        "type": "Action",
                        "@ActionType": 1,
                        "@Target": f"{loop_sound}"
                    }
                ]
            },
            {
                "type": "Event",
                "name": f"{utility_name}_OneShot_Play",
                "children": [
                    {
                        "name": "",
                        "type": "Action",
                        "@ActionType": 1,
                        "@Target": f"{oneShot_sound}"
                    }
                ]
            },
            {
                "type": "Event",
                "name": f"{utility_name}_Stop",
                "children": [
                    {
                        "name": f"Stop_{oneShot_sound}",
                        "type": "Action",
                        "@ActionType": 2,
                        "@Target": f"{oneShot_sound}"
                    },
                    {
                        "name": f"Stop_{loop_sound}",
                        "type": "Action",
                        "@ActionType": 2,
                        "@Target": f"{loop_sound}"
                    }
                ]
            }
        ]
    }

    WaapiClient().call("ak.wwise.core.object.create", args)
    WaapiClient().disconnect()

    WaapiClient().call("ak.wwise.core.project.save")
    WaapiClient().disconnect()

    # stretch goal, give the option to add attenuation
