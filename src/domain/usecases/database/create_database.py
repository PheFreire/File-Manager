from domain.services.database.factories import DatabaseFactory
from domain.services.database.providers import DatabaseExecutorProvider


class CreateDatabase:
    def __init__(self, database_factory: DatabaseFactory):
        self.database_factory = database_factory

    def call(self) -> DatabaseExecutorProvider:
        return self.database_factory.call()