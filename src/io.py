from . import EOS
import os
import json


class InputForwarder(object):
    def __init__(self, data, tag):
        self.data = data
        self.tag = tag
        self.eos_dir = os.path.join(EOS, "tmp", self.tag)
        if not os.path.exists(self.eos_dir):
            os.makedirs(self.eos_dir)
        self.is_file = False
        if type(self.data) is str:
            if self.data.endswith(".csv"):
                self.input_file = os.path.join(self.eos_dir, "input.csv")
                self.is_file = True
            elif self.data.endswith(".tsv"):
                self.input_file = os.path.join(self.eos_dir, "input.tsv")
                self.is_file = True
            elif self.data.endswith(".json"):
                self.input_file = os.path.join(self.eos_dir, "input.json")
                self.is_file = True
            else:
                self.data = json.loads(self.data)
                self.input_file = os.path.join(self.eos_dir, "input.json")
        else:
            self.input_file = os.path.join(self.eos_dir, "input.json")

    def run(self):
        if self.is_file:
            os.copy(self.data, self.input_file)
        else:
            with open(self.input_file, "w") as f:
                json.dump(self.data, f)


class OutputForwarder(object):
    def __init__(self, data, tag):
        self.data = data
        self.tag = tag
        self.eos_dir = os.path.join(EOS, "tmp", self.tag)
        for l in os.listdir(self.eos_dir):
            if l.startswith("output"):
                self.output_file = os.path.join(self.eos_dir, l)

    def run(self):
        if self.data is None:
            with open(self.output_file, "r") as f:
                return json.load(f)
        else:
            os.copy(self.output_file, self.data)
            return self.data
