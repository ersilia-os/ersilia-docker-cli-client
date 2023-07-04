import subprocess
from . import EOS


class ImageManager(object):
    def __init__(self):
        self.image_name = "ersiliaos/shell:latest"
        self.container_name = "ersilia_shell"

    def is_available(self):
        command = ["docker", "images", "-q", self.image_name]
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, _ = process.communicate()
        if process.returncode != 0:
            return False
        return output.strip() != b""

    def pull(self):
        cmd = ["docker", "pull", "ersiliaos/shell:latest"]
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).wait()

    def run(self):
        cmd = [
            "docker",
            "run",
            "-v",
            EOS + ":/root/eos",
            "-v",
            "/var/run/docker.sock:/var/run/docker.sock",
            "-d",
            "--name",
            "--network",
            "host",
            self.container_name,
            self.image_name,
        ]
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).wait()

    def delete(self):
        cmd = ["docker", "rmi", "-f", self.image_name]
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).wait()
