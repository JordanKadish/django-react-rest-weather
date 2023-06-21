import requests

# just a simple notes file on requests lib

def html_httpbin_main() -> None:
    '''prints html response from httpbin
    '''
    source_doc_endpoint = 'https://httpbin.org/'
    # get response based off of HTTP request
    resp = requests.get(source_doc_endpoint)

    # simple print of raw text response
    print(resp.text)

def json_httpbin_main():
    '''prints the dict received from httpbin's echo endpoint
    '''
    echo_endpoint = 'https://httpbin.org/anything'
    # django_test = 'http://localhost:8000/' 

    # this response is an echo of the request being made.
    # Let's us see what requests is sending out from our host
    echoed_resp = requests.get(
            echo_endpoint,
            # we can send our own json data packet to the server
            # we could instead use data= keyword to send this as form data
            json={'query':'Hello World'}
        )

    # printing the status code
    print(echoed_resp.status_code)
    # printing the json dict
    print(echoed_resp.json())

if __name__=='__main__':
    html_httpbin_main()
    json_httpbin_main()