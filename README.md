# LangChain Course Directory Overview

This Markdown file provides a concise overview of each directory in the LangChain course, detailing the key focus and content of each.

## 🚀 Quick Start - Using FREE Google Gemini API (Recommended)

> **No paid API required!** Switch from OpenAI to Google's free Gemini API in 5 minutes.

### Fast Setup:
1. Get FREE API key: https://ai.google.dev/ (no credit card needed)
2. Copy key to `.env` file: `GOOGLE_API_KEY=your_key_here`
3. Auto-convert course code: `python convert_to_gemini.py --all`
4. Verify setup: `python migration_test.py`
5. Start learning! 🎓

**See [GEMINI_SETUP_GUIDE.md](GEMINI_SETUP_GUIDE.md) for complete instructions**

---

## OR Use OpenAI API (Requires Paid Account)

If you prefer to use OpenAI:
- Add your OpenAI API key to `.env`: `OPENAI_API_KEY=sk-...`
- Keep all course code as-is

---

- `01_OpenAI_API`

  - Basic usage of the OpenAI API for generative AI applications.

- `02_LangChain_Inputs_and_Outputs`

  - Understanding the input and output mechanisms within LangChain.

- `03_Prompt_Templates`

  - Templates and best practices for effective prompting for OpenAI models.

- `04_Chains`

  - Detailed exploration of the Chains in LangChain with different use cases.

- `05_Callbacks`

  - Utilizing callback functions in LangChain for dynamic responses and interactions.

- `06_Memory`

  - Techniques and methods for implementing memory in generative AI models.

- `07_OpenAI_Functions`

  - OpenAI Function Calling with the OpenAI API and LangChain.

- `08_RAG`

  - Deep dive into Retrieval Augmented Generation (RAG) and its implementation in LangChain.

- `09_Agents`

  - Building and managing Autonomous Agents within the LangChain framework.

- `10_Hybrid_Search_and_Indexing_API`

  - Integration and use of Hybrid Search and the Indexing API for efficient data indexing.

- `11_LangSmith`

  - Leveraging LangSmith for Tracing, Datasets, and Evaluation.

- `12_MicroServiceArchitecture`

  - Understanding and applying microservice architecture in large language model (LLM) applications.

- `13_LangChain_ExpressionLanguage`
  - Exploring the LangChain Expression Language with the Runnable Interface.

Each directory is structured to provide learners with theoretical knowledge and practical insights, enabling a comprehensive understanding of LangChain and its applications in the field of generative AI.

---

### Additional Instructions

Clone the repository: [LangChain Udemy Course](https://github.com/Coding-Crashkurse/LangChain-Udemy-Course)

Please rename the `.env.example` to `.env` and provide your OpenAI API Key.

### Cleanup of Notebook output:

Linux: `find . -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace {} \;`

Windows: `for /r %i in (*.ipynb) do jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True --inplace "%i"`

---

## 📚 Migration Guides & Resources

- **[GEMINI_SETUP_GUIDE.md](GEMINI_SETUP_GUIDE.md)** - Complete guide to use free Google Gemini API (Recommended)
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Code migration cheat sheet
- **[GEMINI_MIGRATION_GUIDE.md](GEMINI_MIGRATION_GUIDE.md)** - Detailed API differences
- **[convert_to_gemini.py](convert_to_gemini.py)** - Auto-convert script for all course code
- **[migration_test.py](migration_test.py)** - Test script to verify setup
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Project overview and structure
