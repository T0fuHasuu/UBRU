# Data and Signal Fundamental

### Difference Between Data and Signal
- **Data:** Represents meaningful information such as numbers, text, still images, and animations. When transmitting data between two points, it must be converted into a signal that is suitable for the communication system.
- **Signal:** A variable that changes over time, often used in communication systems as electrical currents or electromagnetic waves. Examples include phone conversations, printing commands, and data downloads.

### Analog vs Digital  
- **Analog Signal:** Continuous wave, fluctuating smoothly, with signal levels measured in voltage.  
- **Digital Signal:** Signals must be converted from digital to analog for certain communication systems, and vice versa at the receiving end.  

### Analog Signal Characteristics  
- **Amplitude:** The wave's height, measured in volts, indicates signal strength.  
- **Frequency:** The number of wave cycles per second, measured in Hertz (Hz).  
- **Period:** The time it takes for a wave to complete one cycle.  
- **Phase:** The wave’s position in its cycle, measurable in degrees.

### Digital Signal and Data  
- **Digital Signal:** A non-continuous square wave with voltage levels alternating between 0 and 1, changing in discrete steps.  
- **Advantages:** Lower cost, more resistant to noise, and easier to distinguish data from signals.  
- **Disadvantages:** Signal attenuation over long distances; analog signals perform better for longer distances. Repeaters regenerate weakened signals.

### Digital Signal Characteristics  
- **Bit Interval:** The time it takes to transmit one bit.  
- **Bit Rate:** Number of bits transmitted per second (bps).  
- **Signal Levels:** Can carry more than two levels, transmitting multiple bits at once.  

### Measurement of Data Transmission Speed  
- **Bit Rate:** Number of bits transmitted per second.  
- **Baud Rate:** Number of signal changes per second. Bit rate is typically greater than or equal to baud rate.  
- **Bandwidth:** Dependent on baud rate, compared to the capacity of a transport system (e.g., buses and passengers).

### Data Conversion to Signals  
- **Analog to Analog Conversion:** Data in analog form is converted into analog signals for transmission, e.g., FM radio signals. Techniques like modulation (AM/FM) are used to embed the information in a carrier wave, which is then demodulated at the receiver.  
- **Digital to Digital Conversion:** Digital data is converted into digital signals using a digital transmitter. Binary data (0 or 1) is represented by high or low voltage levels.

### Digital to Digital Signal Conversion  
- **NRZ-L (NonReturn-to-Zero-Level):** In this simple method, the signal level depends on the bit's value: a `1` is represented by a low voltage, and a `0` by high voltage. However, it can be difficult to determine the start and end points of the bit, especially when consecutive bits are the same.  
- **NRZ-I (NonReturn-to-Zero-Invert):** Similar to NRZ-L but more accurate. The signal changes at the beginning of the bit and only changes when a `1` bit is encountered, leaving a `0` unchanged.  
- **Manchester Encoding:** Used in networks like Ethernet, this method changes the signal at the midpoint of the bit. A change from low to high represents a `1`, and from high to low represents a `0`.  
- **Differential Manchester Encoding:** Like Manchester encoding but only uses signal changes at the bit's start if the bit is `0`, while the middle of the bit determines timing.

### Digital to Analog Signal Conversion  
- **Modem (Modulator/Demodulator):** Used for converting digital data to analog signals and vice versa. For example, in dial-up internet, the sending modem converts digital data into analog signals for transmission via telephone lines, and the receiving modem converts the analog signals back to digital for use by the computer.

### Digital to Analog Signal Conversion  
Digital data is converted for transmission over analog channels using **modulation**. The main techniques are:
- **ASK (Amplitude-Shift Keying):** Changes the carrier's amplitude.
- **FSK (Frequency-Shift Keying):** Changes the carrier's frequency.
- **PSK (Phase-Shift Keying):** Changes the carrier's phase.

### Analog to Digital Signal Conversion  
A **codec** (Coder/Decoder) is used to convert analog signals to digital, and vice versa, through techniques like **Voice Digitization**. Examples include sound cards and scanners.

### Signal Loss During Transmission  
Signal quality may degrade due to:
1. **Attenuation:** Weakening of the signal.
2. **Velocity Differences:** Varying speeds of signal transmission.
3. **Noise:** External interference.

### Signal Loss During Data Transmission

1. **Attenuation (Signal Weakening):**  
As signals travel through media (e.g., coaxial cables, fiber optics), their strength decreases with distance. To compensate, **amplifiers** for analog signals and **repeaters** for digital signals are used to maintain signal quality.

2. **Distortion:**  
In composite signals, different frequencies travel at different speeds, causing the signal to distort. To correct this, **equalizers** are used to adjust and synchronize frequencies.

3. **Noise:**  
Various types of noise can degrade the signal:
   - **Thermal Noise:** Caused by heat, this is unavoidable as it results from electron movement. Higher temperatures increase noise levels, affecting signal integrity.

### Signal Loss in Data Transmission

- **Impulse Noise:** Sudden noise spikes from external sources, disrupts signals. Prevent with filters or digital processors.
- **Crosstalk:** Interference between lines, common in twisted pair cables. Prevent with shielded cables.
- **Echo:** Signal reflections cause delays. Prevent with terminators on cable ends.
- **Jitter:** Frequency shifts causing phase changes. Prevent with quality circuits or repeaters.

### Signal Loss Prevention in Data Transmission

To reduce signal interference:

1. **Use shielded cables** to prevent electromagnetic interference and crosstalk.
2. **Ensure proper phone line conditions** with filters or high-speed leased lines to reduce transmission errors.
3. **Upgrade to modern equipment** for better performance, even if more expensive.
4. **Use repeaters or amplifiers** for longer digital or analog signal transmission to maintain signal integrity.
5. **Consider cable limitations**, like UTP which supports up to 100m and 100 Mbps speeds.