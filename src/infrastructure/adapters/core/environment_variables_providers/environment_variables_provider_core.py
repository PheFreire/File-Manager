from domain.models.injections_payload import InjectionsPayload
from domain.services.core.providers.environment_variables_provider import EnvironmentVariablesProvider

import toml
import os

class EnvironmentVariablesProviderCore(EnvironmentVariablesProvider):
    def get_injections_payload(self) -> InjectionsPayload:
        injections_env_path = os.getenv("INJECTION_ENV")

        injections = toml.load(
            open(injections_env_path)
        )["injections"]

        return InjectionsPayload(injections["database_factory"])