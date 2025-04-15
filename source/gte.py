from sentence_transformers import SentenceTransformer
from torch import nn
import torch


class GTE(nn.Module):
    def __init__(self, max_length=512):
        super(GTE, self).__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = SentenceTransformer("Alibaba-NLP/gte-multilingual-base", trust_remote_code=True).to(self.device)

    def do_embedding(self, input_text_list):
        embeddings = self.model.encode(input_text_list, normalize_embeddings=True, convert_to_tensor=True)

        return embeddings

    def do_score(self, emb1, emb2):
        emb1 = emb1.to(self.device)
        emb2 = emb2.to(self.device)
        scores = self.model.similarity(emb1, emb2)

        return scores.tolist()

