from bs4 import BeautifulSoup
import html
import re

def extract_css(html_code, css_data):
    # Remove comments from CSS data
    css_data = re.sub(r'/\*[\w\W]*?\*/', '', css_data)

    # Extract CSS rules
    css_rules = re.findall(r'\s*([\w\W]+?)\s*\{([\w\W]+?)\}', css_data)

    # Extract HTML selectors
    html_selectors = re.findall(r'class="([^"]+)"', html_code)

    # Extract CSS rules for each HTML selector
    extracted_css = []
    for selector in html_selectors:
        for rule in css_rules:
            if selector in rule[0] and rule[1]:
                extracted_css.append(f"{rule[0]} {{ {rule[1]} }}")

    # Remove empty CSS rules
    extracted_css = [css for css in extracted_css if not re.match(r'^\s*[\w-]+\s*{\s*}\s*$', css)]

    # Return extracted CSS
    return "\n".join(extracted_css)

def clusterHTMLCode(htmlTags, css_data):
    soup = BeautifulSoup(htmlTags, 'html.parser')
    grouped_elements = {}

    for element in soup.find_all():
        class_list = element.get('class')
        if class_list is not None:
            prefix = class_list[0].split("-")[0]
            if prefix not in grouped_elements:
                grouped_elements[prefix] = []
            grouped_elements[prefix].append(element)

    cluster = []
    for prefix, elements in grouped_elements.items():
        group = ''
        for element in elements:
            # group += html.escape(str(element))
            group += str(element)
            
        extracted_css = extract_css(group, css_data)
        group += '\n' + extracted_css
        cluster.append(group)

    return cluster
