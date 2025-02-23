# Error Detection Techniques

1. **Parity Check**:
   - **Simple Parity Check**: Involves adding a parity bit to the data to make the number of 1's either even (Even Parity) or odd (Odd Parity). This method is efficient for detecting single-bit errors.
     - *Example*: If sending the word "world" using even parity:
       ```
       w     o     r     l     d
       1110111 1101111 1110010 1101100 1100100
       parity bit calculation: 11101110 11011110 11100100 11011000 11001001
       Received: ✓ ✓ ✓ ✓ ✓ (Each character maintains even parity)
       ```
   - **Limitations**: While effective for single-bit errors, multiple-bit errors are detected only if they result in an odd number of incorrect bits.

2. **Cyclic Redundancy Checksum (CRC)**:
   - Utilizes polynomial division rather than simple addition to generate a checksum.
   - *Steps for CRC Calculation*:
     1. Append \( n \) zero bits to the data, where \( n \) is the length of the divisor minus one.
     2. Perform polynomial division (using XOR) on the extended data.
     3. The remainder from this division is the CRC checksum.
     4. Attach the checksum to the original data for transmission.
   - *Example*:
     - For data `100100` with a divisor `1101`:
       ```
       100100000 / 1101 results in remainder 001.
       Send: 100100 + 001 = 100100001
       ```
   - *Error Detection*: The receiver performs the same division. If the remainder is 0, the data is correct; otherwise, there are errors.

3. **Checksum**:
   - Similar to parity and CRC but involves one's complement arithmetic.
   - *Steps for Checksum Calculation*:
     1. Divide the data into segments (typically 16 bits each).
     2. Add all segments using one's complement.
     3. The complement of the sum becomes the checksum.
     - *Example*: Data segments `10101001` and `00111001`:
       ```
       Sum: 11100010
       Complement: 00011101 (Checksum)
       Send: 10101001 00111001 00011101
       ```
   - *Error Detection*: If the sum of all received segments plus the checksum equals zero (after complement), the data is correct.

### Flow Control

- **Stop-and-Wait**: The sender transmits one frame and waits for an acknowledgment before sending the next frame. It ensures simplicity but can be inefficient due to idle time while waiting.
  - *Scenarios*:
    1. Normal transmission.
    2. Lost or damaged data frames.
    3. Lost or delayed acknowledgment (ACK) frames.
    4. Bidirectional communication using piggybacking.

- **Go-Back-N**: The sender continues to send multiple frames (up to N) without waiting for ACKs. If an error is detected, the sender retransmits from the erroneous frame onwards.
  - *Sliding Window*: Manages the frames sent and acknowledged. Frames to the left of the window are acknowledged and can be removed; those to the right are pending transmission.

- **Selective Repeat**: Only the erroneous frames are retransmitted, ensuring efficiency and reducing retransmission overhead.

### Error Control

- Techniques to ensure accurate data transfer include retransmission strategies such as:
  - **Stop-and-Wait**: Basic method with simple error control but can be inefficient.
  - **Go-Back-N**: Efficient for sequential errors but can result in multiple retransmissions.
  - **Selective Repeat**: Best for minimizing retransmissions by only sending erroneous frames.

