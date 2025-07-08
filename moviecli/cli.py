import click
from ytswebs import *
from utils import *
from InquirerPy import inquirer

@click.command
@click.argument('movie')
def search(movie):
    results = search_movie(movie)
    choices, dict = format_search_results_into_choices(results)

    selection = inquirer.select(
        message="Select a movie:",
        default=choices[0],
        choices=choices,
        pointer='=>',
        instruction='Use arrow keys to navigate and Enter to select.',
    ).execute()

    click.secho(f'You selected {selection}', color="green")




if __name__=='__main__':
    search()