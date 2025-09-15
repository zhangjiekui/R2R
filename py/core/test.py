
from core.base.providers import EmbeddingConfig
from core.providers.embeddings.xinference import XinferenceEmbeddingProvider
import asyncio


emb = XinferenceEmbeddingProvider(
    config=EmbeddingConfig(
        provider="xinference",
        base_model="bce-embedding-base_v1",
        base_dimension=768,
        api_base="http://10.1.150.106:9997/v1",
        rerank_model="jina-reranker-v2",
        rerank_url="http://10.1.150.106:9997/v1/rerank",
    )
)

embedding = emb.get_embedding("hello world")
print(f"{len(embedding)=}")
async_embedding = asyncio.run(emb.async_get_embedding("hello world"))
print(f"{len(async_embedding)=}")
print("============================================================================")

from shared import ChunkSearchResult
import uuid
chunk_result1 = ChunkSearchResult(
    id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
    document_id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
    collection_ids=[uuid.UUID("00000000-0000-0000-0000-000000000000")],
    owner_id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
    text="hello java, returned chunk_result1",
    score=0.9,
    metadata={"text": "hello java, returned chunk_result1"},
)
chunk_result2 = ChunkSearchResult(
    id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
    document_id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
    collection_ids=[uuid.UUID("00000000-0000-0000-0000-000000000000")],
    owner_id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
    text="hello python, returned chunk_result2",
    score=0.5,
    metadata={"text": "hello python, returned chunk_result2"},
)
r = emb.rerank(
    query="hello python",
    results=[chunk_result1,chunk_result2]
)
print(f"{r=}")
async_r = asyncio.run(emb.arerank(
    query="hello java",
    results=[chunk_result1,chunk_result2]
))
print(f"{async_r=}")
