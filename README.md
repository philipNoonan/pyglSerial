# pyglSerial
An openGL GLSL implementation of Serial comms Using a python front end

## Installation

Tested running on win11 with python 3.8 x64

```shell
$ pip install git+https://github.com/philipNoonan/pyglSerial.git
```
or 

```shell
$ git clone https://github.com/philipNoonan/pyglSerial.git
$ cd pyglSerial
$ python -m venv pyglserial-env
$ pyglserial-env\Scripts\activate.bat
$ pip install .
```

## Using pyglSerial


Follow this guide to setup your arduino and LED's gpio. The python code assumes COM4 and 9600 baud.
```
$ pyglSerial
```

This opens a green window, with a menu allowing you to choose between Turn ON or OFF the LED. This sends a 'H' or 'L' char via serial to the arduino so that the sketch logic can control the LED.
