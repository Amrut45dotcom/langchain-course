from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)



"""If we just print the prompt after using the JSONparser it would show an extra command in addition to our own template that is Return a JSON object so the model receives this command from the JSONparser before runtime by usin the .get_format_instructions that we used"""
chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
