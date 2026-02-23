# Migration from OpenAI to Google Gemini API - Complete Guide

## Quick Start

### 1. Get Free Google Gemini API Key
- Go to [Google AI Studio](https://ai.google.dev/)
- Click "Get API Key"
- Create a new API key (free, no credit card needed)
- Copy the key

### 2. Update Environment Variables

Replace `.env.example`:
```env
GOOGLE_API_KEY=your-google-api-key-here
LANGGRAPH_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls__...
```

Then rename to `.env` and add your key.

### 3. Code Migration Patterns

#### Pattern 1: Direct API Usage (Replace)
**Before (OpenAI):**
```python
import openai

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}]
)
```

**After (Gemini):**
```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Hello")
print(response.text)
```

#### Pattern 2: LangChain ChatOpenAI (Replace)
**Before (OpenAI):**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)
```

**After (Gemini):**
```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
```

#### Pattern 3: Chains & Memory (Update LLM)
**Before:**
```python
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-4o-mini")
chain = LLMChain(llm=llm, prompt=prompt)
```

**After:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chain = LLMChain(llm=llm, prompt=prompt)
```

## Model Mapping

| OpenAI | Gemini |
|--------|--------|
| gpt-4 | gemini-2.0-flash |
| gpt-4o | gemini-2.0-flash |
| gpt-4o-mini | gemini-1.5-flash |
| gpt-3.5-turbo | gemini-1.5-flash |

## API Differences to Note

1. **Response Structure**
   - OpenAI: `response.choices[0].message.content`
   - Gemini: `response.text`

2. **Message Format**
   - OpenAI: Uses role-based messages (system, user, assistant)
   - Gemini: Similar via LangChain, but native API is simpler

3. **Temperature Range**
   - Both: 0.0 to 1.0 (or 2.0 for Gemini)

4. **Rate Limits**
   - Gemini Free: 60 RPM, 1M tokens/month (sufficient for learning)

## File-by-File Migration Status

### Updated Files:
- ✅ .env.example
- ✅ UPDATE_ME_FOR_GEMINI.py (Conversion helper script)

### Files Needing Updates:
1. **01_OpenAI_API/code.ipynb** - Direct API usage → Gemini
2. **02_LangChain_Inputs_and_Outputs/code.ipynb** - Replace ChatOpenAI
3. **03_Prompt_Templates/code.ipynb** - Replace ChatOpenAI
4. **04_Chains/basics_and_outputerparsers.ipynb** - Replace ChatOpenAI
5. **04_Chains/advanced_chains.ipynb** - Replace ChatOpenAI
6. **05_Callbacks/code.ipynb** - Replace ChatOpenAI
7. **06_Memory/code.ipynb** - Replace ChatOpenAI
8. **06_Memory/chatbot.py** - Replace imports
9. **06_Memory/chatbot_solution.py** - Replace imports
10. **07_OpenAI_Functions/tool_calling.ipynb** - Tool use with Gemini
11. **08_RAG/code.ipynb** - Replace ChatOpenAI
12. **08_RAG/api.py** - Replace imports
13. **09_Agents/agents.ipynb** - Replace ChatOpenAI
14. **10_Hybrid_Search_and_Indexing_API/indexing_api.ipynb** - Replace ChatOpenAI
15. **10_Hybrid_Search_and_Indexing_API/filtered_search.ipynb** - Replace ChatOpenAI
16. **11_LangSmith/code.ipynb** - Replace ChatOpenAI
17. **12_MicroServiceArchitecture/service2/app.py** - Replace imports
18. **12_MicroServiceArchitecture/service3/app.py** - Replace imports
19. **12_MicroServiceArchitecture/insert_data.py** - Replace imports
20. **13_LangChain_ExpressionLanguage/13_01_LCEL_Deepdive.ipynb** - Replace ChatOpenAI
21. **13_LangChain_ExpressionLanguage/13_02_LCEL_And_Runnables.ipynb** - Replace ChatOpenAI
22. **13_LangChain_ExpressionLanguage/13_03_Chain_Migrations.ipynb** - Replace ChatOpenAI
23. **13_LangChain_ExpressionLanguage/13_04_Chain_Migration_Advanced.ipynb** - Replace ChatOpenAI

## Advantages of Gemini API (Free Tier)

✅ **No Credit Card Required** - Completely free  
✅ **Faster Response Times** - Gemini 2.0 Flash is optimized for speed  
✅ **Good for Learning** - 60 RPM is enough for course practice  
✅ **1M Tokens/Month** - Sufficient for all 13 modules  
✅ **Same Quality** - Capable models with few differences from paid tiers  

## Usage Instructions

1. Set `GOOGLE_API_KEY` in your `.env` file
2. Replace all `from langchain_openai import ChatOpenAI` with `from langchain_google_genai import ChatGoogleGenerativeAI`
3. Replace `ChatOpenAI(model="gpt-4o-mini")` with `ChatGoogleGenerativeAI(model="gemini-1.5-flash")`
4. Update any direct API calls from `openai` to `google.generativeai`

## Testing Your Setup

Run this to verify Gemini works:
```bash
python migration_test.py
```

## Additional Resources

- [Google Generative AI Docs](https://ai.google.dev/docs)
- [LangChain Google Integration](https://python.langchain.com/docs/integrations/llms/google_generative_ai)
- [Gemini API Reference](https://ai.google.dev/api)

---

**Questions?** Refer to the migration examples in `UPDATE_ME_FOR_GEMINI.py`
