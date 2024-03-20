from domain.models import DependencyInjections
from domain.services.core.bridges import DependencyInjectionBridge
from domain.services.core.providers import EnvironmentVariablesProvider


class GetDependencyInjections:
    def __init__(
        self,
        environment_variables_provider: EnvironmentVariablesProvider,
        dependency_injection_bridge: DependencyInjectionBridge,
    ) -> None:
        self.environment_variables_provider = environment_variables_provider
        self.dependency_injection_bridge = dependency_injection_bridge

    def call(self) -> DependencyInjections:
        injections_payload = self.environment_variables_provider.get_injections_payload()
        
        database_factory = self.dependency_injection_bridge.get_database_factory_injection(
            injections_payload.database_factory
        )

        # user_repository = self.dependency_injection_bridge.get_user_repoitory_injection(
        #     injections_payload.user_repository
        # )

        return DependencyInjections(
            database_factory,
            # user_repository,
        )