#Batch conversion (VERY useful for images & matrices)

import numpy as np 

values = [1.0, 0.5, 2.0, 3.25, -1.75]

for v in values:
    fp16 = np.float16(v)
    hex_val = fp16.view(np.uint16)
    print(f"{v:6} → 0x{hex_val:04X}")