# This is a really simple drawing app.
#
# Every time the Tingbot detects something touching the
# screen, this program draws a blue rectangle in that place.
#
# For more info on what can be done with @touch, check out
# https://tingbot-python.readthedocs.io/en/latest/touch.html

import tingbot
from tingbot import *
import requests
import json
import time

global page
global maxpage
global pagedata
global zone
global weatherdata
global lasttouch
global refreshinterval
global weatherRefresh
global weatherTicks
zone = ''
view = 1
page = 1
lasttouch = 0
with open('pagedata.json') as data_file:
    pagedata = json.load(data_file)
weatherdata = {}
maxpage = len(pagedata['Pages'])
refreshinterval = int(pagedata.get('refreshIntervalSeconds'))
weatherRefresh = int(pagedata.get('yahooweatherRefresh'))
weatherTicks = weatherRefresh

@left_button.press
def pressl():
    leftbutton()

@midleft_button.press
def pressml():
    midleftbutton()

@midright_button.press
def pressmr():
    midrightbutton()

@right_button.press
def pressr():
    rightbutton()
    

@touch(xy=(210,2), size=(28,28), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        midrightbutton()
        
@touch(xy=(280,2), size=(28,28), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        rightbutton()

@touch(xy=(0,40), size=(40,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('A1')

@touch(xy=(0,90), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('A2')

@touch(xy=(0,140), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('A3')

@touch(xy=(0,190), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('A4')

@touch(xy=(80,40), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('B1')

@touch(xy=(80,90), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('B2')

@touch(xy=(80,140), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('B3')

@touch(xy=(80,190), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('B4')

@touch(xy=(160,40), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('C1')

@touch(xy=(160,90), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('C2')

@touch(xy=(160,140), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('C3')

@touch(xy=(160,190), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('C4')

@touch(xy=(240,40), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('D1')

@touch(xy=(240,90), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('D2')

@touch(xy=(240,140), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('D3')

@touch(xy=(240,190), size=(80,50), align='topleft')
def on_touch(xy, action):
    if action == 'up':
        zoneaction('D4')

def leftbutton():
    pane()

def midleftbutton():
    pane()

def midrightbutton():
    global page
    global lasttouch
    global refreshinterval
    if lasttouch > refreshinterval:
        page = page
    else:
        if page > 1:
            page = page - 1
        else:
            page = maxpage
    pane()

def rightbutton():
    global page
    global maxpage
    global lasttouch
    global refreshinterval
    if lasttouch > refreshinterval:
        page = page
    else:
        if page < maxpage:
            page = page + 1
        else:
            page = 1
    pane()
    
def pane():
    global page
    global lasttouch
    strName = pagedata['Pages'][(page-1)]['name']
    
    screen.fill(color='silver')
    screen.text('',color='blue')
    screen.rectangle(xy=(197,0), size=(124,35), color='silver', align='topleft')
    screen.text(str(page), xy=(250,0), color='black', font_size=30, align='topleft')
    screen.rectangle(xy=(0,36), size=(320,2), color='navy', align='topleft')
    screen.rectangle(xy=(195,0), size=(2,36), color='navy', align='topleft')
    screen.text(strName, xy=(98,18), color='red', font_size=20, align='center')
    if page > 1:
        screen.image('green-left.png', xy=(208,3), align='topleft')
    else:
        screen.image('grey-left.png', xy=(208,3), align='topleft')
    if page < maxpage: 
        screen.image('green-right.png', xy=(278,3), align='topleft')
    else:
        screen.image('grey-right.png', xy=(278,3), align='topleft')
    drawGrid()
    lasttouch = 0

def drawGrid():
    jsdata = pagedata['Pages'][(page-1)]['layout']
    screen.rectangle(xy=(0,40), size=(320,200), color='white', align='topleft')
    drawItem(0,40,jsdata['A1'])
    drawItem(0,90,jsdata['A2'])
    drawItem(0,140,jsdata['A3'])
    drawItem(0,190,jsdata['A4'])
    drawItem(80,40,jsdata['B1'])
    drawItem(80,90,jsdata['B2'])
    drawItem(80,140,jsdata['B3'])
    drawItem(80,190,jsdata['B4'])
    drawItem(160,40,jsdata['C1'])
    drawItem(160,90,jsdata['C2'])
    drawItem(160,140,jsdata['C3'])
    drawItem(160,190,jsdata['C4'])
    drawItem(240,40,jsdata['D1'])
    drawItem(240,90,jsdata['D2'])
    drawItem(240,140,jsdata['D3'])
    drawItem(240,190,jsdata['D4'])

def drawItem(x,y,jsdata):
    procitem = 0
    if jsdata.get('label'):
        func_label(x,y,jsdata)
        procitem = 1
    if jsdata.get('data'):
        func_data(x,y,jsdata)
        procitem = 1
    if jsdata.get('dispdata'):
        func_dispdata(x,y,jsdata)
        procitem = 1
    if jsdata.get('ywthr'):
        func_ywthr(x,y,jsdata)
        procitem = 1
    if (procitem == 0):
        screen.image(jsdata.get('act'), xy=(x,y), align='topleft')

def func_label(x,y,jsdata):
    addLabel(x,y,jsdata.get('label'))

def func_data(x,y,jsdata):
    r = webRequest(jsdata.get('data'), jsdata)
    bits = jsdata.get('actvalue').split(",")
    bOn = False
    if bits[0] == "int":
        if int(r.text) == int(bits[1]):
            bOn = True
    if bits[0] == "str":
        if r.text == bits[1]:
            bOn = True
    if bOn == True:
        screen.image(jsdata.get('act'), xy=(x,y), align='topleft')
    else:
        screen.image(jsdata.get('inact'), xy=(x,y), align='topleft')

def func_dispdata(x,y,jsdata):
    r = webRequest(jsdata.get('dispdata'), jsdata)
    cmdStr = "r.json()" + jsdata.get('jsonValue')
    val = eval(cmdStr)
    dispval = jsdata.get('syntax').replace('{0}', str(val))
    screen.rectangle(xy=(x,y), size=(80,50), color='white', align='topleft')
    if dispval == "True":
        screen.image('on.png', xy=(x,y), align='topleft')
    else:
        if dispval == "False":
            screen.image('off.png', xy=(x,y), align='topleft')
        else:
            screen.text(dispval, xy=((x+40),(y+25)), color='black', font_size=18, align='center')

def func_ywthr(x,y,jsdata):
    global weatherdata
    screen.rectangle(xy=(x,y), size=(80,50), color='white', align='topleft')
    #r = webRequest(pagedata['yahooweather'], jsdata)
    #data = r.json()
    if (jsdata.get('ywthr') == 'img'):
        cdata = weatherdata['query']['results']['channel']['item']['description']
        imgpos = cdata.find('img src="') + 9 
        img = cdata[imgpos:(cdata.find('"',imgpos))]
        screen.image(img, xy=((x+40),(y+25)), align='center')
    if (jsdata.get('ywthr') == 'hightemp'):
        cdata = weatherdata['query']['results']['channel']['item']['forecast'][0]['high']
        dispval = jsdata.get('syntax').replace('{0}', cdata)
        screen.text(dispval, xy=((x+40),(y+25)), color='red', font_size=18, align='center')
    if (jsdata.get('ywthr') == 'nowtemp'):
        cdata = weatherdata['query']['results']['channel']['item']['condition']['temp']
        dispval = jsdata.get('syntax').replace('{0}', cdata)
        screen.text(dispval, xy=((x+40),(y+25)), color='black', font_size=18, align='center')
    if (jsdata.get('ywthr') == 'lowtemp'):
        cdata = weatherdata['query']['results']['channel']['item']['forecast'][0]['low']
        dispval = jsdata.get('syntax').replace('{0}', cdata)
        screen.text(dispval, xy=((x+40),(y+25)), color='blue', font_size=18, align='center')

def webRequest(data, jsdata):
    hdrs = {"content-type": "application/json"}
    if jsdata.get('headers'):
        hdrs = jsdata.get('headers')
    bits = data.split(",")
    if bits[0] == "GET":
        ret = requests.get(bits[1], headers=hdrs)
    if bits[0] == "POST":
        ret = requests.post(bits[1], headers=hdrs, data=bits[2])
    if bits[0] == "PUT":
        ret = requests.put(bits[1], headers=hdrs)
    return ret
        
def zoneaction(setZone):
    global zone
    zone = setZone
    redraw = False
    #addLabel(240,190,zone)
    jsdata = pagedata['Pages'][(page-1)]['layout'][zone] 
    
    if jsdata.get('on_action'):
        redraw = True
        if jsdata.get('actvalue'):
            r = webRequest(jsdata.get('data'), jsdata)
            bits = jsdata.get('actvalue').split(",")
            bOn = False
            if bits[0] == "int":
                if int(r.text) == int(bits[1]):
                    bOn = True
            if bits[0] == "str":
                if r.text == bits[1]:
                    bOn = True
            if bOn == True:
                webRequest(jsdata.get('off_action'), jsdata)
            else:
                webRequest(jsdata.get('on_action'), jsdata)
        else:
            webRequest(jsdata.get('on_action'), jsdata)

    if redraw:
        drawGrid()

def addLabel(x,y,sLabel):
    fontSize = 19
    if len(sLabel) > 8:
        fontSize = 12 - int( (len(sLabel) -8 ) / 2)
    screen.rectangle(xy=(x,y), size=(80,50), color='white', align='topleft')
    screen.image('Label.png', xy=(x,y), align='topleft')
    screen.text(sLabel, xy=((x+40),(y+25)), color='black', font_size=fontSize, align='center')

def showclock():
    screen.fill(color='black')
    curTime = time.localtime()
    iHour = curTime.tm_hour
    iMin = curTime.tm_min
    iSec = curTime.tm_sec
    sHour = ""
    sMin = ""
    sDay = pagedata.get('daynames')[curTime.tm_wday]
    sMon = pagedata.get('monthnames')[curTime.tm_mon - 1]
    dayStr = str(curTime.tm_mday) + " " + sMon  + " " + str((curTime.tm_year-2000))
    if (iHour > 12):
        iHour = iHour - 12
    sHour = sHour + str(iHour)
    if (iMin < 10):
        sMin = "0"
    sMin = sMin + str(iMin)
    strTime = "\t\t\t\t\t\t" +  sDay + "\n\t\t" + dayStr + "\n\t\t\t\t\t" + sHour + ":" + sMin
    offset = iMin
    if (iMin > 30):
        offset = 60 - iMin
    screen.text(strTime, xy=(0,offset), color='blue', font_size=50, align='topleft')

@every (seconds=30)
def init():
    global lasttouch
    global refreshinterval
    global weatherRefresh
    global weatherTicks
    global weatherdata
    weatherTicks = weatherTicks + 30
    if  weatherTicks > weatherRefresh:
        weatherdata = (webRequest(pagedata['yahooweather'], weatherdata)).json()
        weatherTicks = 0
    if lasttouch > refreshinterval:
        showclock()
    else:
        lasttouch = lasttouch + 30

init()
pane()
tingbot.run()
