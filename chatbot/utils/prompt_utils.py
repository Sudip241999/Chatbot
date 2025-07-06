from langchain_core.prompts import ChatPromptTemplate
from config import SYSTEM_PROMPT
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


def build_context_prompt(history, user_input):
    """Builds the full chat prompt with history and system instructions."""
    messages = [SystemMessage(content=SYSTEM_PROMPT)]

    for msg in history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=user_input))
    
    return ChatPromptTemplate.from_messages(messages)
