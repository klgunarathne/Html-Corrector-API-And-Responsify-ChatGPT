import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("API_KEY")

def get_token_size(text: str) -> int:
    """
    Given a text prompt, returns the number of tokens in the generated output
    using the OpenAI API.

    Args:
        text: A string representing the text prompt to generate from.

    Returns:
        An integer representing the number of tokens in the generated output.
    """
    # Use OpenAI API to generate output from prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=0,
        echo=True,
        logprobs=1
    )

    # Extract token count from response
    token_count = len(response['choices'][0]['logprobs']['tokens'])

    return token_count