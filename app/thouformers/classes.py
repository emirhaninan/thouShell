from .base import BaseTransformer
import ast
import random

class ClassTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.class_comments = [
            "A noble class of great import",
            "Behold, a regal collection of methods",
            "A courtly assembly of attributes and functions",
            "Here stands a proud and virtuous class",
            "A distinguished company of code"
        ]
    
    def visit_ClassDef(self, node):
        # Transform class name
        node.name = f"Noble{node.name}"
        
        # Add Shakespearean docstring if none exists
        if not any(isinstance(n, ast.Expr) and isinstance(n.value, ast.Str) for n in node.body):
            docstring = ast.Expr(ast.Str(random.choice(self.class_comments)))
            node.body.insert(0, docstring)
        
        # Process class body
        self.context.in_class = True
        self.generic_visit(node)
        self.context.in_class = False
        
        return node
    
    def visit_Attribute(self, node):
        # Transform attribute access
        if isinstance(node.attr, str):
            node.attr = f"thy_{node.attr}"
        return node