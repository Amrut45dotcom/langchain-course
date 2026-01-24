import os
from dotenv import load_dotenv

# Load .env FIRST
load_dotenv()


from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

def main():
    load_dotenv() 
    print("Hello from langchain-course!")
    information = """Narendra Damodardas Modi[a] (born 17 September 1950) is an Indian politician who has served as the prime minister of India since 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the member of parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindutva paramilitary volunteer organisation. He is the longest-serving prime minister outside the Indian National Congress."""

    summary_template = """
    given the information {information} about a person I want you to create :
    1. A short summary
    2. two interesting facts about them
"""

    summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)




if __name__ == "__main__":
    main()
