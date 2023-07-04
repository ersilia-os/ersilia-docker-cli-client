import subprocess
import uuid

from .io import InputForwarder, OutputForwarder


class ModelRunner(object):
    def __init__(self, model_id):
        self.model_id = model_id
        self.tag = str(uuid.uuid4())
        self.i_fwd = InputForwarder(model_id=self.model_id, tag=self.tag)
        self.o_fwd = OutputForwarder(model_id=self.model_id, tag=self.tag)

    def run(self, input_data, output_data):
        subprocess.Popen('docker -it exec "ersilia run "', shell=True).wait()
