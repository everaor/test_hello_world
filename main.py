import re
import requests
import json
from bs4 import BeautifulSoup

strweb = 'https://www.ree.es/es'


page = requests.get(strweb)

print(page.status_code)

# print(page.content)
soup = BeautifulSoup(page.content, "html.parser")

data = soup.find(type="application/json")
data = str(data)

data_clean=re.sub("<.*>.",'{',data)
data_clean_1 = re.sub('</script>','',data_clean)
print(data_clean_1)

y = json.loads(data_clean_1)
print(y['customElectricityStatistics']['hoursValue'])
print(y['customElectricityStatistics']['realDemandValue'])
print(y['customElectricityStatistics']['scheduledDemandValue'])
print(y['customElectricityStatistics']['expectedDemandValue'])