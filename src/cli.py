import click
from .fetch import ModelFetcher


@click.group()
def ersilia_group():
    """Ersilia Docker Interface"""
    pass


@ersilia_group.command()
@click.option(model_id)
def fetch(model_id):
    click.echo("Fetching model")
    ModelFetcher(model_id=model_id).run()


@ersilia_group.command()
@click.option()
def serve(model_id):
    click.echo("Serving model")
    # ModelServer(model_id=model_id).run()


@ersilia_group.command()
@click.option()
def run():
    click.echo("Running model")


@ersilia_group.command()
@click.option()
def delete():
    click.echo("Deleting")


if __name__ == "__main__":
    ersilia_group()
