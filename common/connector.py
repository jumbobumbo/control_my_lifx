from lifxlan import LifxLAN


class ReturnConnectedLights:
    def __init__(self, device_list):
        """
        -- MUST UTILISE WITH --
        returns connection object requested device(s)
        :param device_list: lst
        """
        self.device_list = device_list

    def __enter__(self):
        self.connection = LifxLAN(len(self.device_list))
        return self.connection.get_devices_by_name(self.device_list)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close_socket()
