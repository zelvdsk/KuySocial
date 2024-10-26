import re
from .other import domain, save

class Tools:
    def __init__(self, ses) -> None:
        self.ses = ses

    # Error
    def upload(self, file: list[bytes], type: str, handle: str=None, blur: bool= False) -> dict:
        secret = re.search(r'signout/\?cache\=(.*?)"', self.ses.get(domain()).text).group(1)

        headers = {"Accept": "application/json, text/javascript, */*; q=0.01","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryJ7n9LMz12qRAUPjg","Origin": "https://www.kuysocial.com","Referer": "https://www.kuysocial.com/","sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="81", "Google Chrome";v="81"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": '"Ubuntu"',"Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/14.04.6 Chrome/81.0.3990.0 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        data = {'blur': str(blur), 'handle': handle, 'multiple': 'true' if len(file) > 1 else 'false', 'secret': secret, 'type': type}
        print(data)
        files = {'file': file}

        output = self.ses.post(domain('includes/ajax/data/upload.php'), data=data, files=files, headers=headers).json()
        print(output)

