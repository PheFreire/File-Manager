from dataclasses import dataclass
from domain.services.database.factories import DatabaseFactory

@dataclass
class DependencyInjections:
    database_factory: DatabaseFactory
    # user_repository: UserRepository
