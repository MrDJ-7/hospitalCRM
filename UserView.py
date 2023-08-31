# import sys
from xml.etree import ElementTree as ET

class UserView:
    def MakeHtml(self, listUsers):
        html = ET.Element('html')
        body = ET.Element('body')
        html.append(body)
        div = ET.Element('div', attrib={'class': 'foo'})
        body.append(div)
        span = ET.Element('span', attrib={'class': 'bar'})
        div.append(span)
        span.text = "All users\n"
        tr = ET.Element('tr')
        table = ET.Element('table')
        for x in listUsers:
            td = ET.Element('td')
            td.text = x
            tr.append(td)
        table.append(tr)
        body.append(table)
        with open('output.html', 'wb') as f:
            tree = ET.ElementTree(html)
            print(tree)
            tree.write(f, encoding='utf-8', method='html')

