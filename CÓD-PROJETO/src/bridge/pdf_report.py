from bridge.report import Report

class PDFReport(Report):
    def generate(self) -> str:
        return "Relatório gerado em PDF"