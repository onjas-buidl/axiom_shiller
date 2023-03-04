import requests
import tqdm
import json
# Set the URL for the API endpoint
url = "https://goerli.infura.io/v3/PRIVATE_KEY"
headers = {"Content-Type": "application/json"}

l = []
for bn in tqdm.tqdm(range(8591360, 8591487+1)):
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex(bn).upper(), False],
        "id": 1
    }
    response = requests.post(url, headers=headers, json=data)
    l.append(json.loads(response.text)['result']['hash'])


# Open a file for writing
with open('my_listasdfasdf.txt', 'w') as f:
    # Iterate over the list and write each item to a new line in the file
    for item in l:
        f.write("%s\n" % item)
