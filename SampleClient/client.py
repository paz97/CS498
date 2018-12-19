import requests
import sys
import json

def test_post_endpoint(host_address, dict={
    'sensor_id':1,
    'seats_taken':2,
    'seats_empty':3,
    'seats_total':5
}):
    print(dict)
    r = requests.post(host_address, json=dict)
    return r

def test_get_endpoint(host_address, sensor_id=1):
    r = requests.get(host_address,params={"sensor_id":sensor_id})
    return r

if __name__ =="__main__":
    if(len(sys.argv)!=2):
        print("Input Not Formatted")
    else:
        r=test_post_endpoint(sys.argv[1])
        print(r.status_code)
        if(r.status_code==200):
            print("success:")
            print(r.content)
            #For Binary Response Content
            # print(r.json()) For JSON Response Content
        r=test_get_endpoint(sys.argv[1])

        print(r.status_code)
        if(r.status_code==200):
            print("success:")
            print(json.loads(r.content)["seats_empty"])
