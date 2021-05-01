# adb-capture

## Use
### Install files...

#### Windows
파이썬을 3.6.8을 설치해 준다.
pyenv-win으로 설치하면 조금 쉽다.

### pyenv 설치하기

* choco : `choco install pyenv-win`

### 3.6.8 파이썬을 설치

```
pyenv install 3.6.8
pyenv local 3.6.8
python --version
```

### 파이썬 가상 환경 만들어 주기

```cmd
> python -m pip install virtualenv
> python -m virtualenv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
```

```cmd
> python -m venv venv
> .\venv\Scripts\activate.bat
> pip install -r requirements.txt
```

#### Linux

```bash
$ sudo apt-get install chromium-chromedriver
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

------

## How to use
```cmd
$ python mangashowme.py
```

## Make Install file..
빌드 할 때는 python이 3.6 버전이여야 한다.
```cmd
auto-pi-to-exe
```

Or
```cmd
pyinstaller -y -F "mangashowme.py"
```

# Update all package
```
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```


## Reference
* [Python Capture Android Phone Screenshot using ADB – ADB Tutorial](https://www.tutorialexample.com/python-capture-android-phone-screenshot-using-adb-adb-tutorial/)
* [Android Shell (adb.exe) - 안드로이드 여러가지 명령어들](https://m.blog.naver.com/PostView.nhn?blogId=gyurse&logNo=220911727781&proxyReferer=https:%2F%2Fwww.google.co.kr%2F)
* [안드로이드 키 이벤트 (adb shell로 보내는 법)](http://www.dreamy.pe.kr/zbxe/CodeClip/164608)
* [ADB로 안드로이드 스크린 캡쳐하기 (Windows에 바로 저장하기)](http://heyo.net/wp/66574)