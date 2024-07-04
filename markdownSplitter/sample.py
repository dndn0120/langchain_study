from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)
from langchain.text_splitter import HTMLHeaderTextSplitter

with open('/Users/jinwook/Documents/langchain/quick_start/markdownSplitter/llm_example_text.txt') as f:
    llm_example_text = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 3,
    length_function = len,
    add_start_index = True,
)

texts = text_splitter.create_documents([llm_example_text])


html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)

