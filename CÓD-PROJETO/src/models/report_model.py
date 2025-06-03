class ReportModel:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def get_info(self) -> str:
        return f"Relatório: {self.title}\nConteúdo: {self.content}"