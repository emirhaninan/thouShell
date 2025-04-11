from .base import BaseTransformer
import ast
import random

class ControlFlowTransformer(BaseTransformer):
    def visit_If(self, node):
        # Add dramatic conditional comments
        test_comment = random.choice([
            "Put to the test",
            "Upon examination",
            "When scrutinized",
            "If proven true"
        ])
        
        new_test_comment = ast.Expr(ast.Str(test_comment))
        node.body.insert(0, new_test_comment)
        
        if node.orelse:
            else_comment = ast.Expr(ast.Str("Else, despair!"))
            node.orelse.insert(0, else_comment)
        
        self.generic_visit(node)
        return node
    
    def visit_For(self, node):
        # Add loop commentary
        loop_comment = random.choice([
            "Again and again I iterate",
            "With steadfast repetition",
            "In ceaseless cycles",
            "Round and round we go"
        ])
        
        new_loop_comment = ast.Expr(ast.Str(loop_comment))
        node.body.insert(0, new_loop_comment)
        
        self.context.in_loop = True
        self.generic_visit(node)
        self.context.in_loop = False
        
        return node
    
    def visit_While(self, node):
        # While loop transformation
        while_comment = random.choice([
            "Whilst the condition holds",
            "So long as it remains true",
            "Until proven false",
            "Persisting while possible"
        ])
        
        new_while_comment = ast.Expr(ast.Str(while_comment))
        node.body.insert(0, new_while_comment)
        
        self.context.in_loop = True
        self.generic_visit(node)
        self.context.in_loop = False
        
        return node