"""
Gera o PDF do relatório a partir do arquivo Markdown.

Uso (a partir da raiz do projeto, com o .venv ativado):
    python docs/gerar_pdf.py
"""

import os
import sys
import markdown
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(ROOT, "docs", "relatorio_students_performance.md")
PDF_PATH = os.path.join(ROOT, "docs", "relatorio_students_performance.pdf")

CSS = """
body{font-family:Arial,sans-serif;font-size:11pt;line-height:1.6;color:#1a1a1a}
@page{size:A4;margin:2cm 2.5cm;@bottom-center{content:counter(page) " / " counter(pages);font-size:9pt;color:#666}}
h1{font-size:18pt;color:#1a3a5c;border-bottom:3px solid #e67e22;padding-bottom:6px;margin-top:28px}
h2{font-size:14pt;color:#1a3a5c;border-bottom:1px solid #ccc;padding-bottom:3px;margin-top:20px}
h3{font-size:12pt;color:#2c3e50;margin-top:16px}
h4{font-size:11pt;color:#34495e;margin-top:12px}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:9.5pt}
th{background:#2c3e50;color:#fff;padding:7px 9px;text-align:left}
td{padding:5px 9px;border-bottom:1px solid #ddd}
tr:nth-child(even) td{background:#f8f9fa}
code{background:#f4f4f4;padding:1px 4px;border-radius:3px;font-size:9pt;color:#c0392b}
pre{background:#2b2b2b;color:#f8f8f2;padding:12px;border-radius:5px;font-size:8.5pt;line-height:1.4;page-break-inside:avoid}
pre code{background:none;color:#f8f8f2;padding:0}
blockquote{border-left:4px solid #e67e22;background:#fef9f0;margin:12px 0;padding:8px 14px;font-style:italic;color:#555}
ul,ol{padding-left:22px;margin:6px 0}li{margin:3px 0}
hr{border:none;border-top:2px solid #ecf0f1;margin:18px 0}
p{margin:7px 0}
"""


def main():
    with open(MD_PATH, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

    html_full = (
        '<!DOCTYPE html><html lang="pt-BR"><head>'
        '<meta charset="utf-8">'
        f"<style>{CSS}</style>"
        "</head><body>"
        + html_body
        + "</body></html>"
    )

    HTML(string=html_full, base_url=ROOT).write_pdf(PDF_PATH)
    size_kb = os.path.getsize(PDF_PATH) / 1024
    print(f"PDF gerado: {PDF_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
