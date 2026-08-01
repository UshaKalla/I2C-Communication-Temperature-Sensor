# Logic Analyzer Output During Read Temperature

<img width="1531" height="337" alt="image" src="https://github.com/user-attachments/assets/4970c0e8-8c9c-4766-8f2e-86a47d252bc3" />

# Logic Analyzer Output During Button Press On/Off
# I2C Waveform Analysis: LED Brightness Write (Button Unpressed)
<img width="1831" height="140" alt="image" src="https://github.com/user-attachments/assets/314d1fb4-92b6-4265-8fa2-ffcaed535adc" />

Command breakdown of this:

<img width="677" height="202" alt="image" src="https://github.com/user-attachments/assets/b0f56785-b29e-4682-82a8-4aacf7de0273" />


Command Breakdown (`h6F WR` → `h19` → `h00`)

* **`h6F WR` (Address Frame)**
  * **`0x6F`**: I2C peripheral address of the SparkFun Qwiic Button.
  * **`WR`**: Write operation (`R/W` bit = `0`).

* **`h19` (Register Address Byte)**
  * Target internal register: `0x19` (`LED_BRIGHTNESS`).

* **`h00` (Data Byte)**
  * Data written to `0x19`: `0x00` (Brightness level 0 / **OFF**, since the button is not pressed).

---
Waveform Signals (`SCL` & `SDA`)

* **`SCL` (Clock Line)**
  * Pulses in bursts strictly during data/address transmission (plus the 9th ACK bit); idles HIGH between bytes.

* **`SDA` (Data Line)**
  * Toggles between HIGH and LOW to transmit bits synchronized with `SCL` rising/falling edges.

* **ACK/NACK Bits**
  * Downward ticks on `SDA` between frames (`h6F WR`, `h19`, `h00`) representing **Acknowledge (ACK)** signals sent by the button device.




# I2C Waveform Analysis: LED Brightness Write (Button Pressed)
<img width="1625" height="105" alt="image" src="https://github.com/user-attachments/assets/1add3ad5-3c0a-46e0-bef3-2a46bffd4858" />

Command break down of this: 

<img width="936" height="252" alt="image" src="https://github.com/user-attachments/assets/0ffcc8f0-ec5f-4f1f-831a-d9cd38d348e9" />

# I2C Waveform Analysis: LED Brightness Write (Button Pressed)

1. Command Breakdown (`h6F WR` → `h19` → `hFF`)

* **`h6F WR` (Address Frame)**
  * **`0x6F`**: I2C peripheral address of the SparkFun Qwiic Button.
  * **`WR`**: Write operation (`R/W` bit = `0`).

* **`h19` (Register Address Byte)**
  * Target internal register: `0x19` (`LED_BRIGHTNESS`).

* **`hFF` (Data Byte)**
  * Data written to `0x19`: `0xFF` (Max brightness level 255 / **ON**, since the button is pressed).

---

## 2. Key Differences From the Unpressed State (`h00` vs `hFF`)

* **Data Payload Sent to Register `0x19`**
  * **Unpressed State (`image_ccf17d.png`):** Transmits **`h00`** to turn the LED off.
  * **Pressed State (`image_ccded8.png`):** Transmits **`hFF`** to turn the LED on at full brightness.
* **SDA Bit Pattern for Data Byte**
  * Because `0x00` is all zeros (`0000 0000`) and `0xFF` is all ones (`1111 1111`), the data portion of the SDA line stays LOW for the entire byte frame in the unpressed state, whereas it stays HIGH for the data transmission in the pressed state (aside from the trailing ACK bit).


