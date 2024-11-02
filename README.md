# WiFiHack - WiFi Hacking Simulator
![WiFiHack](https://github.com/user-attachments/assets/63fc751e-6fca-4647-8e95-ed60c691495c)

WiFiHack is a simple brute-force tool to attempt finding WiFi passwords using the PyWiFi library in Python. With a password list, this tool systematically attempts each entry to gain access to the targeted WiFi network.

> **Disclaimer**: This tool is intended solely for educational purposes on personal WiFi networks. Do not use this tool on networks you do not have permission to access.

## 🔥 Features
- **WPA2PSK Authentication**: Supports attempts to connect to networks secured with WPA2.
- **Multithreaded Brute-Force**: Utilizes `ThreadPoolExecutor` for efficient brute-force attempts.
- **Windows Compatibility**: Designed to run on Windows PowerShell; it is not compatible with WSL.
- **Interactive UI**: Uses the `rich` library for a visually appealing, modern interface.

## 📦 Requirements
- **Python** >= 3.9
- Libraries: `pywifi` and `rich`

## ⚙️ Usage
1. **Prepare Network Name and Password List**
Make sure you have the SSID of the target WiFi network and a text file containing a list of potential passwords.
2. **Run the Program**
Open Windows PowerShell, navigate to the project folder, and run:
    ```bash
    python Run.py
    ```
3. **Input Required Data**
When prompted, enter the WiFi network name (SSID) and the path to your password list file.
4. **Monitor the Process**
The brute-force process will start, displaying each attempt. You can stop the process at any time by pressing `CTRL + Z`.

## 📷 Screenshot
![WiFiHack_20241103](https://github.com/user-attachments/assets/b2063168-3068-47e5-a840-988730e410fd)

## 🛠 Troubleshooting
- Open the password file and verify it contains valid passwords, one per line. Remove any blank lines or entries that are too short (under five characters).
- This usually means that the password list provided does not contain the correct password. Try using a more comprehensive or updated password list.
- Ensure that the password file is in the same folder as the program and that the file path is correct. Also, check that the file has read permissions.
- WiFiHack requires direct hardware access, which is limited in WSL. To resolve this, run the tool in *Windows PowerShell* or *Command Prompt* on Windows.
- A slow brute-force process may be due to a large password list or limited system resources. Try a smaller, optimized password list and ensure your system can handle multithreading.
- If the program is interrupted mid-attempt, success and failure counts may be inaccurate. Restart the program and let it run uninterrupted for accurate results.

## ❤️ Support Me
If you'd like to support the development of this project, consider donating:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

Your support is greatly appreciated and helps keep this project alive and improving!

## 🚫 Limitations
This tool **cannot run in WSL (Windows Subsystem for Linux)**. If you attempt to run it in WSL, WiFiHack will display an error message and exit. To run WiFiHack, please use Windows PowerShell or Command Prompt on Windows.

## 📝 Important Note
WiFiHack is designed for testing on your own network. Misuse of this tool on unauthorized networks may be illegal. Please use this tool responsibly.

## 💬 Support
If you encounter any issues or want to contribute, feel free to open an issue or pull request in this repository.

> © 2024 WiFiHack Project - For educational and research purposes only.
