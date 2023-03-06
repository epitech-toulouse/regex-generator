# Regex Generator

This is a simple regex generator who generate a regex from a gitignore based on
the [gitignore.io](https://www.gitignore.io) API.
It uses github-linguist to retrieve the list of languages.

## Usage

```bash
docker run -it --rm -v $PATH_TO_THE_REPO:/app/repo epitechtoulouse/regex-generator:latest
```

## Build

```bash
docker build -t epitechtoulouse/regex-generator:latest .
```

## Author
Lucas Mathieux ([@Madfish5415](https://github.com/Madfish5415))

