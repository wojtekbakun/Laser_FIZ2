import struct

def pcm_to_txt(input_file, output_file):
    with open(input_file, 'rb') as pcm_file, open(output_file, 'w') as txt_file:
        pcm_data = pcm_file.read()
        for value in struct.iter_unpack('h', pcm_data):
            normalized_value = max(0, min(255, int((value[0] + 32768) / 256)))
            txt_file.write(str(normalized_value) + ',')

if __name__ == "__main__":
    input_file = "../voices/formatted/pcm/what_is_the_weather_today.pcm"  # Zmień na nazwę pliku PCM wejściowego
    output_file = "../voices/formatted/txt/what_is_the_weather_today.txt"  # Zmień na nazwę pliku TXT wyjściowego
    pcm_to_txt(input_file, output_file)
