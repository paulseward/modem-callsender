#!/usr/bin/env python

import serial
import time

modem = serial.Serial(
    port='/dev/tty.usbserial-1410',
    baudrate=9600,
    bytesize=8,
    parity='N',
    timeout=1,
    stopbits=1,
    rtscts=False,
    dsrdtr=False
)

def modemCmd(command):
  modem.write(str.encode(command + '\r\n'))
  result=modem.read(100)
  return result.decode('utf-8')

## Main
def main():
  # Check we have a modem listening
  print(modemCmd('AT'))
  
  # Modem configuration string:
  # AT
  # X1    - disable dialtone and busy tone detection
  # &G0*  - disable guard tone
  # VBT=0 - disable beep tone timer

  print(modemCmd('ATX1&G0*VBT=0'))

  time.sleep(3)

  for i in range(1):
    # Go offhook, dial '55', wait 10 seconds, hangup
    print(modemCmd('ATX5DP55W'))
    time.sleep(10)
    modemCmd('ATH')

if __name__ == "__main__":
    main()
