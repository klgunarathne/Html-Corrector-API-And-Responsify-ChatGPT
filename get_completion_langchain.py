import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

chat = ChatOpenAI(temperature=1.0, openai_api_key=os.getenv("API_KEY"), model_name='gpt-3.5-turbo')

def chat_with_gpt(messages):
    response = chat(messages)
    return response.content

def get_completion_langchain(htmlTags, css):
    template1 = f"""Turn the HTML code below from having no parent-child structure to having the correct parent-child structure. Provide only HTML code without any other text. {htmlTags}"""
    template2 = f"""Given CSS are related to above HTML Gnerated code, Turn the CSS to create a responsive view by removing absolute positioning. Provide only CSS code without any other text. {css}"""
    
    messages = [SystemMessage(content="You are a helpful assistant for generating HTML and CSS code.")]

    messages.append(HumanMessage(content=template1))
    ai_response_html = chat_with_gpt(messages)
    messages.append(AIMessage(content= ai_response_html))

    messages.append(HumanMessage(content= template2))
    ai_response_css = chat_with_gpt(messages)
    messages.append(AIMessage(content= ai_response_css))

    return ai_response_html, ai_response_css


# html_tags = "<div><p>Hello, world!</p></div>"
# css = "div { position: absolute; }"
# for i in range(10):
#     html_result, css_result = get_completion_langchain(html_tags, css)
#     print("Generated HTML:", html_result)
#     print("Generated CSS:", css_result)
#     print("range", i)
