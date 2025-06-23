import os
import shutil
import psutil

def clean_chrome():
    print("🧹 Dọn Chrome cache & extension...")

    cache_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache")
    ext_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions")

    for path in [cache_path, ext_path]:
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
            print(f"✅ Đã xóa: {path}")
        else:
            print(f"⚠️ Không tìm thấy: {path}")

def check_ram_usage():
    print("🔍 Kiểm tra các tiến trình Chrome:")
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            if 'chrome' in proc.info['name'].lower():
                ram = proc.info['memory_info'].rss / (1024 * 1024)
                print(f" - PID {proc.info['pid']}: {proc.info['name']} dùng {ram:.1f} MB")
        except:
            continue
