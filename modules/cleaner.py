import winreg
import subprocess
from InquirerPy import inquirer

def get_installed_apps():
    keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    apps = []
    for root in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        for key in keys:
            try:
                with winreg.OpenKey(root, key) as k:
                    for i in range(winreg.QueryInfoKey(k)[0]):
                        try:
                            subkey = winreg.EnumKey(k, i)
                            with winreg.OpenKey(k, subkey) as sk:
                                name = winreg.QueryValueEx(sk, "DisplayName")[0]
                                uninstall_cmd = winreg.QueryValueEx(sk, "UninstallString")[0]
                                apps.append({"name": name, "cmd": uninstall_cmd})
                        except:
                            continue
            except:
                continue
    return apps

def uninstall_apps():
    apps = get_installed_apps()
    if not apps:
        print("⚠️ Không tìm thấy ứng dụng nào.")
        return

    selected = inquirer.checkbox(
        message="Chọn ứng dụng để gỡ:",
        choices=[{"name": app["name"], "value": app["cmd"]} for app in apps]
    ).execute()

    for cmd in selected:
        print(f"🚮 Gỡ bằng lệnh: {cmd}")
        subprocess.run(cmd, shell=True)
