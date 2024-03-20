from domain.services.database.providers import DatabaseExecutorProvider


class DatabaseFactory:
    def call(self) -> DatabaseExecutorProvider:
        raise NotImplementedError()