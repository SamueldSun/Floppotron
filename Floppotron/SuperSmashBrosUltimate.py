hertz = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         31,
         33,
         35,
         37,
         39,
         41,
         44,
         46,
         49,
         52,
         55,
         58,
         62,
         65,
         69,
         73,
         78,
         82,
         87,
         93,
         98,
         104,
         110,
         117,
         123,
         131,
         139,
         147,
         156,
         165,
         175,
         185,
         196,
         208,
         220,
         233,
         247,
         262,
         277,
         294,
         311,
         330,
         349,
         370,
         392,
         415,
         440,
         466,
         494,
         523,
         554,
         587,
         622,
         659,
         698,
         740,
         784,
         831,
         880,
         932,
         988,
         1047,
         1109,
         1175,
         1245,
         1319,
         1397,
         1480,
         1568,
         1661,
         1760,
         1865,
         1976,
         2093,
         2217,
         2349,
         2489]

# Import stuff
from mido import MidiFile
import time
import serial

# Changing variables
ser = serial.Serial('COM4')
midiFile = 'SuperSmashBrosUltimate.mid'

# Other startup stuff
send = "\n"
time.sleep(3)


# Sends code to Arduino
def sendLine(code):
    print(int(code))
    ser.write((code+"\n").encode())
    # ser.write(send.encode())

# Opens and reads Midi file
for msg in MidiFile(midiFile):
    time.sleep(msg.time*0.8)
    if not msg.is_meta:
        data = str(msg)

        # Filters out other initializing stuff
        if data[0:4] == "note":

            # If drive should turn on
            if data[6:7] == "n":
                if data[16] == "0":
                    code = ("3" + str(hertz[int(data[23:25])]) + "1")
                    sendLine(code)
                else:
                    code = ("2" + str(hertz[int(data[23:25])]) + "1")
                    sendLine(code)
            # If drive should turn off
            elif data[6:7] == "f":
                if data[17] == "0":
                    code = "30"
                    sendLine(code)
                else:
                    code = "20"
                    sendLine(code)

            # Else
            else:
                print("ERROR")
