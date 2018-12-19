import requests
import sys

def test_endpoint(host_address, dict={'key':"value"}):
    r = requests.post(host_address, data = dict)
    return r

if __name__ =="__main__":
    if(len(sys.argv)!=2):
        print("Input Not Formatted")
    else:
        r=test_endpoint(sys.argv[1])
        print(r.status_code)
        if(r.status_code==200):
            print("success:")
            print(r.content)
            #For Binary Response Content
            # print(r.json()) For JSON Response Content
