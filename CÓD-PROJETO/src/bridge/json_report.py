import json
from bridge.report import Report

class JSONReport(Report):
    def generate(self) -> str:
        data = {"title": "Relatório JSON", "content": "Dados estruturados"}
        return json.dumps(data, indent=4)