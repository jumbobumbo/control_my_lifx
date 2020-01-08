from common.config_reader import ReturnConfDict
from common.connector import ReturnConnectedLights as RCL
from datetime import datetime
from time import sleep

# config data we are using (blank means default)
config = ReturnConfDict().json_data

# # do we turn the light on or off?
# light_on = True if config["active_hours"]["group_1"]["start"] <= datetime.now().strftime("%H:%M:%S") <= \
#                    config["active_hours"]["group_1"]["end"] else False

# connect to the light(s)
with RCL([k for k, _ in config["lights"].items()]) as lights:
    for light in lights.devices:
        print(light.color)
        if light.color[2] < config["lights"][light.label]["color"][2]:
            light.set_color(config["lights"][light.label]["color"])
        else:
            light.set_color([0, 0, 0, 0])

