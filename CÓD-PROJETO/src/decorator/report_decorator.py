from bridge.report import Report

class ReportDecorator(Report):
    def __init__(self, report: Report):
        self._report = report

    def generate(self) -> str:
        return self._report.generate()