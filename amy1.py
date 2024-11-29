# run on WSL

import sys
sys.path.append("/home/frankw/Projects/amy")

import amy
m = amy.message(voices='0', load_patch=130, note=50, vel=1)
print(m) # Show the wire protocol message
# v0n50l1K130r0Z
amy.send_raw(m)
# This plays immediately on Tulip, but if you're running Amy in regular Python, you can get the waveform from render:
audio = amy.render(5.0)