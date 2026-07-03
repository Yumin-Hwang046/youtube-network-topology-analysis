import json
import base64
import os

os.makedirs("../results/figures", exist_ok=True)

# Define which notebooks to process and what to name their outputs
notebooks = [
    ("03_exploratory_analysis.ipynb", "degree_distribution.png"),
    ("04_model_comparison_ER_BA_WS.ipynb", "model_comparison.png")
]

for nb_file, out_name in notebooks:
    try:
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb_data = json.load(f)
        
        img_count = 0
        for cell in nb_data.get('cells', []):
            if cell.get('cell_type') == 'code':
                for output in cell.get('outputs', []):
                    if 'data' in output and 'image/png' in output['data']:
                        # some strings might have newlines in the json array, so we join them
                        img_b64_raw = output['data']['image/png']
                        if isinstance(img_b64_raw, list):
                            img_b64 = "".join(img_b64_raw)
                        else:
                            img_b64 = img_b64_raw
                            
                        img_data = base64.b64decode(img_b64)
                        
                        fname = out_name if img_count == 0 else f"{out_name.split('.')[0]}_{img_count}.png"
                        out_path = os.path.join("../results/figures", fname)
                        
                        with open(out_path, 'wb') as img_f:
                            img_f.write(img_data)
                        print(f"Extracted {out_path} from {nb_file}")
                        img_count += 1
    except Exception as e:
        print(f"Error processing {nb_file}: {e}")
