import datetime
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from get_completion_langchain import get_completion_langchain

from helper.cluster_html_and_css import clusterHTMLCSSCode
from helper.write_to_css_file import write_to_css_file
from helper.write_to_html_file import write_to_html_file


load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        html_file = request.files['html']
        css_file = request.files['css']
        
        html_content = html_file.read().decode('utf-8')
        css_content = css_file.read().decode('utf-8')
        
        clusters = clusterHTMLCSSCode(html_content, css_content) if len(clusterHTMLCSSCode(html_content, css_content)) > 0 else []
        
        # get completions
        lstResponse_html = []
        lstResponse_css = []
        cluster_no = 0
        total_execution_time = 0
        print('Total number of clusters', len(clusters))
        for cluster in clusters:
            start_time = datetime.datetime.now()
            ai_response_html, ai_response_css = get_completion_langchain(cluster['html'], cluster['css'])
            lstResponse_html.append(ai_response_html)
            lstResponse_css.append(ai_response_css)
        
            # write_to_html_file(html.unescape(response), 'test.html')
            # write_to_html_file(ai_response_html, 'test.html')
            # write_to_css_file(ai_response_css, 'test.css')
            end_time = datetime.datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            total_execution_time += execution_time
            cluster_no += 1
            print('cluster_no:', cluster_no, 'execution time:', execution_time, 'seconds')
            # time.sleep(30)
            if(len(clusters) == cluster_no):
                break
            
        print('Total execution time:', total_execution_time/60, 'minute(s)')
        print("Generating stoped at", cluster_no)
        # return jsonify(clusters=clusters, noOfClusters=len(clusters))
        return jsonify(html=lstResponse_html, css=lstResponse_css, noOfClusters=len(clusters))


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
