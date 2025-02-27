from machine import Pin,I2C,SPI,PWM,ADC
import framebuf
import time
import math

from lcd_driver import LCD_1inch28
from imu_qmi8658 import QMI8658

from writer import CWriter
import courier20
from boolpalette import BoolPalette

I2C_SDA = 6
I2C_SDL = 7

DC = 8
CS = 9
SCK = 10
MOSI = 11
RST = 12

BL = 25

Vbat_Pin = 29





if __name__=='__main__':
  
    LCD = LCD_1inch28()
    LCD.set_bl_pwm(65535)
    qmi8658=QMI8658()
    Vbat= ADC(Pin(Vbat_Pin))
    
    wri = CWriter(LCD, courier20)
    
    while(True):
        #read QMI8658
        xyz=qmi8658.Read_XYZ()
        xyz[1]=math.atan2(xyz[0],-xyz[2])*180/math.pi
        reading = Vbat.read_u16()*3.3/65535*2
        
        LCD.fill(0x0000)
        



        
       
        
       
        
        CWriter.set_textpos(LCD, 40, 50)  # In case a previous test has altered this
        wri.setcolor(0xffff, 0x0000)  # Colors can be set in constructor or changed dynamically
        wri.printstring("ACC_X={:+.1f}".format(xyz[0]))
        
        CWriter.set_textpos(LCD, 60, 50)  # In case a previous test has altered this
        wri.setcolor(0xffff, 0x0000)  # Colors can be set in constructor or changed dynamically
        wri.printstring("ACC_Z={:+.1f}".format(xyz[2]))
        
        CWriter.set_textpos(LCD, 100, 50)  # In case a previous test has altered this
        wri.setcolor(0xe0ff, 0x0000)  # Colors can be set in constructor or changed dynamically
        wri.printstring("ANG={:+.1f}".format(xyz[1]))
        
        CWriter.set_textpos(LCD, 150, 50)  # In case a previous test has altered this
        wri.setcolor(0xffff, 0x0000)  # Colors can be set in constructor or changed dynamically
        wri.printstring("Vbat={:.2f}".format(reading))
        
        LCD.show()
        time.sleep(0.1)


