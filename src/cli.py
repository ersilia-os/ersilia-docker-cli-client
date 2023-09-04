import click
from .fetch import ModelFetcher
from .serve import ModelServer
from .delete import ModelDeleter


@click.group()
def ersilia_group():
    """Ersilia Docker Interface"""
    pass


@ersilia_group.command()
@click.argument("model", type=click.STRING)
def fetch(model):
    click.echo("Fetching model from DockerHub...")
    model_id = model
    ModelFetcher(model_id=model_id).run()


@ersilia_group.command()
@click.argument("model", type=click.STRING)
def serve(model):
    click.echo("Serving model as a Docker container")
    model_id = model
    ModelServer(model_id=model_id).run()


@ersilia_group.command()
@click.option("--input", "-i", default=None, type=click.STRING)
@click.option("--output", "-o", default=None, type=click.STRING)
def run(input, output):
    click.echo("Running model")
    

@ersilia_group.command()
@click.argument("model", type=click.STRING)
def delete():
    click.echo("Deleting")
    model_id = model
    ModelDeleter(model_id=model_id).run()


if __name__ == "__main__":
    ersilia_group()
