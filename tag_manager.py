from tinydb import TinyDB

from geotag import GeoTag

class TagManager:

    def __init__(self) -> None:
        self.db = TinyDB('db.json')
        self.geotag_table = self.db.table('geotags')

    def reset_db(self) -> None:
        self.db.drop_tables()


    def add_tag(self, tag: GeoTag) -> None:
        self.geotag_table.insert(tag.__dict__)
        
    
    def get_all_tags(self) -> list:
        return self.geotag_table.all()
    

    

