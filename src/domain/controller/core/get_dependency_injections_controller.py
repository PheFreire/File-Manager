from domain.models.dependency_injections import DependencyInjections
from domain.usecases.core.get_dependency_injections import GetDependencyInjections
from infrastructure.adapters.core.dependency_injection_bridges.dependency_injection_bridge_core import DependencyInjectionBridgeCore
from infrastructure.adapters.core.environment_variables_providers import EnvironmentVariablesProviderCore


def get_dependency_injections_controller() -> DependencyInjections:
    environment_variables_provider = EnvironmentVariablesProviderCore()
    dependency_injection_bridge = DependencyInjectionBridgeCore()
    
    get_dependency_injections = GetDependencyInjections(
        environment_variables_provider,
        dependency_injection_bridge,
    )

    return get_dependency_injections.call()