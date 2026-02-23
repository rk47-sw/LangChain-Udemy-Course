"""
Batch Conversion Script: Converts Python files and Notebooks from OpenAI to Gemini

Usage:
    python convert_to_gemini_fixed.py --all              # Convert all files
    python convert_to_gemini_fixed.py --file path.py     # Convert single file
    python convert_to_gemini_fixed.py --notebooks         # Convert only notebooks
    python convert_to_gemini_fixed.py --preview           # Preview changes without applying
"""

import os
import json
import re
import argparse
import sys
from pathlib import Path

class GeminiConverter:
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root)
        self.changes = []
        
    def convert_python_file(self, file_path, preview_only=False):
        """Convert Python file from OpenAI to Gemini"""
        file_path = Path(file_path)
        
        if not file_path.exists():
            print(f"[ERROR] File not found: {file_path}")
            return False
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Replace imports
            content = re.sub(
                r'from\s+langchain_openai\s+import\s+ChatOpenAI',
                'from langchain_google_genai import ChatGoogleGenerativeAI',
                content
            )
            
            content = re.sub(
                r'from\s+langchain_openai\s+import\s+OpenAIEmbeddings',
                'from langchain_google_genai import GoogleGenerativeAIEmbeddings',
                content
            )
            
            content = re.sub(
                r'from\s+langchain_community\.embeddings\s+import\s+OpenAIEmbeddings',
                'from langchain_google_genai import GoogleGenerativeAIEmbeddings',
                content
            )
            
            content = re.sub(
                r'import\s+openai\s*\n',
                'import google.generativeai as genai\n',
                content
            )
            
            # Replace ChatOpenAI with ChatGoogleGenerativeAI
            content = re.sub(
                r'ChatOpenAI\s*\(',
                'ChatGoogleGenerativeAI(',
                content
            )
            
            # Replace OpenAIEmbeddings with GoogleGenerativeAIEmbeddings
            content = re.sub(
                r'OpenAIEmbeddings\s*\(',
                'GoogleGenerativeAIEmbeddings(',
                content
            )
            
            # Replace model names
            model_replacements = {
                r'model\s*=\s*["\']gpt-4o-mini["\']': 'model="gemini-1.5-flash"',
                r'model\s*=\s*["\']gpt-4o["\']': 'model="gemini-1.5-flash"',
                r'model\s*=\s*["\']gpt-4["\']': 'model="gemini-1.5-flash"',
                r'model\s*=\s*["\']gpt-3.5-turbo["\']': 'model="gemini-1.5-flash"',
            }
            
            for old_model, new_model in model_replacements.items():
                content = re.sub(old_model, new_model, content)
            
            # Replace api_key parameter
            content = re.sub(
                r'api_key\s*=\s*os\.getenv\(["\']OPENAI_API_KEY["\']\)',
                'google_api_key=os.getenv("GOOGLE_API_KEY")',
                content
            )
            
            # Replace direct API calls
            content = re.sub(
                r'openai\.chat\.completions\.create\(',
                'genai.GenerativeModel("gemini-2.0-flash").generate_content(',
                content
            )
            
            if content != original:
                if not preview_only:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"[OK] Converted: {file_path}")
                else:
                    print(f"[PREVIEW] {file_path}")
                
                self.changes.append(str(file_path))
                return True
            else:
                print(f"[INFO] No changes needed: {file_path}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Error converting {file_path}: {str(e)}")
            return False
    
    def convert_notebook(self, notebook_path, preview_only=False):
        """Convert Jupyter notebook from OpenAI to Gemini"""
        notebook_path = Path(notebook_path)
        
        if not notebook_path.exists() or notebook_path.suffix != '.ipynb':
            print(f"[ERROR] Notebook not found: {notebook_path}")
            return False
            
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
            
            original = json.dumps(notebook)
            code_cells_changed = 0
            
            for cell in notebook.get('cells', []):
                if cell['cell_type'] == 'code':
                    source_text = ''.join(cell.get('source', []))
                    
                    # Replace imports
                    source_text = re.sub(
                        r'from\s+langchain_openai\s+import\s+OpenAIEmbeddings',
                        'from langchain_google_genai import GoogleGenerativeAIEmbeddings',
                        source_text
                    )
                    
                    source_text = re.sub(
                        r'from\s+langchain_openai\s+import\s+ChatOpenAI',
                        'from langchain_google_genai import ChatGoogleGenerativeAI',
                        source_text
                    )
                    
                    source_text = re.sub(
                        r'from\s+langchain_openai\s+import\s+(.*)',
                        lambda m: f'from langchain_google_genai import {m.group(1)}',
                        source_text
                    )
                    
                    source_text = re.sub(
                        r'import\s+openai',
                        'import google.generativeai as genai',
                        source_text
                    )
                    
                    # Replace ChatOpenAI
                    source_text = re.sub(
                        r'ChatOpenAI\s*\(',
                        'ChatGoogleGenerativeAI(',
                        source_text
                    )
                    
                    # Replace OpenAIEmbeddings
                    source_text = re.sub(
                        r'OpenAIEmbeddings\s*\(',
                        'GoogleGenerativeAIEmbeddings(',
                        source_text
                    )
                    
                    # Replace model names
                    model_replacements = {
                        r'["\']gpt-4o-mini["\']': '"gemini-1.5-flash"',
                        r'["\']gpt-4o["\']': '"gemini-1.5-flash"',
                        r'["\']gpt-4["\']': '"gemini-1.5-flash"',
                        r'["\']gpt-3.5-turbo["\']': '"gemini-1.5-flash"',
                    }
                    
                    for old_model, new_model in model_replacements.items():
                        source_text = re.sub(old_model, new_model, source_text)
                    
                    # Update source
                    if isinstance(cell['source'], list):
                        cell['source'] = source_text.splitlines(keepends=True)
                    else:
                        cell['source'] = source_text
                    
                    code_cells_changed += 1
            
            if json.dumps(notebook) != original:
                if not preview_only:
                    with open(notebook_path, 'w', encoding='utf-8') as f:
                        json.dump(notebook, f, indent=1)
                    print(f"[OK] Converted: {notebook_path}")
                else:
                    print(f"[PREVIEW] {notebook_path}")
                
                self.changes.append(str(notebook_path))
                return True
            else:
                print(f"[INFO] No changes needed: {notebook_path}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Error converting {notebook_path}: {str(e)}")
            return False
    
    def convert_all(self, preview_only=False):
        """Convert all Python files and notebooks"""
        print("\n[INFO] Finding files to convert...")
        
        # Find Python files
        py_files = list(self.repo_root.rglob("*.py"))
        py_files = [f for f in py_files if "venv" not in str(f) and ".git" not in str(f)]
        
        # Find notebooks
        nb_files = list(self.repo_root.rglob("*.ipynb"))
        nb_files = [f for f in nb_files if "venv" not in str(f) and ".git" not in str(f)]
        
        print(f"[INFO] Found {len(py_files)} Python files and {len(nb_files)} notebooks\n")
        
        # Convert Python files
        if py_files:
            print("Converting Python files...")
            for py_file in py_files:
                self.convert_python_file(py_file, preview_only=preview_only)
        
        # Convert notebooks
        if nb_files:
            print("\nConverting Jupyter notebooks...")
            for nb_file in nb_files:
                self.convert_notebook(nb_file, preview_only=preview_only)
        
        # Summary
        print("\n" + "="*60)
        print(f"CONVERSION COMPLETE")
        print("="*60)
        print(f"Total files modified: {len(self.changes)}")
        
        if self.changes:
            print("\nModified files:")
            for f in self.changes:
                print(f"  - {f}")
        
        if preview_only:
            print("\n[INFO] Run without --preview to apply changes")

def main():
    parser = argparse.ArgumentParser(description="Convert OpenAI code to Gemini API")
    parser.add_argument("--all", action="store_true", help="Convert all files")
    parser.add_argument("--file", type=str, help="Convert specific file")
    parser.add_argument("--notebooks", action="store_true", help="Convert only notebooks")
    parser.add_argument("--preview", action="store_true", help="Preview changes without applying")
    
    args = parser.parse_args()
    
    repo_root = Path(__file__).parent
    converter = GeminiConverter(repo_root)
    
    if args.file:
        converter.convert_python_file(args.file, preview_only=args.preview)
    elif args.all:
        converter.convert_all(preview_only=args.preview)
    elif args.notebooks:
        nb_files = list(repo_root.rglob("*.ipynb"))
        nb_files = [f for f in nb_files if "venv" not in str(f)]
        for nb_file in nb_files:
            converter.convert_notebook(nb_file, preview_only=args.preview)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
