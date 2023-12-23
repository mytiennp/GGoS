import os

file_path = "promos.txt"

try:
    os.remove(file_path)
    print(f"File '{file_path}' đã được xóa thành công.")
except FileNotFoundError:
    print(f"File '{file_path}' không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra khi xóa file: {e}")
