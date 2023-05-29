import os
from dotenv import load_dotenv
import openai

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

html = ''
css = ''

# Define the first chain
first_prompt = """
<div class="header-logo-topbar-left">
  <div class="header-logo-topbar-left-1">
    <img src="image/Screenshot_334.png">
  </div>
  <p class="header-logo-text-topbar-left-2">Cash App</p>
</div>
<div class="header-logo-topbar-middle-3">
  <img src="image/Screenshot_339-removebg-preview.png">
</div>
<p class="header-button-topbar-left-4">LOG IN</p>
"""

# Define the second chain
second_prompt = """
    .header-logo-topbar-left-1{
    position: absolute;
    transform: translate(-50%, -50%);
    top: 47px;
    left: 18.5%;
    z-index: 2;
    }
    .header-logo-text-topbar-left-2{
        position: absolute;
        transform: translate(-50%, -50%);
        top: 47px;
        left: 23.5%;
        z-index: 2;
        color: #00d54b;
        font-size: 23px;
        font-weight: 800;
    }
    .header-logo-topbar-middle-3{
        position: absolute;
        transform: translate(-50%, -50%);
        top: 53px;
        left: 50%;
        z-index: 2;
    }
    .header-button-topbar-left-4{
        position: absolute;
        transform: translate(-50%, -50%);
        top: 47px;
        left: 79%;
        z-index: 2;
        color: black;
        background-color: white;
        padding: 12px 40px;
        font-size: 13px;
        font-weight: 800;
        border-radius: 50px;
    }
    """
    
template1 = f"""Turn the HTML code below from having no parent-child structure to having the correct parent-child structure. Provide only HTML code. {first_prompt}"""
template2 = f"""Given CSS are related to above HTML Gnerated code, Turn the CSS to create a responsive view by removing absolute positioning. {second_prompt}"""

openai.api_key = os.getenv("API_KEY")

def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

messages = [{"role": "system", "content": "You are a helpful assistant for generate HTML and CSS code."}]

# user_message = input("User: ")
messages.append({"role": "user", "content": template1})
ai_response = chat_with_gpt(messages)
print(f"AI: {ai_response}")
messages.append({"role": "assistant", "content": ai_response})

messages.append({"role": "user", "content": template2})
ai_response = chat_with_gpt(messages)
print(f"AI: {ai_response}")
messages.append({"role": "assistant", "content": ai_response})