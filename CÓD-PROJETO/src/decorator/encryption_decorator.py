from decorator.report_decorator import ReportDecorator

class EncryptionDecorator(ReportDecorator):
    def generate(self) -> str:
        return f"🔒 {self._report.generate()} [Conteúdo criptografado]"