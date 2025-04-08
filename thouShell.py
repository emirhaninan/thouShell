import ast
import astor
import random

#main dictionary
SHAKESPEAREAN_DICT = {
    "def": "def doth",
    "return": "returneth",
    "if": "if 'tis so that",
    "else": "else, alas",
    "print": "proclaim",
    "True": "True, by the stars",
    "False": "False, a pox upon it",
}

def shakepearean_comment():
    return random.choice([
        "\"Verily, this function doth performeth its duty.\"",
        "\"By the grace of the Bard, herein lies logic.\"",
        "\"Hark! A noble computation!\""
    ])

def transform_code(input_code: str) -> str:
    tree = ast.parse(input_code)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            node.name = f"shakespearize_{node.name}"
            node.body.insert(0, ast.Expr(ast.Str(shakepearean_comment())))
    
    transformed_code = astor.to_source(tree)
    
    for modern, shakespearean in SHAKESPEAREAN_DICT.items():
        transformed_code = transformed_code.replace(modern, shakespearean)
    
    return transformed_code

if __name__ == "__main__":
    sample_code = """
def add_numbers(a, b):
    if a > b:
        return a
    else:
        return b
    """
    print(transform_code(sample_code))