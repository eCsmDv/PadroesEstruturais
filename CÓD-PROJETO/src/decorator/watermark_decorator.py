from decorator.report_decorator import ReportDecorator

class WatermarkDecorator(ReportDecorator):
    def generate(self) -> str:
        return f"{self._report.generate()} + Marca d'água adicionada"