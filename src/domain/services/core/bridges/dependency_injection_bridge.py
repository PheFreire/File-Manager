from domain.services.database.factories import DatabaseFactory


class DependencyInjectionBridge:
    def get_database_factory_injection(self, injection_name: str) -> DatabaseFactory:
        raise NotImplementedError()