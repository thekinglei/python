#coding=utf-8
'''
用户每次分类后，将信息更新到elasticsearch
'''
import json
import requests
import time
SERVER_IP="192.168.1.1"

def insert_into_ela(objid):
    ipaddress = "192.168.1.1"
    entity = {"id":objid}
    content = ela_excute_request("http://" + ipaddress + "/admin/test",
                             'post', data=entity)
 
    resp_obj = json.loads(content)
    #print resp_obj
    #res_code = resp_obj.get('code')
def ela_excute_request(req_url, type='get', data=None):
    retry_num = 3
    html = ''
    headers = {'Content-type': 'application/json;charset=UTF-8'}
    while retry_num:
        try:
            if 'get' in type:
                resp = requests.get(req_url, headers=headers, timeout=30)
            elif 'post' in type:
                resp = requests.post(req_url, headers=headers, data=json.dumps(data), timeout=100)
            print('-----' + str(resp.status_code) + '------')
            if resp.status_code != 200:
                time.sleep(3)
            if resp.status_code == 200:
                html = resp.text
                break
            elif resp.status_code == 404:
                print('resp_status ' + str(resp.status_code))
                return None
        except Exception as e:
            print(e)
            time.sleep(60)
    return html
if __name__ == "__main__":
    print "test"
