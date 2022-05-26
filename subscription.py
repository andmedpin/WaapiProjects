from waapi import WaapiClient
from pprint import pprint
import object_data

client = WaapiClient()


def on_name_changed(*args, **kwargs):
    obj_type = kwargs.get("object", {}).get("type")

    old_name = kwargs.get("oldName")

    new_name = kwargs.get("newName")

    print(f"Object {old_name} (of type {obj_type}) was renamed to {new_name}\n")
    # pprint(kwargs.get("object", {}))
    # client.disconnect()


def on_object_created(*args, **kwargs):
    new_object = kwargs.get("object", {})
    object_id = kwargs.get("id")
    pprint(f'New Object created. {object_id}')


if __name__ == '__main__':
    # handler = client.subscribe("ak.wwise.core.object.nameChanged", on_name_changed, {"return": ["type","pluginName"]})
    client.subscribe(
        "ak.wwise.core.object.created",
        on_object_created,
        {"return": ["type", "id", "name"]}
    )
