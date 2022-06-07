from waapi import WaapiClient
from pprint import pprint
import object_data as wdata
import wwise_object as wobject


if __name__ == '__main__':

    # Create a child Object of selected Work Unit
    parent_object_id = wdata.get_selected_object_id()

    new_object = wobject.WwiseObject("amp_sound", "Sound", parent_object_id)
    new_object.create_object()
    print(f"New Object Created, ID is {new_object.new_object_id}, Name is {new_object.name}")