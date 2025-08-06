from langchain.text_splitter import CharacterTextSplitter

text = """
Document splitting is often a crucial preprocessing step for many applications. It involves breaking down large texts into smaller, manageable chunks. This process offers several benefits, such as ensuring consistent processing of varying document lengths, overcoming input size limitations of models, and improving the quality of text representations used in retrieval systems. There are several strategies for splitting documents, each with its own advantages.
"""

splitter = CharacterTextSplitter(
    chunk_size= 100,
    chunk_overlap= 0,
    separator=''
)

result = splitter.split_text(text)

print(result)

