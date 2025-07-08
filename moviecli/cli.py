import click
from ytswebs import *

@click.command
@click.argument('movie')
def search(movie):
    results = search_movie(movie)
    click.echo(results)


if __name__=='__main__':
    search()