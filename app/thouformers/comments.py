from .base import BaseTransformer
import ast
import random

class CommentTransformer(BaseTransformer):
    def visit_Expr(self, node):
        if isinstance(node.value, ast.Str):
            # Transform existing docstrings
            original = node.value.s
            if not original.startswith(('"', "'")) or not original.endswith(('"', "'")):
                return node
                
            transformed = self.transform_comment(original.strip('"\''))
            node.value.s = transformed
        return node
    
    def transform_comment(self, comment: str) -> str:
        """Transform regular comments into Shakespearean prose"""
        if not comment.strip():
            return comment
            
        templates = [
            "Verily, {}",
            "Hark! {}",
            "By mine honor, {}",
            "Thus sayeth the coder: {}",
            "In sooth, {}",
            "Mark well: {}",
            "Prithee note: {}",
            "As the stars decree: {}"
        ]
        
        return random.choice(templates).format(comment)