from bridge.report import Report

class HTMLReport(Report):
    def generate(self) -> str:
        return "<html><body>Relatório gerado em HTML</body></html>"