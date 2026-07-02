# YouTube Network Topology Analysis

## Project Overview
This project analyzes the structure of the YouTube social network using graph theory. It empirically evaluates the topology of the real-world network and compares it against standard theoretical models:
- Erdos-Renyi (ER) Random Graph
- Barabasi-Albert (BA) Scale-Free Network
- Watts-Strogatz (WS) Small-World Network

The primary research objective is to determine whether the YouTube network exhibits scale-free or small-world properties, with a focus on understanding degree distributions, hub dominance, and overall structural robustness.




## Tools and Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-8A2BE2.svg?style=for-the-badge&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-314655?style=for-the-badge&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logoColor=white)


## Environment Setup (Reproducibility)
This project uses `uv` for lightning-fast dependency management and strict version locking.

```bash
# 1. Sync the environment (installs all dependencies exactly as locked in uv.lock)
uv sync

# 2. Launch Jupyter Notebook within the isolated environment
uv run jupyter notebook
```

## Dataset
- **Source:** Stanford Network Analysis Project (SNAP) - `com-youtube` dataset
- **Acquisition:** Direct HTTP Download (Stanford SNAP Official Server)
- **Format:** Tab-separated Edge List format (`.txt`) parsed as an undirected graph
- **Scale:**
  - Nodes: 1,134,890
  - Edges: 2,987,624
- **Context:** Nodes represent users, and edges represent mutual friendships between users.

## Analysis Pipeline & Key Insights
The project is structured sequentially across six Jupyter notebooks. Each step builds upon the previous one, transitioning from raw data processing to structural discovery:

1. **`01_data_load.ipynb`** (Data Provenance)
   - **Action:** Loads the dataset via local path or Kaggle API fallback.
   - **Result:** Secures and extracts the `com-youtube.ungraph.txt` edge list for reproducible analysis.

2. **`02_graph_construction.ipynb`** (Graph Definition Clarity)
   - **Action:** Constructs the undirected NetworkX graph object.
   - **Result:** Confirms the massive scale of 1,134,890 nodes and 2,987,624 edges, exporting a reusable `load_youtube_graph()` utility.

3. **`03_exploratory_analysis.ipynb`** (Empirical Properties)
   - **Action:** Computes baseline metrics using approximation techniques (random sampling) for computational feasibility.
   - **Insight:** Reveals a highly right-skewed degree distribution (plotted on a log-log scale) where the vast majority of users have very few connections, while a tiny fraction of "mega-hubs" possess tens of thousands of friends.

4. **`04_model_comparison_ER_BA_WS.ipynb`** (Deviation Detection)
   - **Action:** Benchmarks the empirical network against scaled theoretical null models (ER, BA, WS).
   - **Insight:** The empirical degree distribution almost perfectly mirrors the Barabasi-Albert (BA) scale-free model. However, an unexpected structural deviation emerges: the real network's clustering coefficient is significantly higher than what pure preferential attachment (BA) predicts.

5. **`05_research_question_analysis.ipynb`** (Mechanism Interpretation)
   - **Action:** Investigates the root cause of the clustering deviation through data-driven hypothesis testing.
   - **Insight:** Identifies that the top 1% of hubs control a massive percentage of all network traffic. The deviation from the pure BA model is analytically attributed to algorithmic influence (triadic closure via recommendations) and user homophily (tightly-knit communities). This hybrid structure grants the network high robustness to random failures but extreme structural sensitivity to targeted attacks.

6. **`06_visualization_report_assets.ipynb`** (Report Asset Generation)
   - **Action:** Generates clean, publication-ready figures for the final written report.
   - **Result:** Produces a comparative bar chart that visually highlights and proves the clustering coefficient deviation discussed in Notebook 05.
