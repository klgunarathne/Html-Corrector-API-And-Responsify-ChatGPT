import re

def extract_css(html_code, css_file):
    # Read CSS file
    with open(css_file, 'r') as f:
        css_data = f.read()

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



html_code = '<div class=\"\"><div class=\"header-logo-topbar-left-1\"><img src=\"image/Screenshot_334.png\"/></div><p class=\"header-logo-text-topbar-left-2\">Cash App</p><div class=\"header-logo-topbar-middle-3\"><img src=\"image/Screenshot_339-removebg-preview.png\"/></div><p class=\"header-button-topbar-left-4\">LOG IN</p></div>'
css_file = './testing_sites/1. Cash App/css/style.css'

extracted_css = extract_css(html_code, css_file)

print(extracted_css)
