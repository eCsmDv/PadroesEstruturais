import datetime
from decorator.report_decorator import ReportDecorator

class TimestampDecorator(ReportDecorator):
    def generate(self) -> str:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{self._report.generate()}\nGerado em: {timestamp}"