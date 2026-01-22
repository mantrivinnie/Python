import numpy as np

def float_to_fp16_hex(value):
    fp16 = np.float16(value)
    hex_val = fp16.view(np.uint16)
    return f"0x{hex_val:04X}"

# Examples
print(float_to_fp16_hex(1.0))     # 0x3C00
print(float_to_fp16_hex(0.5))     # 0x3800
print(float_to_fp16_hex(1.25))    # 0x3D00
print(float_to_fp16_hex(-0.5))    # 0xB800
print(float_to_fp16_hex(3.25))    # 0x4280
print(float_to_fp16_hex(2.0))     # 0x4000