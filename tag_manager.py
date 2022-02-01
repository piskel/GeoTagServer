from tinydb import TinyDB

from geotag import GeoTag

class TagManager:

    # Initializes the database and loads saves access to
    # the "geotags" table.
    def __init__(self) -> None:
        self.db = TinyDB('db.json')
        self.geotags_table = self.db.table('geotags')

    # Resets the entire database
    def reset_db(self) -> None:
        self.db.drop_tables()

    # Adds a new tag to the database
    def add_tag(self, tag: GeoTag) -> None:
        self.geotags_table.insert(tag.__dict__)

    # Returns every entry in the geotags table
    def get_all_tags(self) -> list:
        return self.geotags_table.all()
    

    

