import requests
from requests_html import HTMLSession
import os

def check_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_proxies(api_url, timeout=10000):
    try:
        response = requests.get(api_url, params={"request": "getproxies", "protocol": "http", "timeout": timeout, "country": "all", "ssl": "all", "anonymity": "all"})
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Không thể lấy proxy từ API: {e}")
        return []

def save_proxies_to_file(proxies, file_path):
    with open(file_path, "w") as file:
        for proxy in proxies:
            file.write(proxy + "\n")

def clean_and_update_proxies(file_path):
    # Đọc danh sách proxy từ file
    with open(file_path, "r") as file:
        old_proxies = file.read().splitlines()

    # Kiểm tra và lọc proxy còn hoạt động
    working_proxies = [proxy for proxy in old_proxies if check_proxy(proxy)]

    # Ghi danh sách proxy hoạt động vào file
    save_proxies_to_file(working_proxies, file_path)

    # In thông báo
    print(f"Đã cập nhật và lưu {len(working_proxies)} proxy vào file {file_path}.")

if __name__ == "__main__":
    api_url = "https://api.proxyscrape.com/v2/"
    proxies_file = "proxies.txt"
    timeout = 10000

    # Lấy danh sách proxy mới từ API và lưu vào proxies.txt
    new_proxies = get_proxies(api_url, timeout)
    save_proxies_to_file(new_proxies, proxies_file)

    # Kiểm tra và cập nhật proxies.txt
    clean_and_update_proxies(proxies_file)

    print(f"Đã lấy và lưu {len(new_proxies)} proxy mới vào file {proxies_file}.")

    # Tiếp tục các bước cần thiết với proxies.txt (ví dụ: sử dụng proxies trong các yêu cầu HTTP)
    # ...

# Chú ý: Bạn có thể thêm vào đoạn mã để sử dụng danh sách proxy (new_proxies hoặc working_proxies) trong các yêu cầu HTTP của bạn.
