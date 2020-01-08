from common.config_reader import ReturnConfDict
from common.connector import ReturnConnectedLights as RCL
from datetime import datetime

# config data we are using (blank means default)
config = ReturnConfDict().json_data

c_time = datetime.now().strftime("%H:%M:%S")
# connect to the light(s)
with RCL([k for k, _ in config["lights"].items()]) as lights:
    for light in lights.devices:
        # are we within active hours?
        if config["active_hours"][config["lights"][light.label]["group"]]["start"] <= c_time < \
                config["active_hours"][config["lights"][light.label]["group"]]["end"]:
            # if color[2] (brightness) is lower than config - turn on - if its the same, leave it alone
            if light.get_color()[2] < config["lights"][light.label]["color"][2]:
                light.set_color(config["lights"][light.label]["color"])
        else:  # turn off
            light.set_color([0, 0, 0, 0])
