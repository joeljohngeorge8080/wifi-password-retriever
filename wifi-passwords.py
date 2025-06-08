import subprocess

# This gets the list of saved Wi-Fi names
def get_wifi_names():
    result = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
    lines = result.split('\n')
    names = []
    for line in lines:
        if "All User Profile" in line:
            # The Wi-Fi name is after the colon
            name = line.split(":")[1].strip()
            names.append(name)
    return names

# This gets the password for one Wi-Fi name
def get_wifi_password(name):
    result = subprocess.check_output(f'netsh wlan show profile "{name}" key=clear', shell=True, text=True)
    lines = result.split('\n')
    for line in lines:
        if "Key Content" in line:
            # The password is after the colon
            password = line.split(":")[1].strip()
            return password
    return "No password found"

# Main part: get names and show passwords
wifi_names = get_wifi_names()

for wifi in wifi_names:
    password = get_wifi_password(wifi)
    print("Wi-Fi Name:", wifi)
    print("Password:", password)
    print("----------------------------")
