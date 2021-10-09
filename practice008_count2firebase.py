#いつもの定型文
from m5stack import *
from m5ui import *
from uiflow import *
from numbers import Number

#スクリーンカラーをセット
setScreenColor(0x222222)
label0.setPosition(10, 100)


#ここから下がコピペしたexample
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect("[SSID]", "[PASSWD]")

while not GLOB_WLAN.isconnected():
  pass

#firebase example
#こうしないとpyファイルを読み込んでくれない
import sys
sys.path.append('/flash/res')

#プロジェクトをセット
import ufirebase as firebase
firebase.setURL("https://[プロジェクト名].firebaseio.com/")

#button操作
count = None
label0 = M5TextBox(51, 112, "Text", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

#buttonAの動き
def buttonA_wasPressed():
  global count
  count = (count if isinstance(count, Number) else 0) + 1
  setScreenColor(0xff0000)
  label0.setColor(0xFFFFFF)
  label0.setText(str((str('Count Up:') + str(count))))
  pass
btnA.wasPressed(buttonA_wasPressed)

#buttonCの動き
def buttonC_wasPressed():
  global count
  count = (count if isinstance(count, Number) else 0) + -1
  setScreenColor(0x33ff33)
  label0.setColor(0xFFFF00)
  label0.setText(str((str('Count Down:') + str(count))))
  pass
btnC.wasPressed(buttonC_wasPressed)

#buttonBの動き
def buttonB_wasPressed():
  global count
  lcd.clear()
  firebase.put("/M5stack/counter", count)
  label0.setText(str((str('Count Send:') + str(count))))
  
btnB.wasPressed(buttonB_wasPressed)
