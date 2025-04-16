from typing import List
from chromadb import Client
from chromadb.config import Settings
from ollama import Client as OllamaClient

class RAGSystem:
    def __init__(self):
        self.chroma_client = Client()  # 不加参数
        self.ollama_client = OllamaClient()
        self.collection = self.chroma_client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, documents: List[str], metadatas: List[dict] = None):
        """将文档添加到Chroma中"""
        ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )

    def search_similar(self, query: str, k: int = 3) -> List[dict]:
        """搜索与查询最相似的文档"""
        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )
        return results

    def ask_question(self, question: str) -> str:
        """使用Ollama生成回答"""
        # 首先搜索相关文档
        results = self.search_similar(question)
        
        # 准备上下文
        context = "\n".join(results["documents"][0])
        
        # 使用Ollama生成回答
        prompt = f"""
        你是一个智能助手。请根据以下上下文回答问题：
        
        上下文：
        {context}
        
        问题：{question}
        
        请给出详细且准确的回答。
        """
        
        response = self.ollama_client.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response["message"]["content"]

# 使用示例
def main():
    # 创建RAG系统实例
    rag = RAGSystem()
    
    # 添加文档
    documents = [
        "Python是一种高级编程语言，由Guido van Rossum在1991年发布。",
        "Python的设计哲学是代码的可读性和简洁的语法。",
        "Python支持多种编程范式，包括面向对象、命令式、函数式和过程式编程。"
    ]
    
    rag.add_documents(documents)
    
    # 提问
    question = "Python的设计哲学是什么？"
    answer = rag.ask_question(question)
    print(f"问题：{question}")
    print(f"回答：{answer}")

if __name__ == "__main__":
    main()