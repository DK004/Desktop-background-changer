import ctypes,win32con
# import ctypes
# from plyer import notification
import psutil
import time
# from wallpaper import set_wallpaper, get_wallpaper

imgStableMode = ""
imgGodMode = ""
imgCharging = ""



def getWallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value

# def setWallpaper(path):
#     changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
#     ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER,0,path,changed)

# print(getWallpaper() == imgStableMode)



# percent = battery.percent

# print(status)
# ctypes.windll.user32.SystemParametersInfoW(20, 0, imgStableMode , 0)
while True:
    time.sleep(2)    
    battery = psutil.sensors_battery()
    status = battery.power_plugged
    if status:
        print("charging")
        if getWallpaper() == imgCharging:
            continue
            # notification.notify(title="Charging Status changed", message="The wallpaper is changed...", app_name="Desktop changer")
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, imgCharging , 0)
        
    else:
        print("not charging")
        if getWallpaper() == imgStableMode:
            continue
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, imgStableMode , 0)
        
# ctypes.windll.user32.SystemParametersInfoW(20, 0, imgCharging , 0)
