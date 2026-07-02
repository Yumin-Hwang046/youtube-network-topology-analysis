import networkx as nx
import os

def load_youtube_graph(filepath="../data/raw/com-youtube.ungraph.txt"):
    """
    Loads the YouTube graph from the standard data directory.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}. Please run 01_data_load.ipynb first.")

    print(f"Loading graph from {filepath}...")
    G = nx.read_edgelist(
        filepath,
        comments="#",
        create_using=nx.Graph(),
        nodetype=int
    )
    return G
