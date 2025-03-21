# Image-Based Secret Message Encryption & Decryption

This Python project allows users to hide a secret message inside an image using encryption and retrieve it using decryption with a passcode.

## Features
- Encrypts a message by modifying image pixels.
- Requires a passcode for decryption.
- Uses OpenCV for image processing.

## Setup & Installation

### Prerequisites
- Python 3.x
- OpenCV (cv2)

### Install Dependencies
```sh
pip install opencv-python
```

### Running the Script
```sh
python main.py
```

## How It Works
1. **Encryption**:
   - The script reads an image (`joyboy.jpg`).
   - It encodes the message into the image pixels.
   - The modified image is saved as `encryptedImage.jpg`.
2. **Decryption**:
   - Requires the correct passcode.
   - Extracts and reconstructs the message from the image.

## Usage Instructions
1. Run `main.py` and enter the message you want to encrypt.
2. Enter a passcode when prompted.
3. Open `encryptedImage.jpg` to see the modified image.
4. To decrypt, enter the same passcode when prompted.

## License
This project is open-source and free to use under the MIT License.

