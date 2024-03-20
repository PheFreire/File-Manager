class DatabaseExecutorProvider:
    def execute(
        self, 
        query: str,
        parameter: tuple[str]=None,
        is_select=True,
    ) -> list[list[str]]:
        raise NotImplementedError()