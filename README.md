# october-utils

Some bits and pieces that make it easier to load test [October](https://github.com/marcus-crane/october), my open-source Kobo-to-Readwise sync tool.

`genfakekobodb.py` is intended to generate a base-minimum `KoboReader.sqlite` that October is able to parse, prepopulated with "books" and "highlights". Really, it just uses faker to populate the `content` and `Bookmark` tables.

Most of the tables and indexes you would find on a normal `KoboReader.sqlite` are missing but October doesn't query most of them.