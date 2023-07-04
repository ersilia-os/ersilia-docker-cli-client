import subprocess


class ContainerManager(object):
    def __init__(self):
        self.container_name = "ersilia_shell"
        self.image_name = "ersiliaos/shell"

    def is_available(self):
        result = subprocess.run(
            ["docker", "ps", "-q", "-f", "name={0}".format(self.container_name)],
            stdout=subprocess.PIPE,
        )
        return result.stdout.decode("utf-8").strip() != ""

    def start(self):
        pass

    def stop(self):
        pass

    def delete(self):
        pass
