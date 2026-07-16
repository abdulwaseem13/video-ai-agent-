import pygetwindow as gw

windows = []

for window in gw.getAllWindows():
    title = window.title.strip()

    if title:
        windows.append(window)

print("\nOpen Windows:\n")

for i, window in enumerate(windows):
    print(f"{i + 1}. {window.title}")
    