import subprocess

def run_windows_defender():
    print("🛡️ Đang kích hoạt quét nhanh bằng Windows Defender...")
    try:
        subprocess.run('powershell.exe Start-MpScan -ScanType QuickScan', shell=True)
        print("✅ Đã chạy Windows Defender quét nhanh.")
    except Exception as e:
        print(f"❌ Lỗi khi quét: {e}")
