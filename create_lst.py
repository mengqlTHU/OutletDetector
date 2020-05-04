import os

dir_name = "p"
output_file = "pos.lst"

with open(output_file, 'w') as f:
    files = os.listdir("p")
    for filename in files:
        if "jpg" in filename:
            f.write(f"p/{filename} 1 0 0 255 255\n")

dir_name = "n"
output_file = "neg.lst"

with open(output_file, 'w') as f:
    files = os.listdir("n")
    for filename in files:
        if "jpg" in filename:
            f.write(f"n/{filename}\n")