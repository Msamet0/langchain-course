from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool 
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
    
def run_Agent():
    result=agent.invoke({"messages":HumanMessage(content="İstanbulda hava nasıl")} )
    print(result)
    
    final_answer = result["messages"][-1].content
    print(f"\nAI Yanıtı: {final_answer}")

if __name__ == "__main__":
    run_Agent()    
   