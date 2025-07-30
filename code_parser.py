# code_parser.py

import ast
import inspect

class CodeParser:
    """
    Parses a Python file to extract top-level functions and classes using AST.
    """
    def __init__(self, file_path: str):
        """
        Initializes the parser with the path to the Python file.

        Args:
            file_path (str): The path to the .py file to be parsed.
        """
        self.file_path = file_path
        # Specify UTF-8 encoding to prevent errors on Windows
        with open(file_path, 'r', encoding='utf-8') as source_file:
            self.source_code = source_file.read()
        self.tree = ast.parse(self.source_code)

    def get_code_elements(self):
        """
        Extracts all top-level functions and classes from the parsed file.

        Returns:
            list: A list of dictionaries, where each dictionary represents a
                  function or class and contains its type and source code.
        """
        elements = []
        for node in self.tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                element_type = 'function' if isinstance(node, ast.FunctionDef) else 'class'
                
                # Use inspect.getsource to get the full source including decorators
                try:
                    # To use inspect.getsource, we need to compile and exec the AST
                    # This is a safe way to get the source of nodes from an AST
                    # We create a temporary module to execute the code in.
                    temp_module = {}
                    code_obj = compile(self.tree, filename="<ast>", mode="exec")
                    exec(code_obj, temp_module)
                    
                    obj = temp_module.get(node.name)
                    if obj:
                        source_snippet = inspect.getsource(obj)
                    else: # Fallback for any edge cases
                        source_snippet = ast.get_source_segment(self.source_code, node)

                except Exception:
                    # Fallback to ast.get_source_segment if inspect fails
                    source_snippet = ast.get_source_segment(self.source_code, node)

                elements.append({
                    'type': element_type,
                    'name': node.name,
                    'source': source_snippet
                })
        return elements
