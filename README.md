### `README.md`

````markdown
# YTS Movie Torrent CLI

A command-line interface (CLI) tool to search and download movie torrents from YTS.mx using a guided, interactive terminal experience. It allows you to:

- Search for movies by name
- View detailed information including IMDb, Audience Score, and more
- Choose torrent quality and start downloads
- Control the torrent download process (pause, resume, stop)

## Features

- Interactive movie search using [InquirerPy](https://github.com/kazhala/InquirerPy)
- Torrent download and progress tracking with `torrentp`
- Integration with YTS movie database

## Installation

```bash
pip install .
````

## Usage

```bash
python -m moviecli "The Matrix"
```

You will be prompted to:

* Choose the correct movie
* Select the desired torrent quality
* Control the download with actions like pause, resume, stop

## Requirements

* Python 3.8+
* Dependencies listed in `setup.py`

## Dependencies

* `click`
* `InquirerPy`
* `torrentp`
* `beautifulsoup4`
* `requests`

## License

MIT License

````