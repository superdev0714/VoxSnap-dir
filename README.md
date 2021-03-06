# Voice apps directory

## Installation

From project root in a virtualenv or similar:

```sh
pip install -e .
```

### Developer dependencies

Useful for VS Code and other IDEs.

```sh
pip install mypy flake8 pylint rope django-stubs pylint-django pep257 pyflakes
```

## Django app

Main app is in the `vad` directory.

The Django project is in the `voxsnapvad` directory.

## Scraper

### Alexa skills

From project root:

```sh
scrapy crawl amazon_alexa_skills
```

Code for this scraper is in `scraping/alexa.py`. Settings are in `scraping/scrapy_settings.py`.

### Google Assistant actions

```sh
python scraping/google_assistant.py
```

You must pass a cookies.txt file that contains `.google.com` cookies HSID, SID, and SSID if you want to scrape reviews:

```sh
python scraping/google_assistant.py cookies.txt
```

Run with PDB:

```sh
python -m pdb -c 'continue' scraping/google_assistant.py cookies.txt
```
