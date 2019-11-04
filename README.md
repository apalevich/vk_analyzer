# VK analizer (CLI)

Simple CLI application to analyze VK accounts

## Features
- Shows top 3 posts with most likes

## Requirements
- Python3
- Standart library Requests (see requrements.txt for more info)
- VK service token (instructions here: https://vk.com/dev/access_token)

## Installation
1. Download the repo by downloading it or using `git clone` in your CLI
2. In the same directory, create file `token.py` and open it in any text editor
3. Create an app at [VK Dev](https://vk.com/apps?act=manage "VK Dev"), generate its service token and copy it
4. While editing `token.py`, type in here:
```python
TOKEN = 'put here you token'
```
5. Now you can save it and close.

## Using
Launch vk_parcing.py by typing in CLI python `vk_parcing.py`. Follow the instructions.

------------
### Ideas
- Launch from CLI with different arguments (sys.argv)
- Export and import selection to CSV
