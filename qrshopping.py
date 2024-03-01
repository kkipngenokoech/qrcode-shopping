import qrcode

# Function to generate QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# qr code usage
if __name__ == "__main__":
    data = "https://twitter.com/Kkipngeno_koech"  # Data you want to encode in the QR code
    filename = "example_qr_code.png"   # Output filename for the QR code image
    generate_qr_code(data, filename)
    print(f"QR code generated and saved as '{filename}'")
