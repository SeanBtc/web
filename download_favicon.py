import requests
import os

# 确保static目录存在
static_dir = os.path.join(os.path.dirname(__file__), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# 下载favicon
url = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=professional%20trading%20bot%20icon%20with%20chart%20and%20dollar%20sign%2C%20minimalist%2C%20blue%20color%2C%20transparent%20background%2C%20favicon%20size&image_size=square"
save_path = os.path.join(static_dir, 'favicon.ico')

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Favicon downloaded successfully to {save_path}")
except Exception as e:
    print(f"Error downloading favicon: {e}")
