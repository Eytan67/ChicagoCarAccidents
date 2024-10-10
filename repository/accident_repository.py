from repository.base_repository import BaseRepository


class AccidentRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)