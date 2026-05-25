# Cathook

Simple Python webhook sender with file upload support.

Cathook is a lightweight terminal-based tool that allows sending text messages or files directly to a webhook URL.

## Features

- Send text messages to a webhook
- Upload files automatically
- Automatic file detection
- Drag and drop file support
- Minimal terminal interface
- Simple installation
- Lightweight and fast

## Requirements

- Windows
- Python 3.8+
- requests

## Platform Support

Cathook is designed for **Windows only**.

It uses Windows-dependent behavior and was intentionally kept Windows-only because cross-platform support was not implemented.

If you want to run it on another platform, you will need to use the executable version through compatibility tools such as Wine.

## Installation

### Automatic

Run:

```bat
install.bat
```

### Manual

Install dependencies:

```bash
pip install requests
```

## Run

```bash
python main.py
```

You will be prompted to enter your webhook URL:

```text
webhook >
```

Example:

```text
https://discord.com/api/webhooks/...
```

## Usage

### Send a message

Type any text and press Enter.

```text
hello
```

### Upload a file

You can upload a file by simply dragging and dropping it into the command prompt window, then pressing Enter.

You can also paste the file path manually:

```text
C:\Users\User\Desktop\image.png
```

Cathook automatically detects the file and uploads it.

### Exit

Type:

```text
/exit
```

or

```text
/quit
```

## Project Structure

```text
cathook/
├── main.py
├── install.bat
└── README.md
```

## Included Functions

- clear
- is_file
- send_text
- send_file
- ui
- main

## Error Handling

If an operation fails:

```text
[failed]
```

## Notes

- Invalid file paths are treated as text
- Requires an active internet connection
- Windows command prompt recommended

## License

MIT
