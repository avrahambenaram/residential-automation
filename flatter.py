import ast
import pathlib

def flatten(file):
    seen = set()
    output = []

    def load(f):
        code = pathlib.Path(f).read_text()

        for line in code.splitlines():
            if line.startswith("import ") or line.startswith("from "):
                continue
            output.append(line)

    load(file)
    return "\n".join(output)

print(flatten("main.py"))