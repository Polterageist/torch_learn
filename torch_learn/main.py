import click
from torch_learn.introduction.quickstart import quickstart


@click.group()
def cli():
    pass


cli.add_command(quickstart)

if __name__ == '__main__':
    cli()
