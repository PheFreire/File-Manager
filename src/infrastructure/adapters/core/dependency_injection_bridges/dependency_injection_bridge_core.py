from domain.services.core.bridges.dependency_injection_bridge import DependencyInjectionBridge
from domain.services.database.factories import DatabaseFactory
from infrastructure.adapters.database.database_factories.database_factory_postgres import DatabaseFactoryPostgres


class DependencyInjectionBridgeCore(DependencyInjectionBridge):
    def __init__(self) -> None:
        self.adapters = {
            "database_factory_postgres": DatabaseFactoryPostgres
        }
    
    def get_database_factory_injection(self, injection_name: str) -> DatabaseFactory:
        return self.adapters[injection_name]()