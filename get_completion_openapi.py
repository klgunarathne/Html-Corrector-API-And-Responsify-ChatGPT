import os
from dotenv import load_dotenv
import openai

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

openai.api_key = os.getenv("API_KEY")

def get_completion_openai(htmlTags, css):
    
    template1 = f"""Turn the HTML code below from having no parent-child structure to having the correct parent-child structure. Provide only HTML code. {htmlTags}"""
    template2 = f"""Given CSS are related to above HTML Gnerated code, Turn the CSS to create a responsive view by removing absolute positioning. Provide only CSS code. {css}"""

    def chat_with_gpt(messages):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.9,
        )
        return response.choices[0].message.content

    messages = [{"role": "system", "content": "You are a helpful assistant for generating HTML and CSS code."}]

    # user_message = input("User: ")
    messages.append({"role": "user", "content": template1})
    ai_response_html = chat_with_gpt(messages)
    messages.append({"role": "assistant", "content": ai_response_html})

    messages.append({"role": "user", "content": template2})
    ai_response_css = chat_with_gpt(messages)
    messages.append({"role": "assistant", "content": ai_response_css})
    
    return ai_response_html, ai_response_css