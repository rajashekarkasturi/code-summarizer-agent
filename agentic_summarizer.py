# agentic_summarizer.py

import os
from schemas import FunctionSummary, ClassSummary

# LangChain Imports
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from dotenv import load_dotenv
load_dotenv()

# Ensure you have your Google API Key set in your environment variables
# a-la: export GOOGLE_API_KEY="YOUR_API_KEY"
# if os.environ.get("GOOGLE_API_KEY") is None:
#     print("GOOGLE_API_KEY environment variable not set. The agent will not work.")

if os.environ.get("GROQ_API_KEY") is None:
    print("GROQ_API_KEY environment variable not set. The agent will not work.")

# if os.environ.get("OPENAI_API_KEY") is None:
#     print("OPENAI_API_KEY environment variable not set. The agent will not work.")


class AgenticSummarizer:
    """
    Generates structured code summaries using LangChain and a powerful LLM.
    """
    def __init__(self):
        """Initializes the summarizer with the LLM and output parsers."""

        # self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
        # self.llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

        self.llm = ChatGroq(model="moonshotai/kimi-k2-instruct", temperature=0.2) # Replace with your preferred model, follow the docs at (https://python.langchain.com/docs/integrations/chat/)

        self.function_parser = PydanticOutputParser(pydantic_object=FunctionSummary)
        self.class_parser = PydanticOutputParser(pydantic_object=ClassSummary)

    def _create_chain(self, parser, prompt_template_string):
        """Helper to create a LangChain chain."""
        prompt = PromptTemplate(
            template=prompt_template_string,
            input_variables=["code_snippet"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        return prompt | self.llm | parser

    def get_function_summary(self, code_snippet: str) -> FunctionSummary:
        """Generates a structured summary for a Python function."""
        prompt_template = """
        You are an expert programmer creating documentation. Analyze the following Python function.
        Your response must be a JSON object that strictly follows the provided schema.

        {format_instructions}

        **Code to analyze:**
        ```python
        {code_snippet}
        ```
        """
        chain = self._create_chain(self.function_parser, prompt_template)
        return chain.invoke({"code_snippet": code_snippet})

    def get_class_summary(self, code_snippet: str) -> ClassSummary:
        """Generates a structured summary for a Python class."""
        prompt_template = """
        You are an expert programmer creating documentation. Analyze the following Python class.
        Your response must be a JSON object that strictly follows the provided schema.

        {format_instructions}

        **Code to analyze:**
        ```python
        {code_snippet}
        ```
        """
        chain = self._create_chain(self.class_parser, prompt_template)
        return chain.invoke({"code_snippet": code_snippet})

    @staticmethod
    def format_function_summary_to_markdown(summary: FunctionSummary, name: str) -> str:
        """Formats the structured function summary into a Markdown string."""
        md = f"### Function: `{name}`\n\n"
        md += f"**Description:**\n{summary.description}\n\n"
        md += "**Parameters:**\n"
        if summary.parameters:
            for param in summary.parameters:
                md += f"- `{param.name}` ({param.param_type}): {param.description}\n"
        else:
            md += "- This function takes no parameters.\n"
        md += f"\n**Returns:**\n{summary.returns}\n\n"
        md += f"**Usage Example:**\n```python\n{summary.usage_example}\n```"
        return md

    @staticmethod
    def format_class_summary_to_markdown(summary: ClassSummary, name: str) -> str:
        """Formats the structured class summary into a Markdown string."""
        md = f"### Class: `{name}`\n\n"
        md += f"**Overall Description:**\n{summary.overall_description}\n\n"
        md += f"**Initialization:**\n{summary.initialization}\n\n"
        md += "**Key Methods:**\n"
        for method in summary.key_methods:
            md += f"- {method}\n"
        md += f"\n**Usage Example:**\n```python\n{summary.usage_example}\n```"
        return md
