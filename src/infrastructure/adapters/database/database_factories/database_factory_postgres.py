from domain.services.database.factories import DatabaseFactory
from domain.services.database.providers import DatabaseExecutorProvider

import os
import psycopg

from infrastructure.adapters.database.database_executor_providers import DatabaseExecutorProviderPostgres


class DatabaseFactoryPostgres(DatabaseFactory):
    def call(self) -> DatabaseExecutorProviderPostgres:
        connection_url = os.getenv("DATABASE_URL")
        connection = psycopg.connect(connection_url)
        cursor = connection.cursor()

        return DatabaseExecutorProviderPostgres(connection, cursor)
