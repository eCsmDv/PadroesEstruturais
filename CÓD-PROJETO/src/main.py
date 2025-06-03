from bridge.pdf_report import PDFReport
from bridge.csv_report import CSVReport
from bridge.json_report import JSONReport
from decorator.header_decorator import HeaderDecorator
from decorator.timestamp_decorator import TimestampDecorator
from decorator.encryption_decorator import EncryptionDecorator
from utils.file_export import FileExport

# Escolher o relatório
report = JSONReport()  # Trocar para PDFReport, CSVReport, etc.

# Aplicar decoradores
decorated_report = HeaderDecorator(TimestampDecorator(EncryptionDecorator(report)))

# Gerar o relatório
final_report = decorated_report.generate()
print(final_report)

# Salvar no arquivo
print(FileExport.save_to_file("relatorio.txt", final_report))