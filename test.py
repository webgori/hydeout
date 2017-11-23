import re

p = re.compile('(\{%\sasset_img\s\S+.jpg\s%\})')
p2 = re.compile('\S+.jpg')

with open('2014-08-16-쿄토.md', 'rt', encoding='UTF8') as f:
    content = f.readlines()

f = open("2014-08-16-쿄토-.md", 'w', encoding='UTF8')
for line in content:
    line2 = line
    m = p.findall(line)
    if m:
        for i, tag in enumerate(m):
            m2 = p2.search(tag)
            file_name = m2.group()
            replace_tag = "![](/assets/posts/쿄토/" + file_name + ")"
            if i > 0:
                replace_tag = "\n" + replace_tag
            line2 = line2.replace(tag, replace_tag)
    #print(line2.replace("\n\n", ""))
    f.write(line2)
f.close()