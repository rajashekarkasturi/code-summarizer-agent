# schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional

class Parameter(BaseModel):
    """Data model for a function parameter."""
    name: str = Field(description="The name of the parameter.")
    param_type: str = Field(description="The expected type of the parameter.")
    description: str = Field(description="A concise explanation of the parameter.")

class FunctionSummary(BaseModel):
    """Data model for the AI-generated summary of a function."""
    description: str = Field(description="A one-sentence explanation of what the function does.")
    parameters: List[Parameter] = Field(description="A list of the function's parameters.")
    returns: str = Field(description="A description of the value returned by the function and its type.")
    usage_example: str = Field(description="A simple, clear code block showing how to call this function.")

class ClassSummary(BaseModel):
    """Data model for the AI-generated summary of a class."""
    overall_description: str = Field(description="A paragraph explaining the purpose and capabilities of the class.")
    initialization: str = Field(description="An explanation of the __init__ method and its parameters.")
    key_methods: List[str] = Field(description="A bulleted list summarizing the most important public methods and what they do.")
    usage_example: str = Field(description="A simple, clear code block showing how to instantiate and use the class.")
