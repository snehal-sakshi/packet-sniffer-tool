# packet-sniffer-tool
Step-by-Step Guide to Run the Code on Windows
1. Install Python:
Ensure you have Python installed on your system. You can download it from Python's official website. During installation, make sure to check the box that says "Add Python to PATH".

2. Create a Python Script:
You can use Notepad or any text editor to create a Python script.

Open Notepad.
Copy the provided code into Notepad.
Save the file with a .py extension, for example, sniffer.py.
3. Open Command Prompt (CMD) as Administrator:
Since sniffing network traffic requires elevated privileges, you'll need to run the Command Prompt with Administrator privileges.

Press Win + S and search for Command Prompt.
Right-click Command Prompt and select Run as administrator.
4. Run the Python Script:
In the Command Prompt, navigate to the directory where you saved your sniffer.py script. For example, if you saved the script in C:\Users\YourName\Documents, use the following command to navigate there:
bash
Copy code
cd C:\Users\YourName\Documents
Once you're in the correct directory, run the script by typing:
bash
Copy code
python sniffer.py
5. Confirm Output:
The script should start running, and you will see network packet data printed in the Command Prompt window.

Notes:
If you're running Windows, Administrator privileges are required for raw socket operations, which is why running the Command Prompt as an administrator is essential.
The network sniffer script will capture all packets, including any packets sent over your local network. You may need to configure the network interface in promiscuous mode depending on your setup, but on Windows, this is managed automatically.
