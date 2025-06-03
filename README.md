# PadroesEstruturais
Padrões Estruturais

Construção Incremental de uma Solução com Padrões de Projeto aplicando Decorator e Bridge para garantir flexibilidade e reutilização.

📌 Construção Incremental de uma Solução com Padrões de Projeto
Projeto: Sistema de Geração de Relatórios
Autor: Eduardo
Data: 12/06/25
Objetivo: Implementação dos padrões estruturais Bridge e Decorator para garantir flexibilidade, reutilização e expansão de um sistema de geração de relatórios

🔷 1. Introdução
Este projeto apresenta uma abordagem modular para a geração e personalização de relatórios, utilizando os padrões Bridge e Decorator. Com isso, garantimos: ✅ Flexibilidade na escolha do formato de relatório (PDF, HTML, CSV, JSON).
✅ Extensibilidade na adição de funcionalidades sem modificar código original.
✅ Reutilização de componentes estruturais para facilitar futuras expansões.


🏗 2. Arquitetura do Sistema
A organização do projeto segue uma estrutura clara e modular:

src/
│── bridge/         # Implementação do padrão Bridge
│── decorator/      # Implementação do padrão Decorator
│── models/         # Modelos de relatórios
│── utils/          # Funções auxiliares (exportação)
│── main.py         # Arquivo principal

🖇 Bridge – Separação entre Abstração e Implementação
O padrão Bridge foi aplicado para permitir múltiplas formas de gerar relatórios:
- Report (Abstração): Define a interface dos relatórios.
- PDFReport, HTMLReport, CSVReport, JSONReport: Implementações separadas.
✨ Decorator – Incremento de Funcionalidades
O padrão Decorator foi utilizado para incrementar relatórios dinamicamente:
- HeaderDecorator: Adiciona cabeçalho ao relatório.
- TimestampDecorator: Insere data e hora.
- EncryptionDecorator: Criptografa o conteúdo antes da exportação.

🔍 3. Implementação e Código
Abaixo, um exemplo da aplicação dos padrões Bridge e Decorator:

🏗 Exemplo de implementação do Bridge

class Report(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass

class PDFReport(Report):
    def generate(self) -> str:
        return "Relatório gerado em PDF"


✨ Exemplo de uso do Decorator
class HeaderDecorator(ReportDecorator):
    def generate(self) -> str:
        return "Cabeçalho do Relatório\n" + self._report.generate()



📂 4. Exportação de Arquivos
Para garantir maior utilidade, o sistema permite salvar relatórios em arquivos .txt, utilizando o módulo utils/file_export.py:

class FileExport:
    @staticmethod
    def save_to_file(filename: str, content: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return f"Arquivo salvo como {filename}"


🚀 5. Testes e Execução
O sistema foi testado para validar: ✔ Geração correta dos relatórios.
✔ Aplicação de decoradores sem alterar a estrutura original.
✔ Exportação de arquivos sem perda de conteúdo.
Execução
Para rodar o projeto:

CÓD-PROJETO src/
python main.py


🎯 6. Conclusão
Este projeto demonstra como os padrões Bridge e Decorator podem ser combinados para criar um sistema modular, expansível e reutilizável. Com essa abordagem, podemos facilmente adicionar novos formatos de relatório e incrementar funcionalidades sem impactar o código base.
Se precisar de mais refinamentos na documentação, estou aqui para ajudar! 🔥😃🚀
O que acha? Precisa de ajustes para a apresentação?

