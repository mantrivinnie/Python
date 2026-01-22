#Generate .mem file for Verilog ($readmemh)

import numpy as np

values = [1.0, 0.5, 2.0, 3.25, -1.75]

with open("fp16_data.mem", "w") as f:
    for v in values:
        fp16 = np.float16(v)
        hex_val = fp16.view(np.uint16)
        f.write(f"{hex_val:04X}\n")

print("fp16_data.mem generated successfully")
