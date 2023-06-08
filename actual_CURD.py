import re
import requests
import json

endpoint_url = 'https://10.82.2.14:8443'
username = 'ashok'
password = 'India@14356'
def auth_post_request(**kwargs):
    '''This function is used to authenticate the request
    and return the token'''
    cred = {
        "username": kwargs['username'],
        "password": kwargs['password']
    }
    try:
        headers = {
            'content_type': 'application/json',
            'accept': 'application/vnd.ceph.api.v1.0+json'
        }
        url = f'https://10.82.2.14:8443/api'
        # Send the HTTP POST request and receive the response
        response = requests.post(
            url + '/auth', headers=headers, verify=False, data=json.dumps(cred))
    except Exception as e:
        raise Exception(e)
    print("response",response)
    token = response.headers['Set-Cookie']

    '''Return response token'''
    return re.search(r'token=(.*?);', token).group(1)


#print(auth_post_request(username='admin', password='p@ssw0rd'))


#1 GET METHOD

def fetch(endpoint_url):
    # url = f'https://10.82.2.14:8443/api/rgw/bucket'
    token = auth_post_request(username='ashok', password='India@14356')
    print(token)
    new_headers = {
        'Authorization': f'Bearer {token}',
        "accept": 'application/vnd.ceph.api.v1.0+json',
        'Content-Type': 'application/json'
    }

    get_bucket = requests.get(endpoint_url + '/api/rgw/bucket', verify=False, headers=new_headers)
    buckets = json.loads(get_bucket.content)
    print(buckets)
    # return buckets

fetch(endpoint_url)

# 2 POST METHOD

def create_bucket(bucket_name):

        url = f'https://10.82.2.14:8443/api/rgw/bucket'
        token = auth_post_request(username='ashok', password='India@14356')

        headers = {
            'content-type': 'application/json',
            'accept': 'application/vnd.ceph.api.v1.0+json',
            'authorization': 'Bearer ' + token,
        }

        cred = {
           "bucket": bucket_name,
            "uid": "test",
        }

        response = requests.post(url, headers=headers,
                                 verify=False, data=json.dumps(cred))
        return response.json()

print(create_bucket('saurabh1'))



# PUT method

def update_bucket(bucket_name):
    url = f'https://10.82.2.14:8443/api/rgw/bucket/{bucket_name}'
    token = auth_post_request(username='ashok', password='India@14356')
    print(token)

    headers = {
        'content-type': 'application/json',
        'accept': 'application/vnd.ceph.api.v1.0+json',
        'authorization': 'Bearer ' + token,
    }

    cred = {
        "bucket_id": "984cc844-0b1f-40ab-a3d8-d7758f11dd04.11866500.40",
        "uid": "test",
        "versioning_state": 'null',
        "mfa_delete": 'null',
        "mfa_token_serial": 'null',
        "mfa_token_pin": 'null',
        "lock_mode": 'null',
        "lock_retention_period_days": 'null',
        "lock_retention_period_years": 'null',
        "daemon_name": 'null'
    }

    update_bucket = requests.put(url, headers=headers,verify=False, data=json.dumps(cred))
    if update_bucket.status_code == 200:
        print(f"Bucket'{bucket_name}'Updated Successful")
    else:
        print(f"Failed To update Bucket. Error:{update_bucket.text}")
update_bucket('bucket_name')

#print(update_bucket('jay.bucket'))


#4 DELETE METHOD

def delete_bucket(bucket_name,purge_objects,daemon_name):
    url = f'https://10.82.2.14:8443/api/rgw/bucket/{bucket_name}?purge_objects={purge_objects}&daemon_name={daemon_name}'
    token = auth_post_request(username='ashok', password='India@14356')
    print(token)

    headers = {
        'content-type': 'application/json',
        'accept': 'application/vnd.ceph.api.v1.0+json',
        'authorization': 'Bearer ' + token,
    }
    delete_bucket = requests.delete(url, headers=headers, verify=False)
    if delete_bucket.status_code == 204:
        print(f"Bucket'{bucket_name}'Delete Successful !!")
    else:
        print(f"Failed To update Bucket. Error:{delete_bucket.text}")

delete_bucket('bucket_name','purge_objects','daemon_name')

# print(update_bucket('jay.bucket'))