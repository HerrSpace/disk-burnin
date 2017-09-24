
from burnin.camcontrol import camcontrol
from burnin.sas2ircu import sas2ircu


class Controller():
    def __init__(self, controller_id):
        self.id = controller_id
        self.reload()

    def reload(self):
        controller_data = sas2ircu(self.id)
        disk_ids = camcontrol()

        for device in controller_data['Physical Device']:
            device.update(
                {'Device IDs': disk_ids.get(device['Serial No'])}
            )

        self._devices = controller_data['Physical Device']

    def _dev_filter(self, **kwargs):
        for device in self._devices:
            if all([
                key in device and device[key] == value
                for key, value in kwargs.items()
            ]):
                yield device
