import requests

notify_url = "https://notify-api.line.me/api/notify"

def send_line(token: str, message: str):      
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': message }          
    r = requests.post(notify_url, headers = headers, data = data)    
    if r.status_code != 200:
        print(r.status_code)