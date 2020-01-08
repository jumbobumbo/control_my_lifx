import json
from pathlib import Path


class ReturnConfDict:
    """
    json_file: file name - creates Path obj
    Example: JSONReads(json_file).json_data["key1"]
    """
    def __init__(self, json_file="default.json"):
        """
        json_file: Path OBJ to (and including) json file
        """
        # self.json_data = Path(str(Path.cwd()), "control_my_lifx/", "config/", json_file)
        self.json_data = Path(str(Path.cwd()), "config/", json_file)

    @property
    def json_data(self):
        return self.__json_data

    @json_data.setter
    def json_data(self, json_file):
        with open(json_file, "r") as f:
            self.__json_data = json.load(f)

    def __repr__(self):
        return str(self.json_data)
