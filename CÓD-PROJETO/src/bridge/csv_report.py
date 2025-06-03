from bridge.report import Report

class CSVReport(Report):
    def generate(self) -> str:
        return "Relatório gerado em CSV, formatado como tabela separada por vírgulas."