# -*- coding: utf-8 -*-
"""BERT_embeddings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wHjPnNWQvY5f7ysF9hBJxhOg8ajJkPj1
"""

# !pip install transformers
# !pip install torch
!pip install sentence_transformers

from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import numpy as np 

model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

quotes_and_labels = [
  ('I adore ice cream', 1), 
  ('I hate ice cream', 0),
  ('I hate fucking london because of rain', 0),
  ('Jana is a dumbass', 0),
  ('I am beatiful', 1),
  ('hate hate hate you', 0),
  ('she is a very smart cute girl', 1),
  ('love love love love beautiful', 1),
  ('bad ugly smelly stupid', 0),
  ('stupid stupid bad worse the worst', 0),
  ('beautiful beautiful pretty very nice nice', 1)
  ]

quotes = [pair[0] for pair in quotes_and_labels]

embeddings = model.encode(quotes)
print(embeddings.shape)

out_features = 2
quote_num = embeddings.shape[0]
pca = PCA(n_components=out_features)

embeddings_pca = pca.fit_transform(embeddings)

import matplotlib.pyplot as plt

pos_embeddings_pca = []
neg_embeddings_pca = []

for ind, (quote, label) in enumerate(quotes_and_labels):
  if label == 1:
    pos_embeddings_pca.append(list(embeddings_pca[ind, :]))
  else:
    neg_embeddings_pca.append(list(embeddings_pca[ind, :]))

pos_embeddings_pca = np.array(pos_embeddings_pca)
neg_embeddings_pca = np.array(neg_embeddings_pca)

plt.figure(figsize=(10, 5))
plt.scatter(
    pos_embeddings_pca[:, 0], pos_embeddings_pca[:, 1], 
    marker='+', s=200, c='b'
    )
plt.scatter(
    neg_embeddings_pca[:, 0], neg_embeddings_pca[:, 1], 
    marker='_', s=200, c='r'
    )

plt.grid()

