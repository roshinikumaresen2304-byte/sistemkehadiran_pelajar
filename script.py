import os

html_file = "index.html"

# Semak kewujudan fail HTML
if os.path.exists(html_file):
    print("Fail index.html wujud ✅")

    with open(html_file, "r", encoding="utf-8") as file:
        content = file.read()

        if "alert(" in content:
            print("Fungsi alert() dijumpai ✅")
        else:
            print("Fungsi alert() tidak dijumpai ❌")
else:
    print("Fail index.html tidak wujud ❌")