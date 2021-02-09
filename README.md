# shycopy
Just copy over ssh. Sugarless. Say 'adzhara gudzhu' to FileZilla!

**For orthodox linux users only!**

Windows users can automate copy using WinSCP or go the fucking out.

## Install

1. Clone.
```bash
git clone https://github.com/tminei/shycopy.git
```
2. Install system dependencies:
```bash
sudo apt install python3 notify-osd sshpass
```
3. Install python libs:
```bash
pip3 install PyYAML
```

## Setup
1. Go to shycopy/projects and copy test.yml to another_file.yml in shycopy/projects folder **dont touch defautl.yml**
2. Change project key in shycopy/settings.yml
3. Launch using ```python3 shycopy/main.py```
4. You can hang on the hotkey ```python3 shycopy/main.py``` to copy automated.
5. ?????????
6. PROFIT
