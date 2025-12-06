import json
import sys

# Pass the notebook filename as an argument
# Example: python remove_widgets.py your_notebook.ipynb
if len(sys.argv) < 2:
    print("Usage: python remove_widgets.py <notebook_file.ipynb>")
    sys.exit(1)

notebook_file = sys.argv[1]
output_file = notebook_file.replace(".ipynb", "_no_widgets.ipynb")

# Load the notebook
with open(notebook_file, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Remove widget metadata from each cell
for cell in nb.get("cells", []):
    if "metadata" in cell and "widgets" in cell["metadata"]:
        del cell["metadata"]["widgets"]

# Remove top-level notebook widget metadata
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

# Save the cleaned notebook
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print(f"Widget metadata removed. Clean notebook saved as: {output_file}")
