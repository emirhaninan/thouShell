from .base import BaseTransformer
import ast
import random

class FunctionTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.function_comments = [
            "Verily, this function doth perform its duty",
            "By mine honor, this procedure shall execute",
            "Hark! A noble function to serve thy needs",
            "With solemn vow, this code shall run",
            "Upon my word, this method shall not fail thee"
        ]
    
    def visit_FunctionDef(self, node):
        # Transform function name and parameters
        node.name = f"shakespearize_{node.name}"
        
        # Add Shakespearean docstring if none exists
        if not any(isinstance(n, ast.Expr) and isinstance(n.value, ast.Str) for n in node.body):
            docstring = ast.Expr(ast.Str(random.choice(self.function_comments)))
            node.body.insert(0, docstring)
        
        # Process function body
        self.context.in_function = True
        self.generic_visit(node)
        self.context.in_function = False
        
        return node
    
    def visit_Return(self, node):
        # Add flourish to return statements
        return_comment = random.choice([
            "Thus I returneth",
            "Herewith I yield",
            "With this I part",
            "Farewell, I give thee"
        ])
        
        if node.value:
            new_node = ast.Expr(ast.Str(return_comment))
            return ast.copy_location(ast.If(
                test=ast.NameConstant(value=True),
                body=[new_node, node],
                orelse=[]
            ), node)
        return node