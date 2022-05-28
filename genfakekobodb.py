import sqlite3

from faker import Faker

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

conn = sqlite3.connect("KoboReader.sqlite")

cur = conn.cursor()

cur.execute(CONTENT_SCHEMA)
cur.execute(BOOKMARK_SCHEMA)

conn.commit()

conn.close()

