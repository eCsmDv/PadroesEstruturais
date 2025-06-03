from decorator.report_decorator import ReportDecorator

class FooterDecorator(ReportDecorator):
    def generate(self) -> str:
        return f"{self._report.generate()} + Rodapé customizado"