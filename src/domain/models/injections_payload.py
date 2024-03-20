from dataclasses import dataclass

@dataclass
class InjectionsPayload:
    database_factory: str
    # user_repository: str