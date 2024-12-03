# 7-segment clock (segmock)

![segmock_screenshot](https://github.com/user-attachments/assets/79055e60-2c06-4c55-9104-13f45ea2b4d9)

A simple and large 7 segment Figlet font clock CLI app.
It can display the current time and measure with a stopwatch.
It can also be used in the Linux console.

## Usage
### Using uv
If you don't have uv installed, please install it.
#### Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
---
```bash
uv tool install segmock
```
```bash
segmock
```
or
```bash
uvx segmock
```
