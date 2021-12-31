from qr_generator.qr_generator_wrapper import generate_small_qr

if __name__ == "__main__":
    # Generate `Add contact QR code
    generate_small_qr(
        input_data=b"""BEGIN:VCARD
VERSION:3.0
N:Dancso;Peter;;;
FN:Peter Dancso
TEL;TYPE=CELL:012345567
END:VCARD""",
                      output_file="./contact_card.png")

    # Generate link
    generate_small_qr(input_data="https://www.youtube.com/watch?v=gjXPHaiqEOg",
                      output_file="./enjoyable_tutorial.png")