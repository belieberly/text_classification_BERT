from xml.dom.minidom import parse
import re

path_file = open('D:/NJU/final_project/data/example/path.txt', 'r', encoding='utf-8')
total = 0
count = 0
outputf = open('./data_ly/train.tvs','w+',encoding='utf-8')
for path in path_file.readlines():
    if count>100:
        break
    # print(path.strip())
    count = count+1
    domTree = parse('D:/NJU/final_project/data/example/' + path.strip())
    rootNode = domTree.documentElement
    judicial = rootNode.getElementsByTagName("QW")[0]
    judicial_txt = judicial.getAttribute('value')
    # print(judicial_txt)
    outputf.write('judicial'+'\t'+judicial_txt+'\n')
print(count)


