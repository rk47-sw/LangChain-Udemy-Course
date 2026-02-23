#!/bin/bash
# Quick Start Setup Script for Gemini API Migration

echo "🚀 LangChain Course - Gemini API Quick Setup"
echo "=============================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo "Creating .env template..."
    cat > .env << 'EOF'
# Get your FREE API key from https://ai.google.dev/
# No credit card required!
GOOGLE_API_KEY=AIza_PASTE_YOUR_KEY_HERE

# Optional - LangSmith tracking
LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=
EOF
    echo "✅ Created .env file template"
    echo "✅ Add your GOOGLE_API_KEY from https://ai.google.dev/"
else
    echo "✅ .env file found"
fi

echo ""
echo "Next steps:"
echo "1. Get free API key: https://ai.google.dev/"
echo "2. Edit .env and add: GOOGLE_API_KEY=AIza_YOUR_KEY"
echo "3. Run: python migration_test.py"
echo ""
echo "Then start with: 01_OpenAI_API/code.ipynb"
