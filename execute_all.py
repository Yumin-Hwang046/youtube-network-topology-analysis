import subprocess
import sys

notebooks = [
    "notebooks/01_data_load.ipynb",
    "notebooks/02_graph_construction.ipynb",
    "notebooks/03_exploratory_analysis.ipynb",
    "notebooks/04_model_comparison_ER_BA_WS.ipynb",
    "notebooks/05_research_question_analysis.ipynb",
    "notebooks/06_visualization_report_assets.ipynb"
]

print("Installing kernel...")
subprocess.run(["python", "-m", "uv", "run", "python", "-m", "ipykernel", "install", "--user", "--name=youtube-env"], check=True)

for nb in notebooks:
    print(f"Executing {nb}...")
    try:
        result = subprocess.run(
            ["python", "-m", "uv", "run", "jupyter", "nbconvert", "--execute", "--inplace", 
             "--ExecutePreprocessor.timeout=-1", "--ExecutePreprocessor.kernel_name=youtube-env", nb],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Success: {nb}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {nb}:")
        print(e.stderr)
        sys.exit(1)

print("All notebooks executed successfully.")
