# 🔄 Complete Setup Guide: LangChain Course with Google Gemini API (FREE)

## ✨ Overview

This guide helps you switch the entire LangChain course from **paid OpenAI API** to the **free Google Gemini API**.

**Key Benefits:**
- ✅ **Completely FREE** - No credit card required
- ✅ **Fast** - Gemini 2.0 Flash is optimized for speed  
- ✅ **Generous limits** - 60 RPM, 1M tokens/month (plenty for learning)
- ✅ **Same quality** - Capable models suitable for all course modules
- ✅ **Easy migration** - Simple code changes with automated tools provided

---

## 📋 Prerequisites

You should already have:
- ✅ Python 3.10+ 
- ✅ Virtual environment created
- ✅ Dependencies installed (pip list shows langchain, langchain-google-genai, etc.)

If not, refer to PROJECT_STRUCTURE.md

---

## 🚀 Step 1: Get Free Google API Key (2 minutes)

### Option A: Quick Setup (Recommended)

1. Go to **[Google AI Studio](https://ai.google.dev/)**
2. Click **"Get API Key"** button
3. Select **"Create API key in new project"**
4. Copy the generated API key
5. Done! ✅

### Option B: Google Cloud Console (More Control)

1. Go to **[Google Cloud Console](https://console.cloud.google.com/)**
2. Create a new project (or use existing)
3. Enable **"Generative Language API"**
4. Go to **Credentials** → **Create Credentials** → **API Key**
5. Copy the key

---

## ⚙️ Step 2: Configure Your Environment

### 2.1 Create `.env` file from template

```bash
# In your LangChain-Udemy-Course directory
cp .env.example .env
```

### 2.2 Edit `.env` and add your API key

Open `.env` and update:

```env
# Google Gemini API (your actual key from Step 1)
GOOGLE_API_KEY=AIza...YourActualKeyHere...

# Optional: LangSmith for tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls__...
```

### 2.3 Verify configuration

```bash
# Activate venv first
.\venv\Scripts\Activate.ps1

# Test that key is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(f'✓ GOOGLE_API_KEY set: {len(os.getenv(\"GOOGLE_API_KEY\", \"\")) > 0}')"
```

---

## 🔧 Step 3: Test Your Setup

### Run the migration test script

```bash
# Activate venv
.\venv\Scripts\Activate.ps1

# Run tests  
python migration_test.py
```

**Expected Output:**
```
✅ Direct API works!
✅ LangChain Gemini works!
✅ LangChain Chain works!

All tests passed! Your Gemini setup is ready.
```

---

## 🔄 Step 4: Convert Code (Choose One Method)

### Method A: Auto-Convert Everything (Recommended)

```bash
# Preview changes first
python convert_to_gemini.py --all --preview

# Apply conversions
python convert_to_gemini.py --all
```

### Method B: Manual Conversion

For each file using OpenAI, make these changes:

**Find:**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

**Replace with:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
```

### Method C: Convert Specific Modules

```bash
# Convert only notebooks
python convert_to_gemini.py --notebooks

# Convert single file
python convert_to_gemini.py --file path/to/file.py
```

---

## 📊 Model Compatibility

| Use Case | OpenAI (Paid) | Gemini (Free) | Notes |
|----------|---|---|---|
| Chat/Text | gpt-4o-mini | gemini-1.5-flash | ✅ Recommended |
| Fast responses | gpt-4o-mini | gemini-2.0-flash | ✅ Faster alternative |
| Complex tasks | gpt-4 | gemini-2.0-flash | ✅ Equivalent capability |
| Memory/Chains | gpt-3.5-turbo | gemini-1.5-flash | ✅ Works great |

---

## 📚 Module-by-Module Migration

### Format per module:
```python
# Old way (OpenAI)
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")

# New way (Gemini)
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
```

| Module | Status | Notes |
|--------|--------|-------|
| 01_OpenAI_API | ⚠️ Needs conversion | Direct API→Gemini API |
| 02_LangChain_Inputs_and_Outputs | 🔄 Auto-convertible | Replace ChatOpenAI |
| 03_Prompt_Templates | 🔄 Auto-convertible | Replace ChatOpenAI |
| 04_Chains | 🔄 Auto-convertible | Replace ChatOpenAI |
| 05_Callbacks | 🔄 Auto-convertible | Replace ChatOpenAI |
| 06_Memory | 🔄 Auto-convertible | Replace ChatOpenAI |
| 07_OpenAI_Functions | ⚠️ Needs review | Tool use compatible |
| 08_RAG | 🔄 Auto-convertible | Replace ChatOpenAI |
| 09_Agents | 🔄 Auto-convertible | Replace ChatOpenAI |
| 10_Hybrid_Search | 🔄 Auto-convertible | Replace ChatOpenAI |
| 11_LangSmith | 🔄 Auto-convertible | Replace ChatOpenAI |
| 12_MicroServices | 🔄 Auto-convertible | Replace ChatOpenAI |
| 13_LCEL | 🔄 Auto-convertible | Replace ChatOpenAI |

---

## 📝 Common Patterns

### Pattern 1: Simple Chat

**Before:**
```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([...])
chain = prompt | llm
response = chain.invoke({...})
```

**After:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
prompt = ChatPromptTemplate.from_messages([...])
chain = prompt | llm
response = chain.invoke({...})
```

### Pattern 2: With Memory

**Before:**
```python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(model="gpt-4o-mini")
memory = ConversationBufferMemory()
```

**After:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
memory = ConversationBufferMemory()
```

### Pattern 3: Agents

**Before:**
```python
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent

llm = ChatOpenAI(model="gpt-4o-mini")
agent_executor = create_openai_tools_agent(...)
```

**After:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
agent_executor = create_tool_calling_agent(...)
```

---

## ⚠️ Important Differences

### API Response Structure

**OpenAI:**
```python
response = openai.chat.completions.create(...)
print(response.choices[0].message.content)
```

**Gemini:**
```python
response = model.generate_content(...)
print(response.text)
```

### Temperature Parameter

- **OpenAI:** 0.0 - 1.0
- **Gemini:** 0.0 - 2.0 (same range works fine)

### Function Calling

- **OpenAI:** `tools`, `tool_choice`
- **Gemini:** `tools`, `tool_config` (similar but slight naming differences)

---

## 🐛 Troubleshooting

### Error: "GOOGLE_API_KEY not found"
```
Solution: Make sure .env file is in the project root and has GOOGLE_API_KEY=your_key
```

### Error: "APIError: Invalid API Key"
```
Solution: 
1. Double-check your API key from ai.google.dev
2. Make sure there are no extra spaces
3. Regenerate key if needed
```

### Error: "Rate limit exceeded"
```
Solution: Free tier is 60 RPM. Wait a minute before retrying.
Free tier also has 1M tokens/month limit.
```

### Error: "Model not found"
```
Solution: Use these models:
- gemini-2.0-flash (recommended, fastest)
- gemini-1.5-flash (stable, balanced)
- gemini-1.5-pro (more capable but same free tier)
```

---

## 🎯 Next Steps

1. ✅ Get API key from Google AI Studio
2. ✅ Create/update `.env` file with GOOGLE_API_KEY
3. ✅ Run `migration_test.py` to verify setup
4. ✅ Run `convert_to_gemini.py --all` to convert code
5. ✅ Start learning! Run notebooks in order

---

## 📖 Learning Path

**Simple to Complex:**
1. **Start:** 01_OpenAI_API → understand basics
2. **Learn:** 02_Inputs_and_Outputs → 03_Prompts → 04_Chains
3. **Intermediate:** 05_Callbacks → 06_Memory → 07_Functions
4. **Advanced:** 08_RAG → 09_Agents → 10_Hybrid_Search
5. **Mastery:** 11_LangSmith → 12_Microservices → 13_LCEL

Each module builds on previous ones. Skip only if you're experienced.

---

## 💬 API Usage Tips

- **Keep conversations short** for free tier (1M tokens/month)
- **Batch requests** when possible
- **Use faster models** (gemini-2.0-flash) to save tokens
- **Cache prompts** for repeated queries
- **Monitor usage** at [Google AI Studio](https://ai.google.dev/)

---

## 🔗 Useful Resources

- [Google Generative AI Docs](https://ai.google.dev/docs)
- [LangChain Google Integration](https://python.langchain.com/docs/integrations/llms/google_generative_ai)
- [Gemini API Reference](https://ai.google.dev/api)
- [Migration FAQ](GEMINI_MIGRATION_GUIDE.md)

---

## ✨ You're Ready!

Your LangChain course environment is now:
- ✅ Using free Google Gemini API (no paid subscription needed)
- ✅ Fully compatible with all 13 course modules
- ✅ Ready for learning and experimentation

**Happy learning!** 🚀

