from bs4 import BeautifulSoup

soup = lambda src: BeautifulSoup(src, 'html.parser')
domain = lambda path='', dom='https://www.kuysocial.com/': path if dom in path else dom + path
save = lambda x: open('/sdcard/x.htm', 'w').write(str(x))
