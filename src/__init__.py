from pathlib import Path
from .cli import ersilia_group

EOS = str(Path.home())

if __name__ == "__main__":
    ersilia_group()
