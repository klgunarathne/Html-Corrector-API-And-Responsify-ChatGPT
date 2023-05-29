from bs4 import BeautifulSoup
import re

html = """
<div class="icon-box-img-middle-1"><img src="image/tldr-feature-2.png"></div>
<p class="icon-box-heding-middle-2">Spend</p>
<p class="icon-box-para-middle-3">Design a debit card to match your style.</p>

<div class="icon-box-img-right-1"><img src="image/tldr-feature-3.png"></div>
<p class="icon-box-heding-right-2">Bank</p>
<p class="icon-box-para-right-3">Speed up your direct deposits.1</p>

<div class="icon-box-img-fourth-1"><img src="image/tldr-feature-4.png"></div>
<p class="icon-box-heding-fourth-2">Invest</p>
<p class="icon-box-para-fourth-3">Buy stocks and bitcoin with as little as $1.2</p>

<p class="icon-box-para-bottom-1">Cash App is a financial services platform, not a bank. Banking services are provided by Cash’s Bank Partner(s). Brokerage Services provided by Cash App Investing, LLC, Member FINRA/SIPC, subsidiary of Block, Inc. Bitcoin services provided by Cash App.</p>


<!-- CASH-APP-SECTION-1 -->
<div class="cash-app-main-img-1"><img src="image/image (32).png"></div>
<div class="cash-app-logo-1"><img src="image/Screenshot_337-removebg-preview.png"></div>
<p class="cash-app-logo-text-1">Cash App</p>
<p class="cash-app-content-heading-top-1">Pay anyone,instantly</p>
<p class="cash-app-content-para-bottom-1">Send and receive money anytime, anywhere. It’s fast and free, and a $cashtag is all you need to get started.Pillar</p>


<!-- CASH-APP-SECTION-2 -->

<div class="cash-app-main-img-2"><img src="image/image (33).png"></div>
<div class="cash-app-logo-2"><img src="image/Screenshot_334.png"></div>
<p class="cash-app-logo-text-2">Cash App</p>
<p class="cash-app-content-heading-top-2">Design a debit card to match your style</p>
<p class="cash-app-content-para-bottom-2">Cash card is customizeable,fee-free debit card. Use it everywhere to earn instant discounts on everyday spending.</p>
"""

soup = BeautifulSoup(html, 'html.parser')

grouped_elements = {}

for element in soup.find_all():
    class_list = element.get('class')
    if class_list is not None:
        prefix = class_list[0].split("-")[0]
        if prefix not in grouped_elements:
            grouped_elements[prefix] = []
        grouped_elements[prefix].append(element)

for prefix, elements in grouped_elements.items():
    print(f"Group {prefix}:")
    for element in elements:
        print(element)


# html_content = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
# html_elements = html_content.split('\n\n')
# for group in html_elements:
#     print(group, '\n')
