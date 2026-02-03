##from langchain_classic.agents import AgentExecutor, create_react_agent
##from langchain_core.output_parsers.pydantic import PydanticOutputParser
##from langchain_core.prompts import PromptTemplate
##from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from typing import TypedDict,Annotated,Optional,Literal

from dotenv import load_dotenv
load_dotenv()

##from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
##from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
##output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structrued_llm = llm.with_structured_output(Review)
result = structrued_llm.invoke(""" Samsung Galaxy S23 Ultra: A Powerhouse of Performance
The Samsung Galaxy S23 Ultra is a top-tier smartphone that excels in almost every category. Its standout features include:
* Incredible Camera: The 200MP main sensor captures stunning photos with incredible detail and dynamic range.
* Powerful Performance: The Snapdragon 8 Gen 2 processor delivers blazing-fast speeds and smooth multitasking.
* Vibrant Display: The dynamic AMOLED 2X display boasts incredible brightness, sharp visuals, and smooth scrolling.
* Long-lasting Battery: The large battery provides all-day endurance, even with heavy usage.
However:
* Expensive: The S23 Ultra comes with a premium price tag.
* S Pen can be finicky: Some users find the S Pen integration to be less seamless than advertised.
Overall:
The Samsung Galaxy S23 Ultra is an exceptional smartphone for demanding users. If you're looking for the best of the best and are willing to pay the price, it's a fantastic choice.
Disclaimer: This is a brief overview. For a more in-depth analysis, please refer to full reviews from reputable tech publications.
I hope this helps!""")

print(result)












"""react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names"],
).partial(format_instructions=output_parser.get_format_instructions())

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_format_instructions,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)


def clean_output(text: str) -> str:
    text = text.strip()
    if text.startswith("```json"):
        text = text[len("```json"):]
    if text.startswith("```"):
        text = text[len("```"):]
    if text.endswith("```"):
        text = text[:-len("```")]
    return text.strip()


extract_output = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(clean_output(x)))
chain = agent_executor | extract_output | parse_output


def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
        }
    )
    print(result)


if __name__ == "__main__":
    main()"""