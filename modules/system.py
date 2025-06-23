import psutil
from InquirerPy import inquirer

BLACKLIST = [
    "RuntimeBroker.exe", "SearchIndexer.exe", "YourPhone.exe",
    "Cortana.exe", "XboxAppServices.exe", "OneDrive.exe"
]

def kill_useless_tasks():
    procs = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in BLACKLIST:
            procs.append(proc)

    if not procs:
        print("✅ Không có tiến trình rác đang chạy.")
        return

    selected = inquirer.checkbox(
        message="Chọn tiến trình rác muốn tắt:",
        choices=[f"{p.info['name']} (PID: {p.info['pid']})" for p in procs]
    ).execute()

    for item in selected:
        pid = int(item.split("PID:")[1].split(")")[0])
        try:
            psutil.Process(pid).terminate()
            print(f"🗑️ Đã tắt: PID {pid}")
        except Exception as e:
            print(f"❌ Không tắt được {pid}: {e}")
