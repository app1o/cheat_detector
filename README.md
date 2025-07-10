# Cheat Detector 🧑‍💻

A lightweight GUI application that monitors running processes and detects specified applications from a blacklist. Perfect for educational environments, parental controls, or system monitoring.

## Features

- **Real-time Process Monitoring**: Continuously scans running processes every second
- **Customizable Blacklist**: Uses a CSV file to define which applications to detect
- **User-friendly GUI**: Clean interface built with CustomTkinter
- **Process Termination**: Ability to terminate detected processes
- **Live Logging**: Real-time display of detected applications


## Requirements

- Python 3.7+
- Required packages:
  ```
  psutil
  customtkinter
  tkinter (usually comes with Python)
  ```

## Installation

### Option 1: Ready-to-Use Executable (Recommended)

**🚀 Quick Start**: A pre-built executable is available for immediate use!

1. Go to the `app` folder in this repository
2. Download the ZIP file containing the executable
3. Extract the ZIP file to your desired location
4. The executable comes with a sample `cheat.csv` file
5. Run the executable directly - no Python installation required!

### Option 2: Run from Source

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/cheat-detector.git
   cd cheat-detector
   ```

2. Install required dependencies:
   ```bash
   pip install psutil customtkinter
   ```

3. Create a `cheat.csv` file in the same directory as the script with the application names you want to monitor (one per line):
   ```
   notepad.exe
   calculator.exe
   chrome.exe
   discord.exe
   ```

## Usage

### For Executable Version:
1. **Download**: Get the ZIP file from the `app` folder
2. **Extract**: Unzip to your preferred location
3. **Run**: Double-click the executable file
4. **Configure**: Edit the included `cheat.csv` file to customize your blacklist
5. **Start Monitoring**: Click the "Start" button to begin process monitoring

### For Source Code Version:
1. **Setup**: Ensure `cheat.csv` exists in the same directory as the script
2. **Run the application**:
   ```bash
   python cheat_detector.py
   ```
3. **Start Monitoring**: Click the "Start" button to begin process monitoring
4. **Stop Monitoring**: Click the "Stop" button to pause monitoring
5. **Terminate Processes**: Click the "Terminate" button to close all detected applications

## Configuration

### cheat.csv Format

The `cheat.csv` file should contain one application name per line. Use the exact process name as it appears in the system:

```
notepad.exe
calc.exe
chrome.exe
firefox.exe
discord.exe
steam.exe
```

**Note**: Application names are case-sensitive and should match the exact process name.

## How It Works

1. The application reads the blacklist from `cheat.csv`
2. Every second, it scans all running processes using `psutil`
3. If any process matches the blacklist, it's logged in the interface
4. Users can terminate detected processes with the "Terminate" button

## Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed cheat_detector.py
```

Make sure to place `cheat.csv` in the same directory as the generated executable.

## Important Notes

- **Administrator Privileges**: Some processes may require administrator privileges to terminate
- **System Processes**: Be cautious when adding system processes to the blacklist
- **Performance**: The application scans processes every second, which may have minimal system impact
- **Security**: This tool is for monitoring purposes; ensure you have proper authorization before monitoring systems

## Troubleshooting

### Common Issues

1. **"cheat.csv not found" error**:
   - Ensure `cheat.csv` is in the same directory as the script
   - Check file permissions

2. **Cannot terminate processes**:
   - Run the application as administrator
   - Some system processes cannot be terminated

3. **Application not detecting processes**:
   - Verify process names in `cheat.csv` are exact matches
   - Check if processes are running under different user accounts

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is intended for legitimate monitoring purposes only. Users are responsible for ensuring they have proper authorization before monitoring any system or processes. The developers are not responsible for any misuse of this software.

## Support

If you encounter any issues or have questions:
- Create an issue on GitHub
- Check the troubleshooting section above
- Ensure all requirements are properly installed

---

**⚠️ Legal Notice**: Only use this software on systems you own or have explicit permission to monitor. Unauthorized monitoring of computer systems may violate local laws and regulations.
