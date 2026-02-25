from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

database = [
    {"name": "Salami", "price": 9.99},
    {"name": "Margherita", "price": 8.99},
    {"name": "Pepperoni", "price": 10.99},
    {"name": "Hawaiian", "price": 11.49},
    {"name": "Veggie Supreme", "price": 10.49},
]


@tool
def get_pizza_info(pizza_name: str) -> dict:
    """Retrieve information about a specific pizza from the database.

    Args:
        pizza_name: Name of the pizza.

    Returns:
        A dictionary containing the pizza's name and price or a message indicating the pizza wasn't found.
    """
    for pizza in database:
        if pizza["name"] == pizza_name:
            return pizza
    return {"message": f"No pizza found with the name {pizza_name}."}


@tool
def add_pizza(pizza_name: str, price: float) -> dict:
    """Add a new pizza to the database.

    Args:
        pizza_name: Name of the new pizza.
        price: Price of the new pizza.

    Returns:
        A message indicating the result of the addition.
    """
    for pizza in database:
        if pizza["name"] == pizza_name:
            return {"message": f"Pizza {pizza_name} already exists in the database."}

    database.append({"name": pizza_name, "price": price})
    return {"message": f"Pizza {pizza_name} added successfully!"}


# Initialize the LLM with Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


# Define the tools
tools = [get_pizza_info, add_pizza]

# Bind tools to the LLM
llm_with_tools = llm.bind_tools(tools)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI chatbot having a conversation with a human."),
    ("human", "{human_input}")
])

# Create the base chain
chain = prompt | llm_with_tools


def execute_tools(msg):
    """Execute tool calls from the model's response."""
    tool_results = []
    for tool_call in msg.tool_calls:
        if tool_call["name"] == "get_pizza_info":
            result = get_pizza_info.invoke(tool_call["args"])
            tool_results.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )
        elif tool_call["name"] == "add_pizza":
            result = add_pizza.invoke(tool_call["args"])
            tool_results.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )
    return tool_results


def chat_with_tools(human_input: str):
    """Process user input with tool calling capability."""
    # First call
    messages = [
        HumanMessage(content=human_input)
    ]
    
    response = llm_with_tools.invoke(messages)
    
    # Check if function calling is needed
    if response.tool_calls:
        print(f"Tool calls detected: {response.tool_calls}")
        
        # Execute functions
        tool_results = execute_tools(response)
        
        # Add function call and results to messages
        messages.append(response)
        messages.extend(tool_results)
        
        # Get final response
        final_response = llm_with_tools.invoke(messages)
        return final_response.content
    
    return response.content


# Test examples
if __name__ == "__main__":
    # Test 1: Add a new pizza
    print("Test 1: Adding a new pizza")
    result1 = chat_with_tools("I want to add the pizza 'Jumbo' for 13.99")
    print(f"Response: {result1}")
    print(f"Database after add: {database}")
    print()
    
    # Test 2: Query about non-pizza topic (should not use tools)
    print("Test 2: Non-pizza query")
    result2 = chat_with_tools("Who are the main characters of the A-Team?")
    print(f"Response: {result2}")
    print()
    
    # Test 3: Get pizza info
    print("Test 3: Get pizza info")
    result3 = chat_with_tools("How much does the Jumbo pizza cost?")
    print(f"Response: {result3}")
