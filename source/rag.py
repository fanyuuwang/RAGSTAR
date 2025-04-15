import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class ICRALM(torch.nn.Module):
    def __init__(self, labels=None):
        super(ICRALM, self).__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Load model & tokenizer
        model_name = "meta-llama/Llama-3.1-8B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.model.eval()
        self.labels = labels
    def get_context(self):
        with open("/home/xiaoxikang/fanyu/req/dataset/final_text.txt") as f:
            final_text = f.read()
            final_text.split("\n")
        return final_text

    @torch.inference_mode()
    def evaluate_query_with_docs(self, query: str, docs: list, topk: int = 1):
        doc_logprobs = []

        for doc_id, doc_text in enumerate(docs):
            doc_text = "\n".join(doc_text)
            query_text = "\n".join(query)
            doc_enc = self.tokenizer.encode(doc_text, truncation=True)
            query_enc = self.tokenizer.encode(query_text, add_special_tokens=False)
            input_ids = doc_enc + query_enc
            input_ids_tensor = torch.tensor([input_ids], device=self.device)
            labels = [-100] * len(doc_enc) + query_enc
            labels_tensor = torch.tensor([labels], device=self.device)

            out = self.model(input_ids_tensor, labels=labels_tensor)
            num_query_tokens = len(query_enc)
            neg_log_likelihood = out.loss.item() * num_query_tokens
            doc_logprobs.append(neg_log_likelihood)

            # Delete tensors to free up memory
            del input_ids_tensor, labels_tensor, out
            torch.cuda.empty_cache()

        sorted_pairs = sorted(zip(doc_logprobs, docs))
        sorted_docs = [doc for _, doc in sorted_pairs]
        return sorted_docs[:topk]

    def evaluate_query_with_context(self, query: str, topk: int = 1):
        doc_logprobs = []
        docs = self.get_context()

        for doc_id, doc_text in enumerate(docs):
            doc_text = "\n".join(doc_text)
            query_text = "\n".join(query)
            doc_enc = self.tokenizer.encode(doc_text, truncation=True)
            query_enc = self.tokenizer.encode(query_text, add_special_tokens=False)
            input_ids = doc_enc + query_enc
            input_ids_tensor = torch.tensor([input_ids], device=self.device)
            labels = [-100] * len(doc_enc) + query_enc
            labels_tensor = torch.tensor([labels], device=self.device)

            out = self.model(input_ids_tensor, labels=labels_tensor)
            num_query_tokens = len(query_enc)
            neg_log_likelihood = out.loss.item() * num_query_tokens
            doc_logprobs.append(neg_log_likelihood)

            # Delete tensors to free up memory
            del input_ids_tensor, labels_tensor, out
            torch.cuda.empty_cache()

        ranking = sorted(zip(docs, doc_logprobs), key=lambda x: x[1])
        return [ranking[x][0] for x in range(topk)]

    def evaluate_rag(self,
            query: str,
            docs: list,
            topk: int,
    ):
        """
        Evaluate a list of queries with each query having its own list of retrieved docs.
        Returns a list of results (one per query).
        """
        res = self.evaluate_query_with_docs(
            query=query,
            docs=docs,
            topk=topk,
        )
        return res

    def do_rag(self, text, docs, topk=3):
        combined_text = f"""{text}"""
        query_results = self.evaluate_rag(combined_text, docs, topk=topk)
        return query_results


def initiate_RAG(labels=None):
    model = ICRALM(labels)
    return model