from pdf2markdown4llm import PDF2Markdown4LLM

# Initialize converter
converter = PDF2Markdown4LLM(remove_headers=False, table_header="### Table")

# Convert PDF to Markdown
markdown_content = converter.convert("input.pdf")

# Save to file
with open("output.md", "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)