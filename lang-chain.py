from langchain.embeddings import VertexAIEmbeddings
from langchain.document_loaders import GCSFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import MatchingEngine

# Define Text Embeddings model
embedding = VertexAIEmbeddings()

# Define Matching Engine as Vector Store
me = MatchingEngine.from_components(
    project_id=PROJECT_ID,
    region=ME_REGION,
    gcs_bucket_name=f'gs://{ME_BUCKET_NAME}',
    embedding=embedding,
    index_id=ME_INDEX_ID,
    endpoint_id=ME_INDEX_ENDPOINT_ID
)

# Define Cloud Storage file loader to read a document
loader = GCSFileLoader(project_name=PROJECT_ID,
    bucket=url.split("/")[2],
    blob='/'.join(url.split("/")[3:])
)

# Split document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
doc_splits = text_splitter.split_documents(document)

# Add embeddings of document chunks to Matching Engine
texts = [doc.page_content for doc in doc_splits]
me.add_texts(texts=texts)