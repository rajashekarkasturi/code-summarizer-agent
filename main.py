# main_agentic.py

import os
from code_parser import CodeParser
from agentic_summarizer import AgenticSummarizer

def main():
    """
    Main function to orchestrate the agentic code summarization process.
    """
    codebase_path = 'sample_codebase'
    output_file = os.path.join('output', 'summary_agentic.md')

    print(f"Starting AGENTIC code summarization for codebase: '{codebase_path}'")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    try:
        summarizer = AgenticSummarizer()
    except Exception as e:
        print(f"Failed to initialize the summarizer. Have you set your API_KEY? Error: {e}")
        return

    final_summary = "# AI-Generated Codebase Summary\n\n"

    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"\nProcessing file: {file_path}")
                final_summary += f"## File: `{file_path}`\n\n"

                try:
                    parser = CodeParser(file_path)
                    code_elements = parser.get_code_elements()
                    
                    if not code_elements:
                        print(f" -> No functions or classes found.")
                        continue

                    print(f" -> Found {len(code_elements)} elements. Generating summaries...")

                    for element in code_elements:
                        print(f"   -> Generating summary for `{element['name']}`...")
                        if element['type'] == 'function':
                            structured_summary = summarizer.get_function_summary(element['source'])
                            markdown_summary = summarizer.format_function_summary_to_markdown(structured_summary, element['name'])
                        else: # 'class'
                            structured_summary = summarizer.get_class_summary(element['source'])
                            markdown_summary = summarizer.format_class_summary_to_markdown(structured_summary, element['name'])
                        
                        final_summary += markdown_summary + "\n\n---\n\n"

                except Exception as e:
                    error_message = f"Could not process file {file_path}. Error: {e}"
                    print(f"   -> ERROR: {error_message}")
                    final_summary += f"**Error processing this file:**\n```\n{error_message}\n```\n"

    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(final_summary)

    print(f"\nSummarization complete!")
    print(f"✅ Output saved to: {output_file}")

if __name__ == '__main__':
    main()
