from domain.models.dependency_injections import DependencyInjections
from domain.services.database.providers.database_executor_provider import DatabaseExecutorProvider
from domain.usecases.database import CreateDatabase


def create_database_controller(dependency_injections: DependencyInjections) -> DatabaseExecutorProvider:
    create_database = CreateDatabase(
        dependency_injections.database_factory
    )

    database_executor_provider =  create_database.call()
    breakpoint()
    return database_executor_provider