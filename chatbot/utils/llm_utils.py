from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from config import LLM_MODEL_NAME

llm = Ollama(model=LLM_MODEL_NAME)
parser = StrOutputParser()

def generate_response(prompt):
    return (prompt | llm | parser).invoke({})
