from InquirerPy import inquirer
from modules import vscode, chrome, cleaner, system, security

def main_menu():
    options = [
        "🧼 Dọn Chrome (Cache, Extension)",
        "🗑️ Gỡ extension VS Code",
        "🎨 Gỡ theme VS Code",
        "🧠 Xem tiến trình VS Code & chọn tắt",
        "🚮 Gỡ app Windows không dùng",
        "🔍 Kiểm tra Chrome ngốn RAM",
        "📛 Quét virus (Windows Defender)",
        "💣 Tắt tiến trình rác (RuntimeBroker, SearchIndexer...)",
        "❌ Thoát"
    ]

    choice = inquirer.select(
        message="👉 Chọn chức năng muốn sử dụng:",
        choices=options
    ).execute()

    if choice == options[0]:
        chrome.clean_chrome()
    elif choice == options[1]:
        vscode.remove_all_extensions()
    elif choice == options[2]:
        vscode.remove_themes()
    elif choice == options[3]:
        vscode.selective_kill()
    elif choice == options[4]:
        cleaner.uninstall_apps()
    elif choice == options[5]:
        chrome.check_ram_usage()
    elif choice == options[6]:
        security.run_windows_defender()
    elif choice == options[7]:
        system.kill_useless_tasks()
    else:
        print("👋 Tạm biệt!")
        exit()

if __name__ == "__main__":
    while True:
        main_menu()
