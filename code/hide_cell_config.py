# hide_code_config.py
from nbconvert.preprocessors import Preprocessor
from nbconvert import HTMLExporter
import nbformat


class HideCodePreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, cell_index):
        if "hide" in cell.metadata.get("tags", []):
            cell.source = ""
        return cell, resources


def custom_nbconvert(notebook_path, output_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    html_exporter.register_preprocessor(HideCodePreprocessor, enabled=True)

    (body, resources) = html_exporter.from_notebook_node(nb)

    with open(output_path, "w") as f:
        f.write(body)


custom_nbconvert("model.ipynb", "model.html")
