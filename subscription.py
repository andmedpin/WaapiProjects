from waapi import WaapiClient
from pprint import pprint
import object_data

client = WaapiClient()


def on_name_changed(*args, **kwargs):

    obj_type = kwargs.get("object", {}).get("type")

    old_name = kwargs.get("oldName")

    new_name = kwargs.get("newName")

    print(f"Object {old_name} (of type {obj_type}) was renamed to {new_name}\n")
    pprint(kwargs.get("object", {}))
    # client.disconnect()


def on_object_created(*args, **kwargs):
    object_selected = kwargs.get("object")
    object_id = object_selected.get('id')
    #object_type = object_selected.get('type')
    #object_parent = object_selected.get('parent')

    #pprint(kwargs)

    pprint(f'New Object created ID: {object_id}')


def on_object_selected(*args, **kwargs):
    object_selected = kwargs.get("objects")[0]
    object_id = object_selected.get('id')
    object_type = object_selected.get('type')
    object_parent = object_selected.get('parent')

    # pprint(kwargs)

    pprint(f'Object selected is of type: {object_type}, \n ID of the object: {object_id}, \n Parent: {object_parent}')


if __name__ == '__main__':
    '''
    handler_name = client.subscribe(
        "ak.wwise.core.object.nameChanged", 
        on_name_changed, 
        {"return": ["type", 'parent']}
    )

    handler_create = client.subscribe(
        "ak.wwise.core.object.created",
        on_object_created,
        {"return": ["id"]}
    )
    '''

    handler_select = client.subscribe(
        "ak.wwise.ui.selectionChanged",
        on_object_selected,
        {"return": ["type", "id", "parent"]}
    )

