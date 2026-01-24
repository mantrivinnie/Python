import struct
import os

try:
    from openpyxl import Workbook
    EXCEL_AVAILABLE = True
except ImportError:
    EXCEL_AVAILABLE = False


def validate_hex_value(hex_str):
    """
    Validate and normalize hexadecimal string to 16-bit value.
    
    Args:
        hex_str (str): Hexadecimal string to validate
        
    Returns:
        tuple: (is_valid, normalized_hex_str, error_message)
    """
    hex_str = hex_str.strip()
    
    # Skip empty strings
    if not hex_str:
        return False, None, "Empty value"
    
    # Remove 0x prefix if present
    if hex_str.lower().startswith('0x'):
        hex_str = hex_str[2:]
    
    # Validate hex format
    try:
        bits_int = int(hex_str, 16)
    except ValueError:
        return False, None, f"Invalid hex format"
    
    # Check if it fits in 16 bits
    if bits_int < 0 or bits_int > 65535:
        return False, None, f"Out of range (0-65535)"
    
    # Ensure 4-digit hex (pad with zeros)
    normalized = '0x' + hex_str.upper().zfill(4)
    return True, normalized, None


def hex_to_decimal(hex_value):
    """
    Convert IEEE 754 16-bit hex to decimal.
    
    Args:
        hex_value (str): Hexadecimal FP16 value (e.g., '0x3C00')
        
    Returns:
        float: Decimal representation
    """
    is_valid, normalized, error = validate_hex_value(hex_value)
    
    if not is_valid:
        raise ValueError(f"Invalid hex: {error}")
    
    bits_int = int(normalized, 16)
    bytes_data = struct.pack('>H', bits_int)
    return struct.unpack('>e', bytes_data)[0]


def convert_hex_file_to_decimal(input_file, output_file):
    """
    Read CSV file with index and hex values, convert hex to decimal.
    Format: index,x_hex,y_hex
    Skips index column, converts x_hex and y_hex to decimal.
    
    Args:
        input_file (str): Path to input text file (CSV format)
        output_file (str): Path to output text file
        
    Returns:
        tuple: (success, count_converted, count_errors, error_messages)
    """
    
    # Read input file
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        return False, 0, 0, f"Failed to read input file: {e}"
    
    if not lines:
        return False, 0, 0, "Input file is empty"
    
    conversions = []
    errors = []
    count_converted = 0
    count_errors = 0
    
    # Skip header if present
    start_idx = 0
    if 'index' in lines[0].lower() or 'x_hex' in lines[0].lower():
        start_idx = 1
    
    print(f"\nProcessing {len(lines) - start_idx} rows...")
    print("-" * 80)
    print(f"{'Row':>4} | {'Index':>5} | {'X_Hex':>10} | {'X_Decimal':>15} | {'Y_Hex':>10} | {'Y_Decimal':>15}")
    print("-" * 80)
    
    for row_num, line in enumerate(lines[start_idx:], start=start_idx + 1):
        line = line.strip()
        
        if not line:  # Skip empty lines
            continue
        
        # Split by comma
        parts = [p.strip() for p in line.split(',')]
        
        if len(parts) < 3:
            count_errors += 1
            error_msg = f"Row {row_num}: Invalid format (expected 3 columns, got {len(parts)})"
            errors.append(error_msg)
            print(f"{row_num:4} | ERROR: {error_msg}")
            continue
        
        # Extract values (skip index column)
        try:
            index_val = parts[0]
            x_hex = parts[1]
            y_hex = parts[2]
            
            # Convert hex values to decimal
            x_decimal = hex_to_decimal(x_hex)
            y_decimal = hex_to_decimal(y_hex)
            
            conversions.append((index_val, x_hex, x_decimal, y_hex, y_decimal))
            count_converted += 1
            
            print(f"{row_num:4} | {index_val:>5} | {x_hex:>10} | {x_decimal:>15.6f} | {y_hex:>10} | {y_decimal:>15.6f}")
            
        except ValueError as e:
            count_errors += 1
            error_msg = f"Row {row_num}: {str(e)}"
            errors.append(error_msg)
            print(f"{row_num:4} | ERROR: {error_msg}")
        except Exception as e:
            count_errors += 1
            error_msg = f"Row {row_num}: {str(e)}"
            errors.append(error_msg)
            print(f"{row_num:4} | ERROR: {error_msg}")
    
    print("-" * 80)
    
    # Write output file as Excel
    try:
        if not EXCEL_AVAILABLE:
            raise ImportError("openpyxl is required. Install with: pip install openpyxl")
        
        # Change extension to .xlsx
        output_file_xlsx = os.path.splitext(output_file)[0] + '.xlsx'
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Decimals"
        
        # Write header (without index)
        ws.append(["x_decimal", "y_decimal"])
        
        # Write conversion results (only decimals, no index, no hex)
        for index_val, x_hex, x_decimal, y_hex, y_decimal in conversions:
            ws.append([x_decimal, y_decimal])
        
        # Add error sheet if there are errors
        if errors:
            error_ws = wb.create_sheet("Errors")
            error_ws.append(["Error Messages"])
            for error_msg in errors:
                error_ws.append([error_msg])
        
        wb.save(output_file_xlsx)
        return True, count_converted, count_errors, output_file_xlsx
        
    except Exception as e:
        return False, count_converted, count_errors, f"Failed to write output file: {e}"


if __name__ == "__main__":
    print("=" * 80)
    print("FP16 IEEE 754 Hex to Decimal Converter")
    print("Input:  CSV file with index, x_hex, y_hex")
    print("Output: Excel file with x_decimal, y_decimal (index and hex removed)")
    print("=" * 80)
    
    if not EXCEL_AVAILABLE:
        print("\nError: openpyxl is not installed.")
        print("Install it with: pip install openpyxl")
        exit(1)
    
    # Get input file path
    input_file = input("\nEnter input text file path (CSV format): ").strip()
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        exit(1)
    
    # Generate output file name
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_Decimal.txt"  # Will be converted to .xlsx
    
    print(f"\nInput file:  {input_file}")
    
    # Convert
    success, converted, errors_count, output_result = convert_hex_file_to_decimal(input_file, output_file)
    
    # Display summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    if success:
        print(f"✓ Successfully converted: {converted} rows")
        if errors_count > 0:
            print(f"✗ Errors encountered:    {errors_count} rows")
        print(f"\nOutput saved to: {output_result}")
    else:
        print(f"✗ Conversion failed: {output_result}")
    
    print("=" * 80)