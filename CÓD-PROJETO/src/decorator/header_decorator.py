from decorator.report_decorator import ReportDecorator

class HeaderDecorator(ReportDecorator):
    def generate(self) -> str:
        return "Cabeçalho do Relatório\n" + self._report.generate()