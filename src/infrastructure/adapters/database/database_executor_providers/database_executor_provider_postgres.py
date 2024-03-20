from domain.services.database.providers.database_executor_provider import DatabaseExecutorProvider
import psycopg

class DatabaseExecutorProviderPostgres(DatabaseExecutorProvider):
    def __init__(self, connection: psycopg.Connection, cursor: psycopg.Cursor):
        self.connection = connection
        self.cursor = cursor

    def execute(
        self,
        query: str,
        parameter: tuple[str]=None,
        is_select=True,
    ) -> list[list[str]]:
        self.cursor.execute(query, parameter)
        
        if is_select:
            return self.cursor.fetchall()
        
        self.connection.commit()
        self.connection.close()
        return []