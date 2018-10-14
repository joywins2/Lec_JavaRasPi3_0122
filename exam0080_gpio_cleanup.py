'''
...158p.
   image : https://drive.google.com/open?id=10xISuzeEfse5K2X9B0SZEhgUU-ya2Gyi
...How to Exit GPIO programs cleanly, avoid warnings and protect your Pi :
   RuntimeWarning: This channel is already in use, continuing anyway.  
   Use GPIO.setwarnings(False) to disable warnings.
   http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
'''

'''
...how to check what RPi.GPIO version you have?
   https://raspi.tv/2013/rpi-gpio-basics-1-how-to-check-what-rpi-gpio-version-you-have
   way.01 :
        pi@raspberrypi:~/Lec_JavaRasPi3_0122 $ find /usr | grep -i gpio
        /usr/lib/libpigpioultrasonic.so.1
        /usr/lib/python3/dist-packages/gpiozerocli
        /usr/lib/python3/dist-packages/gpiozerocli/pinout.py
        /usr/lib/python3/dist-packages/gpiozerocli/__init__.py
        /usr/lib/python3/dist-packages/gpiozerocli/__pycache__
        /usr/lib/python3/dist-packages/gpiozerocli/__pycache__/__init__.cpython-35.pyc
        /usr/lib/python3/dist-packages/gpiozerocli/__pycache__/pinout.cpython-35.pyc
        /usr/lib/python3/dist-packages/RPi/GPIO
        /usr/lib/python3/dist-packages/RPi/GPIO/__init__.py
        /usr/lib/python3/dist-packages/RPi/GPIO/__pycache__
        /usr/lib/python3/dist-packages/RPi/GPIO/__pycache__/__init__.cpython-35.pyc
        /usr/lib/python3/dist-packages/RPi/_GPIO.cpython-35m-arm-linux-gnueabihf.so
        /usr/lib/python3/dist-packages/pigpio-1.38.egg-info
        /usr/lib/python3/dist-packages/RPi.GPIO-0.6.3.egg-info¢¸
        /usr/lib/python3/dist-packages/pigpio.py
        /usr/lib/python3/dist-packages/gpiozero-1.4.1.egg-info
    way.02 :
        pi@raspberrypi:~/Lec_JavaRasPi3_0122 $ sudo python
        Python 2.7.13 (default, Sep 26 2018, 18:42:22)
        [GCC 6.3.0 20170516] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import RPi.GPIO as GPIO
        >>> GPIO.VERSION
        '0.6.3'
        >>>
    ...How to update your RPi.GPIO
       sudo apt-get update && sudo apt-get upgrade
    
       But, if you haven¡¯t updated for a while it could take quite a long time to update all your packages (>1hr).
       If you don¡¯t want to do it that way, you could use this, which updates your package list and installs the latest RPi.GPIO
       sudo apt-get update && sudo apt-get install python-rpi.gpio python3-rpi.gpio    
'''


'''
...How to check your Raspberry Pi Revision number?
   https://raspi.tv/2013/rpi-gpio-basics-2-how-to-check-what-pi-board-revision-you-have
    way.01 :
        pi@raspberrypi:~/Lec_JavaRasPi3_0122 $ cat /proc/cpuinfo

    way.02 :
        pi@raspberrypi:~/Lec_JavaRasPi3_0122 $ sudo python
        Python 2.7.13 (default, Sep 26 2018, 18:42:22)
        [GCC 6.3.0 20170516] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import RPi.GPIO as GPIO
        >>> GPIO.RPI_REVISION
        3
        >>>

   

'''

import RPi.GPIO as GPIO

# here you would put all your code for setting up GPIO,  
# we'll cover that tomorrow  
# initial values of variables etc...  
counter = 0  
  
try:  
    # here you put your main loop or block of code  
    while counter < 9000000:  
        # count up to 9000000 - takes ~20s  
        counter += 1  
    print("Target reached: %d" % counter)  
  
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("\n" + str(counter)+"# print value of counter")  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit  