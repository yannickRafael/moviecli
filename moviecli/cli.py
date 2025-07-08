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

    click.secho(f'You selected {selection}', fg="green")

    url = dict[selection]
    
    movie_details = get_movie_details(url)
    details, options, dict = format_movie_details(movie_details)
    print(options)
    
    click.secho(details, fg="blue")
    selection = inquirer.select(
        message="Select an option:",
        default=options[0],
        choices=options,
        pointer='=>',
        instruction='Use arrow keys to navigate and Enter to select.',
    ).execute()
    url = dict[selection]
    filename = download_torrent(url)
    



if __name__=='__main__':
    search()