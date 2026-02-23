# 🔥 Quick Reference: OpenAI → Gemini Migration

## 5-Minute Setup

```bash
# 1. Get FREE API key from https://ai.google.dev/
# 2. Update .env file
GOOGLE_API_KEY=your_key_here

# 3. Run test
python migration_test.py

# 4. Convert code
python convert_to_gemini.py --all

# Done! ✅
```

---

## Code Cheat Sheet

### Import Changes

| What | From | To |
|------|------|-------|
| **LLM** | `from langchain_openai import ChatOpenAI` | `from langchain_google_genai import ChatGoogleGenerativeAI` |
| **Direct API** | `import openai` | `import google.generativeai as genai` |

### Class Changes

| Pattern | Before | After |
|---------|--------|-------|
| **Basic** | `ChatOpenAI(model="gpt-4o-mini")` | `ChatGoogleGenerativeAI(model="gemini-2.5-pro")` |
| **With API Key** | `ChatOpenAI(api_key=...)` | `ChatGoogleGenerativeAI(google_api_key=...)` |
| **With Temp** | `ChatOpenAI(temperature=0.7)` | `ChatGoogleGenerativeAI(temperature=0.7)` |

### Model Mapping

| Speed Level | OpenAI | Gemini |
|--------|--------|--------|
| 🐢 **Slow** | gpt-4 | gemini-2.0-flash |
| 🐇 **Fast** | gpt-4o-mini | gemini-2.5-pro |
| ⚡ **Fastest** | - | gemini-2.0-flash |

**Recommendation:** Use `gemini-2.5-pro` for all tasks (latest model)

### One-Liners

```python
# Old
from langchain_openai import ChatOpenAI; llm = ChatOpenAI(model="gpt-4o-mini")

# New
from langchain_google_genai import ChatGoogleGenerativeAI; llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
```

---

## Common Patterns

### 1️⃣ Simple Chat
```python
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
response = llm.invoke("Hello")
print(response.content)
```

### 2️⃣ With Prompt Template
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
prompt = ChatPromptTemplate.from_template("You are a {role}. User: {input}")
chain = prompt | llm
result = chain.invoke({"role": "chef", "input": "pasta recipe"})
```

### 3️⃣ With Memory
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
memory = ConversationBufferMemory()
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
```

### 4️⃣ With Tools/Agents
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)
```

---

## Environment Setup

### .env Template
```env
# Required
GOOGLE_API_KEY=AIz...

# Optional - LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls__...
```

### Load .env
```python
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```

---

## Tools & Scripts

| Tool | Purpose | Command |
|------|---------|---------|
| **migration_test.py** | Test setup | `python migration_test.py` |
| **convert_to_gemini.py** | Auto-convert files | `python convert_to_gemini.py --all` |
| **Guides** | Read docs | `GEMINI_SETUP_GUIDE.md` |

---

## API Limits (Free Tier)

| Limit | Value | Impact |
|-------|-------|--------|
| **RPM** | 60 | ~1 request/second |
| **TPM** | 1M/month | Huge for learning |
| **Cost** | $0 | Always free |

**Enough for:** All 13 course modules + experimentation

---

## Common Issues

| Error | Solution |
|-------|----------|
| `GOOGLE_API_KEY not found` | Add to `.env` in project root |
| `APIError: Invalid API Key` | Regenerate key at ai.google.dev |
| `Rate limit` | Free tier has 60 RPM, wait between requests |
| `Model not found` | Use `gemini-2.5-pro` (recommended) |

---

## Module-Specific Notes

| Module | Notes |
|--------|-------|
| **01_OpenAI_API** | Replace direct API calls with Gemini API |
| **02-06** | Just replace ChatOpenAI with ChatGoogleGenerativeAI |
| **07_Functions** | Use tool_calling_agent instead of openai_tools_agent |
| **08_RAG** | Embedding models may differ, check docs |
| **09_Agents** | Use create_tool_calling_agent |
| **10-13** | Standard LLM replacement |

---

## Auto-Conversion

### Preview changes
```bash
python convert_to_gemini.py --all --preview
```

### Apply changes
```bash
python convert_to_gemini.py --all
```

### Convert specific type
```bash
python convert_to_gemini.py --notebooks    # Only .ipynb files
python convert_to_gemini.py --file file.py  # Single file
```

---

## Resources

📚 **Documentation**
- [Google Gemini Docs](https://ai.google.dev/docs)
- [LangChain Google Integration](https://python.langchain.com/docs/integrations/llms/google_generative_ai)

🎓 **Learning**
- [Gemini Recipes](https://github.com/google-gemini/gemini-cookbook)
- [LangChain Docs](https://python.langchain.com/)

---

## Next Steps

1. ✅ Get API key: https://ai.google.dev/
2. ✅ Update `.env`
3. ✅ Run `python migration_test.py`
4. ✅ Run `python convert_to_gemini.py --all`
5. ✅ Start learning from Module 01

---

**Pro Tip:** Save this file for quick lookups while learning! 📌
