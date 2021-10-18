from qrcode import QRCode


def generate_small_qr(input_data: str, output_file: str = "enjoyable_tutorial.png"):
    """
    Wrapper code to generate a small QR code for the given input data/link
    :param input_data: <str>
        Data/text/link to embed into the QR code
    :param output_file: <str>
        Output file path with file name, set to local folder so it runs cross OS
    :return: None
    """
    # Creating an instance of QRCode
    qr = QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)
