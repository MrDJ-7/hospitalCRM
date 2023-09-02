# import sys
from xml.etree import ElementTree as ET

class UserView:
    def MakeHtml(self, listUsers, name):
        html = ET.Element('html')
        body = ET.Element('body')
        html.append(body)
        div = ET.Element('div', attrib={'class': 'foo'})
        body.append(div)
        span = ET.Element('span', attrib={'class': 'bar'})
        div.append(span)
        # span.text = "All users\n"
        table = ET.Element('table')
        for i in range(len(listUsers)):
            tr = ET.Element('tr')
            td = ET.Element('td')
            td.text = str(i+1) + " " + listUsers[i]
            tr.append(td)
            table.append(tr)
        body.append(table)
        name += ".html"
        with open(name, 'wb') as f:
            tree = ET.ElementTree(html)
            # print(tree)
            tree.write(f, encoding='utf-8', method='html')

