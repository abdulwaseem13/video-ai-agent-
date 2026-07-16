import win32gui
import pygetwindow as gw

windows = [w for w in gw.getAllWindows() if w.title.strip()]

for i, w in enumerate(windows):
    print(f"{i+1}. {w.title}")

choice = int(input("\nSelect: ")) - 1

window = windows[choice]

hwnd = window._hWnd

left, top, right, bottom = win32gui.GetWindowRect(hwnd)

print("\nWindow Rectangle")
print(left, top, right, bottom)
print("Width :", right - left)
print("Height:", bottom - top)