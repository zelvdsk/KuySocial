import requests
from .interactions import Interactions
from .tools import Tools
from .other import domain, save


class Start(Interactions, Tools):
    # Session generator
    # sign using cookie or username and password
    def __init__(self, cookie: str = None, username: str = None, password: str = None) -> None:
        self.ses = requests.session()
        self.ses.headers.update({"Accept": "application/json, text/javascript, */*; q=0.01","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://www.kuysocial.com","Referer": "https://www.kuysocial.com/pujiixwhy","sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="81", "Google Chrome";v="81"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": '"Ubuntu"',"Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/14.04.6 Chrome/81.0.3990.0 Safari/537.36","X-Requested-With": "XMLHttpRequest"})
        
        self.ses.cookies.set('cookie', cookie) if cookie is not None else self.ses.post(domain('includes/ajax/core/signin.php'), data={'username_email': username, 'password': password, 'remember': 'on'})
        self.login_status = True if 'signout' in self.ses.get(domain()).text else False

        # branch
        Interactions.__init__(self, self.ses)
        Tools.__init__(self, self.ses)


