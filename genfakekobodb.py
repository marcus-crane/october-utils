import os
import random
import sqlite3

from faker import Faker

fake = Faker()

CONTENT_SCHEMA = '''
CREATE TABLE content
(ContentID Text NOT NULL,
ContentType TEXT NOT NULL,
Title Text COLLATE NOCASE,
Attribution TEXT COLLATE NOCASE,
___PercentRead INTEGER,
VolumeIndex INTEGER)
'''

BOOKMARK_SCHEMA = '''
CREATE TABLE Bookmark
(BookmarkID TEXT NOT NULL,
VolumeID NOT NULL,
ContentID TEXT NOT NULL,
Text TEXT,
Annotation TEXT,
ChapterProgress REAL NOT NULL DEFAULT 0,
DateCreated TEXT)
'''

if os.path.exists("KoboReader.sqlite"):
    os.remove("KoboReader.sqlite")
conn = sqlite3.connect("KoboReader.sqlite")

cur = conn.cursor()

cur.execute(CONTENT_SCHEMA)
cur.execute(BOOKMARK_SCHEMA)

conn.commit()

CONTENT = []
BOOKMARKS = []

VOLUME_INDEX = -1
CONTENT_TYPE = 6

GEN_NUM_BOOKS = 50
GEN_NUM_BOOKMARKS_PER_BOOK = 30

def gen_title():
    title = fake.catch_phrase()
    subtitle = fake.sentence(nb_words=15, variable_nb_words=True).replace('.', '')
    return f"{title}: {subtitle}"

def gen_volume_id(book):
    title = book[2]
    author = book[3]
    author_bits = book[3].split(' ')
    author_bits.reverse()
    author_reversed = ', '.join(author_bits)
    return "file:///mnt/onboard/{0}/{1} - {2}.kepub.epub".format(author_reversed, title.replace(":", ""), author)

def gen_read_percent():
    return random.randint(0, 100)

for _ in range(GEN_NUM_BOOKS):
    book = (
        fake.uuid4(),
        CONTENT_TYPE,
        gen_title(),
        fake.name(),
        gen_read_percent(),
        VOLUME_INDEX,
    )
    CONTENT.append(book)

for book in CONTENT:
    for _ in range (GEN_NUM_BOOKMARKS_PER_BOOK):
        bookmark = (
            fake.uuid4(),
            gen_volume_id(book),
            book[0],
            fake.paragraph(nb_sentences=4, variable_nb_sentences=True),
            fake.paragraph(nb_sentences=1, variable_nb_sentences=True),
            32,
            "2021-04-24T05:07:29.943"
        )
        BOOKMARKS.append(bookmark)

cur.executemany("INSERT INTO Content VALUES (?, ?, ?, ?, ?, ?)", CONTENT)
conn.commit()

cur.executemany("INSERT INTO Bookmark VALUES (?, ?, ?, ? ,?, ? ,?)", BOOKMARKS)
conn.commit()

conn.close()

