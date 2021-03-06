import subprocess

print("Hi and welcome to Axos keras to tensorflowjs model converter")

INPUT_PATH = input("Please enter the path to the input directory of the HD5 file saved in .h5 format")
OUTPUT_PATH = input("Please enter the output path to the outut directory whre you want the converted model to be saved")

FULL_COMMAND = "tensorflowjs_converter --input_format=keras " + INPUT_PATH + OUTPUT_PATH

subprocess.run('pip install tensorflowjs')
subprocess.run('pip install keras')
subprocess.run('pip install tensorflow')
subprocess.run(FULL_COMMAND)

