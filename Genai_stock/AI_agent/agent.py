from dotenv import load_dotenv
import google.generativeai as genai
import json
import requests
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")

def run_agent(query):
    return f"You asked: {query}"

def get_stock_news(company):
    api_key = os.getenv("STOCK_API_KEY")

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={company}&sortBy=publishedAt&pageSize=5&apiKey={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    news = []

    for article in data.get("articles", []):
        news.append({
            "title": article["title"],
            "source": article["source"]["name"]
        })

    return news

def get_weather(city: str): #weather api calling logic
    url = f"https://wttr.in/{city}?format=%C+%t" #open source weather api, we don't need to create apis for weather
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    
    return "Something went wrong"

def run_command(cmd: str): #executing system commands logic
    result = os.system(cmd)
    return result

available_tools = {
    "get_weather": get_weather, #using get_weather function where we designed our weather api calling logic
    "run_command": run_command, #using run_commad function where we designed our running system commands logic.
    "get_stock_news": get_stock_news
}

SYSTEM_PROMPT = f"""
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You work on start, plan, action, observe mode.

    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.

    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query
    - Don't do all steps one at a time, go one by one, step by step response
    - Never use run_command when a specialized tool exists.
    - For company news, always use get_stock_news.

    Output JSON Format:
    {{
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    Available Tools:
    - "get_weather": Takes a city name as an input and returns the current weather for the city
    - "run_command": Takes linux command as a string and executes the command and returns the output after executing it.
    - "get_stock_news": Takes a company name and returns latest news articles about that company.

    Example:

    User Query: What is the weather of new york?

    Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york" }}
    Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
    Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
    Output: {{ "step": "observe", "output": "12 Degree Cel" }}
    Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}

    User Query: Give me latest news about Tesla

    Output: {{ "step": "plan", "content": "The user wants latest news about Tesla" }}
    Output: {{ "step": "plan", "content": "I should use get_stock_news" }}
    Output: {{ "step": "action", "function": "get_stock_news", "input": "Tesla" }}

"""

#automating the agent (llm+tools(get_weather,run_command))

messages = [
  { "role": "system", "content": SYSTEM_PROMPT }
]
while True:
    query = input("> ")
    messages.append({ "role": "user", "content": query })

    while True:
        prompt = "\n".join(
        [f"{m['role']}: {m['content']}" for m in messages]
        )

        response = model.generate_content(prompt)

        response_text = response.text

        messages.append({
        "role": "assistant",
        "content": response_text
    })

        parsed_response = json.loads(response_text)

        if parsed_response.get("step") == "plan":#output will be of modes:plan,plan, action
            print(f"🧠: {parsed_response.get('content')}")
            continue

        if parsed_response.get("step") == "action":#once i hit action mode
            tool_name = parsed_response.get("function") #will get the respective function 
            tool_input = parsed_response.get("input")

            print(f"🛠️: Calling Tool:{tool_name} with input {tool_input}")

            if available_tools.get(tool_name) != False: #if that function is in available tools
                output = available_tools[tool_name](tool_input) #func() calling
                messages.append({ "role": "user", "content": json.dumps({ "step": "observe", "output": output }) }) #adding that action response in messages
                continue #go to the next mode
        
        if parsed_response.get("step") == "output":
            print(f"🤖: {parsed_response.get('content')}")
            break