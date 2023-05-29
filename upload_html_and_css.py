import os
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import re
from dotenv import load_dotenv
import json
from get_completion import getCompletion, getCompletionChat
import html

from helper.clustoer_html_code import clusterHTMLCode
from helper.write_to_html_file import write_to_html_file

load_dotenv()

app = Flask(__name__)

def get_elements_list(text):
    # Convert text to dictionary
    data = json.loads(text.replace("'", "\""))

    # Get elements list
    elements = data['elements']

    # Return elements list
    return elements


@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        html_file = request.files['html']
        css_file = request.files['css']
        
        html_content = html_file.read().decode('utf-8')
        css_content = css_file.read().decode('utf-8')
        
        # Parse HTML and extract body tag
        soup = BeautifulSoup(html_content, 'html.parser')
        
        clusters = clusterHTMLCode(html_content, css_content) if len(clusterHTMLCode(html_content, css_content)) > 0 else []
        
        # Convert the Tag object to a string before returning in JSON response
        clusters_str = [str(c) for c in clusters]
        
        # get completions
        lstResponse = []
        for cluster in clusters:
            response = getCompletionChat(cluster, modelName=os.getenv("model_id_davinchi_003"))
            lstResponse.append(response)
        
            # write_to_html_file(html.unescape(response), 'test.html')
            write_to_html_file(response, 'test.html')
            break
        
        # return jsonify(clusters=clusters_str, noOfClusters=len(clusters_str))
        return jsonify(response=lstResponse)

if __name__ == '__main__':
    app.run(debug=True)
