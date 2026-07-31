def readTemp():
	
	data = bytearray(2)
	while not i2c.try_lock():
		time.sleep(0.1)
	
	i2c.readfrom_into(0x48, data)		
	i2c.unlock()

	msb = data[0]
	lsb = data[1]

	res = (msb << 4) | (lsbs >> 4)
	res = res * 0.0625

	return res
	




def readBtnStatus():
	while not i2c.try_lock():
		time.sleep(0.1)
	
	data = bytearray(1)
	i2c.writeto(0x6F, bytearray([0x03]))
	i2c.readfrom_into(0x6F, data)
	
	i2c.unlock()


	
	return bool(data[0] & 0x04)

def writeBtnLED(brightness, reg_addr):
	while not i2c.try_lock():
		time.sleep(0.1)
	

	i2c.writeto(0x03, bytearray([reg_addr, brightness])
	i2c.unlock()



while True:
	if readBtnStatus():
		writeBtnLED(255, 0x19)
		setBacklightColor(0, 255, 0)
	else:
		writeBtnLED(0, 0x19)
		setBacklightColor(255, 0, 0):



def setBacklightColor(red, green, blue):
	while not i2c.try_lock():
		time.sleep(0.1)
	
	i2c.writeto(LCD_ADDR, bytearray([0x7C, 0X2B, red, green, blue)
	
	i2c.unlock()













	