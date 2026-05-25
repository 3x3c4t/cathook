# Cathook

Simple Python webhook sender with file upload support.

Cathook is a lightweight terminal-based tool that allows sending text messages or files directly to a webhook URL.

## Features

- Send text messages to a webhook
- Upload files automatically
- Automatic file detection
- Minimal terminal interface
- Cross-platform support
- Simple installation
- Lightweight and fast

## Requirements

- Python 3.8+
- requests

## Installation

### Automatic (Windows)

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

### Send a file

Enter a valid file path.

```text
C:\Users\User\Desktop\image.png
```

or

```text
"/home/user/file.txt"
```

Cathook automatically uploads the file.

### Exit

Type:

```text
exit
```

or

```text
quit
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
- Works on Windows, Linux, and macOS
- Requires an active internet connection

## License

MIT
