#Задача 5. Web scraping

import re
import requests


response = requests.get('http://www.columbia.edu/~fdc/sample.html')
subheadings = re.findall(re.compile(r"<h3.*>(.*)</h3>"), response.text)
print(subheadings)
