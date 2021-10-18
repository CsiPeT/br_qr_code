from qr_generator.qr_generator_wrapper import generate_small_qr

if __name__ == "__main__":
    # Generate
    generate_small_qr(input_data="https://www.youtube.com/watch?v=gjXPHaiqEOg",
                      output_file="./enjoyable_tutorial.png")
