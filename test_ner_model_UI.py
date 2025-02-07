import gradio as gr
import spacy
import os

MODEL_DIR = "model/ner_copyright_model"
nlp = spacy.load(MODEL_DIR)
file_types = [
    # General Text & Markup
    ".md",
    # ".txt", ".md", ".html", ".htm", ".xml", ".json", ".yaml", ".yml", ".toml", ".csv", ".ini", ".cfg",

    # Python
    ".py", ".pyw",

    # JavaScript & Web
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",

    # Java
    ".java", ".jar",

    # C, C++, C#
    ".c", ".h", ".cpp", ".hpp", ".cc", ".hh", ".cs",

    # Go
    ".go",

    # Rust
    ".rs",

    # Swift
    ".swift",

    # Kotlin
    ".kt", ".kts",

    # PHP
    ".php", ".phtml", ".php3", ".php4", ".php5", ".phps", ".phpt",

    # Ruby
    ".rb", ".erb", ".rhtml",

    # Perl
    ".pl", ".pm", ".t",

    # Shell Scripting
    ".sh", ".bash", ".zsh", ".fish", ".bat", ".cmd", ".ps1",

    # Lua
    ".lua",

    # R
    ".r", ".R", ".Rmd",

    # SQL & Database
    ".sql", ".psql", ".db", ".sqlite", ".db3",

    # Dart
    ".dart",

    # Julia
    ".jl",

    # Scala
    ".scala", ".sc",

    # Haskell
    ".hs", ".lhs",

    # Lisp & Scheme
    ".lisp", ".lsp", ".cl", ".rkt", ".scm",

    # F#
    ".fs", ".fsi", ".fsx",

    # MATLAB
    ".m",

    # Objective-C
    ".m", ".mm",

    # Pascal
    ".pas", ".pp",

    # Assembly
    ".asm", ".s", ".a51", ".inc",

    # Verilog & VHDL
    ".v", ".vh", ".sv", ".svh", ".vhd", ".vhdl",

    # Fortran
    ".f", ".f90", ".f95", ".f03", ".f08",

    # COBOL
    ".cbl", ".cob", ".cpy",

    # Prolog
    ".pl", ".pro",

    # OpenCL & CUDA
    ".cl", ".cu", ".cuh",

    # Configurations & Scripting
    ".conf", ".rc", ".bashrc", ".zshrc", ".vimrc", ".tmux.conf",

    # Docker & Kubernetes
    ".dockerfile", "Dockerfile", ".yaml", ".yml",

    # Makefiles & Build Scripts
    "Makefile", ".mk", ".gradle", ".maven", ".ninja", ".bazel", "BUILD", "WORKSPACE",

    # Others
    ".ipynb"  # Jupyter Notebook
]

def extract_entities_from_folder(files):
    results = {}
    
    for single_file in files:
        file_name=os.path.basename(single_file)
        if os.path.isfile(single_file):
            _,ext = os.path.splitext(file_name)
            if ext in file_types:
                with open(single_file, "r", encoding="utf-8") as file:
                    text = file.read()
                    doc = nlp(text)
                    print(f"✅ Detected entities for {file_name}:")
                    for ent in doc.ents:
                        print(f"{ent.text} ({ent.label_})")
                    entities = [(ent.text, ent.label_) for ent in doc.ents]
                    results[file_name] = entities
           
    return results

def process_files(files):
    # print(files)
    # folder_path = os.path.dirname(files[0].name)
    # print(folder_path)
    # print(os.listdir(folder_path))
    return extract_entities_from_folder(files)

interface = gr.Interface(
    fn=process_files,
    inputs=gr.File(file_types=file_types,file_count="directory"),
    outputs=gr.JSON(),
    title="NER Copyright Detector",
    description="Upload a folder containing text files, and the model will detect copyright-related entities."
)

if __name__ == "__main__":
    interface.launch()
