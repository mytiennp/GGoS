import requests
import json
import time

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}

data = {
    'partnerUserId': '8a3f4ecd45aa7d192708162f4ae87a085a97f00cf4148615f32d3f8d070e8779',
}
#17342b93e44c67952c9ef225c1ecd5fc94e5c06b70fcbc14d4f02ee6a091edb0
#another partneruserid 

response = requests.post(url, headers=headers, json=data)

print('Generating... Check file promos.txt')
print('Gen Code By Tak')
while True:
    try:
        response.raise_for_status()
        json_result = response.json()
        token_value = json_result.get('token', '')
        if token_value:
            final_result = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}\n'
            
            # Save the final result to a text file
            with open('promos.txt', 'a') as file:
                file.write(final_result)
        else:
            print('OperaGX Fix It! FUCK YOU')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        print(f'DitMeMay Error Cai Dau Buoi!')
        print(f'Doi 10 Giay Di Thang Dien!')
        time.sleep(10)