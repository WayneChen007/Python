from linkscan import Spider, VPNCheck
from sendmail import EmailSender
from HTMLTable import HtmlTable, HTMLColor
from configparser import ConfigParser
from threading import Thread
from os.path import join
from sys import path


def get_white_list(file):
    with open(join(path[0], file), 'r') as w:
        return [line.rstrip('\n') for line in w.readlines()]


def table_output(lines):
    title = ''
    status_list = []
    link_list = []
    for line in lines:
        if 'scanning  url= ' in line:
            title = line.split('scanning  url= ')[1]
            status_list.clear()
            link_list.clear()
        elif '> http' in line:
            status = line.split('>', 1)[0].lstrip('<')
            link = line.split('> ', 1)[1].rstrip('\n')
            status_list.append(status)
            link_list.append(link)
        if 'End scanning' in line and title != '' and len(status_list) + len(link_list) != 0:
            yield (title, {'status': status_list, 'link': link_list, 'check': ' '})


def lc_run(_url):
    """t1: link thread
       t2: image thread"""
    s = Spider(_url)
    s.white_list = get_white_list('清单/whitelist.txt')   # white list override
    a_tags = s.get_tags('a')
    img_tags = s.get_tags('img')
    t1 = Thread(target=s.get_links, args=[a_tags, 'href', ], name='href')
    t2 = Thread(target=s.get_links, args=[img_tags, 'src', ], name='src')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    s.exit_browser()


if __name__ == '__main__':
    cl = ConfigParser()  # for CheckList

    CheckList_path = join(path[0], '清单/CheckList.txt')

    cl.read(CheckList_path)
    for section in cl.sections():
        url = cl[section]['url']
        lc_run(url)
    print('link search job done')

    v = VPNCheck()
    logs = v.yield_from_log()   # yield from lines
    html_table = ''
    for i in table_output(logs):
        if i is None:
            continue
        ht = HtmlTable(i[0])
        ht.set_title_style(20, HTMLColor.OrangeRed)
        ht.set_table_style(width=1000, height=20, align='middle')
        table = ht.table_by_column(i[1], diff_width={'status': 200, 'link': 600, 'check': 200})
        html_table += table

    email = EmailSender(html_table)
    email.send()
    print('Email has been sent')
