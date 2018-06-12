#!/usr/bin/env python3
# -*- coding:utf-8 -*-
html_doc='''
...
'''

# 不同 builder之间的差异
from bs4 import BeautifulSoup
# text = '<a><b />123</a>'
#企业用lxml更多一点，更有效率
# soup_test = BeautifulSoup(text, 'lxml') # 会补全 html，body和p
# print('lxml:')
# print(soup_test)
#测试用html.parser更多一点
# soup_test = BeautifulSoup(text, 'html.parser') # 会补全 p
# print('html.parser:')
# print(soup_test)
# soup_test = BeautifulSoup(text, 'html5')  # 会补全 html，head，body和p
# print('html5:')
# print(soup_test)
# soup_test = BeautifulSoup(text, 'xml')  # 会加xml头，忽略错误的标签
# print('xml:')
# print(soup_test)


# 用法
# soup = BeautifulSoup(html_doc, 'lxml')
#
# # print(soup.prettify())
#
# print(soup.title) # 标签，包括标签本身
# print(soup.title.name) # 标签的名字
# s = soup.title.string
# print(soup.title.string) # 标签的内容, NavigableString 对象
# print(soup.title.text) # 标签的内容， str 对象
#
# print(soup.meta) # 标签
# print(soup.meta['charset']) # 标签属性
#
# print(soup.meta.parent.name) # 标签的父标签
# print(soup.html.parent.name)
# print(soup.html.parent.parent)
from bs4 import BeautifulSoup

text = '''
<a><b>text1</b><c>text2</c>
<d>text3</d><e e1='100'/><f f1='101'/><></a>
'''
sibling_soup = BeautifulSoup(text, 'lxml')
print(sibling_soup.b.next_sibling) #  兄弟节点
print(sibling_soup.c.previous_sibling) #  兄弟节点
print(sibling_soup.c.next_sibling) #  兄弟节点，是 换行符
print(sibling_soup.d.previous_sibling) #  兄弟节点，是 换行符

print(sibling_soup.a.next_element) #  下一个元素，是 <b>text1</b>
print(sibling_soup.b.next_element) #  下一个元素，是 text1
print(sibling_soup.b.next_element.next_element) #  下一个元素，是 换行符
print(sibling_soup.d.previous_element) #  上一个元素，是 换行符
print(sibling_soup.f.previous_element) #  上一个元素，是 <e e1='100'/>
print('结束')

soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.find_all('meta')) # 查找所有
# print(soup.find_all('meta', limit=2)) # 查找所有
# print(soup.find('meta', {'charset': 'UTF-8'})) # 查找特定的一个标签，其实也是调用的find_all，不过会在取到一个值后返回
# print(soup.find(id="seajsnode")) # 根据id查找特定的一个标签


# print(soup.find('p', {"text": '测试的连接'}))
# print(soup.find('p', text='测试的连接')) # 根据标签内容查找特定的一个标签，不能仅仅有标签内容一个参数
#
# meta = soup.find('meta', {'name': 'robots'})
# print(meta)
# print(meta.find_next_sibling('meta')) # 查找下个符合条件的兄弟节点
# print(meta.find_next_siblings('meta')) # 查找所有符合条件的兄弟节点
# #
# print(meta.find_next_sibling('a')) # 查找下个符合条件的兄弟节点
# print(meta.find_next('a')) # 查找下个符合条件的节点
# print(meta.find_all_next('a')) # 查找所有符合条件的节点

# print(soup.find('body').get_text()) # 获取所有文本
# print(soup.find('body').get_text('|')) # 获取所有文本，| 是分隔符

'''
    标签对象一样可以使用所有方法
'''
# body = soup.find('body')
# print(body.find('div'))

'''
    标签对象，可以和字符串一样编码和解码
'''
# markup = "<b>\N{SNOWMAN}</b>"
# snowman_soup = BeautifulSoup(markup, 'html.parser')
# tag = snowman_soup.b
# print(tag)
# print(tag.encode("utf-8"))
# print(tag.encode("utf-8").decode('utf-8'))
# print(tag.encode("iso-8859-1"))
# print(tag.encode("iso-8859-1").decode('iso-8859-1'))
# print(tag.encode("gbk"))
# print(tag.encode("gbk").decode('gbk'))

'''
    css选择器
'''
print(soup.select("title"))  # 标签名
print(soup.select("html head title"))  # 逐层查找
print(soup.select("body a"))  # 不逐层查找

print(soup.select("body > a"))  # >  子节点
print(len(soup.select("body > div")))  # >  子节点
print(soup.select("body > div"))  # >  子节点

print(soup.select("input ~ p"))  # >  兄弟节点

print(soup.select("#pin-nav"))  # 通过id
print(soup.select("div#pin-nav"))  # 通过id

print(soup.select('.share-img'))  # 通过class

print(soup.select('meta[charset="gb2312"]'))

"""
    xpath :  xpath("//p[@attr1=""]/div/a").text

    获取 太初 这个小说名字：
    css选择器：soup.select('div.book-info > h1 > em')[0].text

    xpath： /html/body/div[2]/div[6]/div[1]/div[2]/h1/em

    正则表达式： re.search(r'class="book-info ".*?<em>(.*?)</em>', html_doc, re.S).group(1)

    bs4： soup.find('div', {"class": "book-info "}).h1.em.text
"""


#---------------------爬取起点小说名，作者，描述，月票数，打赏人数和所有的章节的名称----------
"""
    要求：
    获取上面文本中的，小说名，作者，描述，月票数，打赏人数和所有的章节的名称
"""

# xpath
# from lxml import etree
#
# # 初始化
# tree = etree.HTML(html_doc)
#
# book_name = tree.xpath('//div[@class="book-info "]/h1/em')[0].text
# # auth = tree.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/h1/span/a')  # 一旦在网页中复制xpath，是从/html开始的，不要使用
# auth = tree.xpath('//div[@class="book-info "]/h1/span/a')[0].text
# des = tree.xpath('//div[@class="book-info "]/p[2]')[0].text
# month_tickets = tree.xpath('//div[@class="ticket month-ticket"]/p[2]/i')[0].text
# reward_num = tree.xpath('//*[@id="rewardNum"]')[0].text
#
#
# normal_reader = tree.xpath('//a[@data-eid="qd_G55" and starts-with(@href, "//read.qidian.com/chapter/SHqBD2nUPpb-JlVC31J8Aw2/")]')
# print('普通章节的长度：', len(normal_reader))
#
# vip_reader = tree.xpath('//a[@data-eid="qd_G55" and starts-with(@href, "//vipreader.qidian.com/chapter/1010399782/")]')
# print('vip章节的长度：', len(vip_reader))
#
#
# all_reader = tree.xpath('//ul[@class="cf"]/li/a')
# print('所有章节的长度：', len(all_reader))

# all_url = [item.get('href') for item in all_reader]


# bs4
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')

div_book_info = soup.find('div', {'class': 'book-info '})
book_name = div_book_info.h1.em.text
auth = div_book_info.h1.span.a.text
des = div_book_info.find('p', {'class': 'intro'}).text
# des = div_book_info.p.find_next_sibling().text
month_tickets = soup.find(id="monthCount").text
reward_num = soup.find(id="rewardNum").text
print(reward_num)

# normal_reader = tree.xpath('//a[@data-eid="qd_G55" and starts-with(@href, "//read.qidian.com/chapter/SHqBD2nUPpb-JlVC31J8Aw2/")]')
# print('普通章节的长度：', len(normal_reader))
all_reader = soup.find_all('a', {'data-eid': 'qd_G55'})
print('所有章节：', len(all_reader))