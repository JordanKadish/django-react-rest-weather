'''
Hacky mess file, just writing this for quick and dirty informal testing.
Pro tip: DO NOT DO THIS, use Postman or other friendly clients in
a "real world setting" :)
'''

import requests


def html_weather_main() -> None:
    '''prints html response from http://127.0.0.1:8000/weather/
    '''
    weather_html_url = 'http://127.0.0.1:8000/weather/'
    
    resp = requests.get(weather_html_url)
    print(resp.text)

def json_weather_main():
    '''prints the dict received from weather's json endpoint
    '''
    json_endpoint = 'http://127.0.0.1:8000/weather/json'

    resp = requests.get(json_endpoint)

    print(resp.status_code)
    print(resp.json())

if __name__=='__main__':
    # TODO: implement LOGGER
    html_weather_main()
    json_weather_main()