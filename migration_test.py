"""
Migration Helper Script: OpenAI → Google Gemini API

This script provides migration patterns and testing utilities
Run: python migration_test.py
"""

import os
from dotenv import load_dotenv, find_dotenv

# Load environment
load_dotenv(find_dotenv())

def test_gemini_direct_api():
    """Test Pattern 1: Direct Gemini API Usage"""
    print("\n" + "="*60)
    print("TEST 1: Direct Gemini API Usage")
    print("="*60)
    
    try:
        import google.generativeai as genai
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("❌ GOOGLE_API_KEY not found in .env")
            return False
            
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content("Say 'Hello World' and nothing else.")
        
        print(f"✅ Direct API works!")
        print(f"Response: {response.text[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Direct API failed: {str(e)}")
        return False

def test_langchain_gemini():
    """Test Pattern 2: LangChain with ChatGoogleGenerativeAI"""
    print("\n" + "="*60)
    print("TEST 2: LangChain ChatGoogleGenerativeAI")
    print("="*60)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("❌ GOOGLE_API_KEY not found in .env")
            return False
            
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key,
            temperature=0.7
        )
        
        response = llm.invoke("Say 'Hello World' and nothing else.")
        
        print(f"✅ LangChain Gemini works!")
        print(f"Response: {response.content[:100]}...")
        return True
    except Exception as e:
        print(f"❌ LangChain Gemini failed: {str(e)}")
        return False

def test_langchain_prompt_chain():
    """Test Pattern 3: LangChain Chains with Prompts"""
    print("\n" + "="*60)
    print("TEST 3: LangChain Chain with Prompt")
    print("="*60)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain.prompts import ChatPromptTemplate
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("❌ GOOGLE_API_KEY not found in .env")
            return False
            
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key,
            temperature=0.7
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("user", "{input}")
        ])
        
        chain = prompt | llm
        response = chain.invoke({"input": "Hello"})
        
        print(f"✅ LangChain Chain works!")
        print(f"Response: {response.content[:100]}...")
        return True
    except Exception as e:
        print(f"❌ LangChain Chain failed: {str(e)}")
        return False

def show_migration_patterns():
    """Display common migration patterns"""
    print("\n" + "="*60)
    print("MIGRATION PATTERNS")
    print("="*60)
    
    patterns = {
        "Direct API": '''
# BEFORE (OpenAI):
import google.generativeai as genai
response = genai.GenerativeModel("gemini-2.0-flash").generate_content(
    model="gemini-1.5-flash",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)

# AFTER (Gemini):
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello")
print(response.text)
        ''',
        
        "LangChain LLM": '''
# BEFORE (OpenAI):
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# AFTER (Gemini):
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
        ''',
        
        "LangChain Chain": '''
# BEFORE (OpenAI):
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chain = LLMChain(llm=llm, prompt=prompt)

# AFTER (Gemini):
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chain = LLMChain(llm=llm, prompt=prompt)
        '''
    }
    
    for pattern_name, pattern_code in patterns.items():
        print(f"\n{pattern_name}:")
        print(pattern_code)

def main():
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "OpenAI → Google Gemini Migration Tests" + " "*9 + "║")
    print("╚" + "="*58 + "╝")
    
    # Show patterns
    show_migration_patterns()
    
    # Run tests
    test_results = {
        "Direct API": test_gemini_direct_api(),
        "LangChain Gemini": test_langchain_gemini(),
        "LangChain Chain": test_langchain_prompt_chain(),
    }
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in test_results.values() if v)
    total = len(test_results)
    
    for test_name, result in test_results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<30} {status}")
    
    print("="*60)
    print(f"PASSED: {passed}/{total}")
    print("="*60)
    
    if passed == total:
        print("\n✅ All tests passed! Your Gemini setup is ready.")
        print("\nNext Steps:")
        print("1. Update notebook files to use ChatGoogleGenerativeAI")
        print("2. Replace 'gpt-4o-mini' with 'gemini-1.5-flash'")
        print("3. Update .env with GOOGLE_API_KEY")
        print("\nSee GEMINI_MIGRATION_GUIDE.md for details.")
    else:
        print("\n❌ Some tests failed. Check your GOOGLE_API_KEY in .env")

if __name__ == "__main__":
    main()
