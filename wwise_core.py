from waapi import WaapiClient
from pprint import pprint
import object_data
import wwise_object


wdata = object_data
wobject = wwise_object


if __name__ == '__main__':

    # Create a child Object of selected Work Unit
    parent_object_id = wdata.get_selected_object_id()

    new_object = wobject.WwiseObject("amp_sound", "Sound", parent_object_id)
    new_object.create_object()
    print(f"New Object Created, ID is {new_object.new_object_id}, Name is {new_object.name}")