from common.config_reader import ReturnConfDict
from common.connector import ReturnConnectedLights as RCL
from datetime import datetime


# config data we are using (blank means default)
config = ReturnConfDict().json_data

# connect to the light(s)
with RCL([k for k, v in config["lights"].items()]) as lights:
    # current light(s) status (off, on, somewhere in between)
    light_status = [light.get_power() for light in lights.devices]

    # do we turn the light on or off?
    if datetime.now().strftime("%H:%M:%S") >= config["active_hours"]["group_1"]["start"]:
        # TODO: include end time - include light status here too
        pass
