import subprocess
import psutil
from InquirerPy import inquirer

def remove_all_extensions():
    print("🗑️ Gỡ toàn bộ extension VS Code...")
    result = subprocess.run(['code', '--list-extensions'], capture_output=True, text=True)
    for ext in result.stdout.strip().split('\n'):
        subprocess.run(['code', '--uninstall-extension', ext])
        print(f"❌ Gỡ: {ext}")

def remove_themes():
    print("🎨 Gỡ các extension theme...")
    result = subprocess.run(['code', '--list-extensions'], capture_output=True, text=True)
    for ext in result.stdout.strip().split('\n'):
        if "theme" in ext.lower():
            subprocess.run(['code', '--uninstall-extension', ext])
            print(f"❌ Gỡ theme: {ext}")

def selective_kill():
    procs = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        if 'code' in proc.info['name'].lower():
            mem = proc.info['memory_info'].rss / (1024 * 1024)
            procs.append({"name": proc.info['name'], "pid": proc.info['pid'], "mem": mem})

    if not procs:
        print("✅ Không có tiến trình VS Code nào.")
        return

    choices = [
        f"{p['name']} (PID: {p['pid']}) - {p['mem']:.1f}MB" for p in procs
    ]

    selected = inquirer.checkbox(
        message="Chọn tiến trình muốn tắt:",
        choices=choices
    ).execute()

    for item in selected:
        pid = int(item.split("PID:")[1].split(")")[0])
        psutil.Process(pid).terminate()
        print(f"🔪 Đã tắt PID {pid}")
