import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

html = ""

# template = """
# Please convert the following HTML code into the correct parent-child structure. 
# Currently, the code is missing the necessary hierarchy to properly structure the elements on the page. 
# Your goal is to arrange the elements into a logical hierarchy that reflects their relationship to each other {html} ###. 
# """

# template = """
# Please convert the following HTML code into the correct parent-child structure. Currently, the code is missing the necessary hierarchy to properly structure the elements on the page. Your goal is to arrange the elements into a logical hierarchy that reflects their relationship to each other.
# HTML: {html} ###
# """

template = """
Turn the HTML code below from having no parent-child structure to having the correct parent-child structure. Turn the CSS from using absolute positioning to being responsive
{html}
"""

html_corrector_template = PromptTemplate(
    input_variables=["html"],
    template=template,
)



def getCompletion(htmlTags, modelName):
    # LLMs
    llm = OpenAI(
        temperature=0.7,
        model_name=modelName,
        top_p=1,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["END"]
    )
    
    html_corrector_chain = LLMChain(llm=llm, prompt=html_corrector_template, verbose=True)
    
    response = ""
    print(htmlTags)
    if htmlTags:
        response = html_corrector_chain.run(html=htmlTags)
        
    return response

def getCompletionChat(htmlTags, modelName):
    # LLMs
    chat = ChatOpenAI(
        temperature=0.7,
        model_name=modelName,
        top_p=1,
        n=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    template="You are a helpful assistant that can turn the following HTML code into the correct parent-child structure. And Turn the CSS from using absolute positioning to being responsive."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = HumanMessagePromptTemplate.from_template("Hi")
    example_ai = AIMessagePromptTemplate.from_template(htmlTags)
    human_template=htmlTags
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    
    response = ""
    if htmlTags:
        response = chain.run(html=chat_prompt)
        
    return response
