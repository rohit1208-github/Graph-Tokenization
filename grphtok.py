import networkx as nx
import spacy
from sklearn.metrics.pairwise import cosine_similarity

graph = nx.Graph()

sentence = "A quick brown fox jumps over the lazy dog"
words = sentence.split()

for i in range(len(words) - 1):
    graph.add_edge(words[i], words[i + 1])

nlp = spacy.load('en_core_web_sm')

new_sentence = "Colorful blossoms flourish during springtime"
doc = nlp(new_sentence)

for token in doc:
    for child in token.children:
        graph.add_edge(token.text, child.text)

for word1 in embeddings:
    for word2 in embeddings:
        if word1 != word2:
            similarity = cosine_similarity([embeddings[word1]], [embeddings[word2]])[0][0]
            if similarity > 0.8:
                graph.add_edge(word1, word2)

# Detect communities in the graph using the greedy modularity algorithm
communities = community.greedy_modularity_communities(graph)

for comm in communities:
    merged_token = ' '.join(comm)
    print("Merged token from community:", merged_token)
