import ndspy.rom
import ndspy.codeCompression as comp
import sys

## Change shiny rate in Pokemon HeartGold/SoulSilver! ##
# Place your .nds file in the same folder as this script.
# Usage: python shiny_rate_editor.py <filename> [<new_shiny_rate>]

def modify_shiny_rate(filename, new_shiny_rate=0xFF):
    # Load rom with ndspy and print rom information
    rom = ndspy.rom.NintendoDSRom.fromFile(filename)
    print(f'Raw arm9 byte size: {len(rom.arm9)}')

    # SoothingSilver's shiny offset is 0x70080, no need to check ROM ID
    shiny_offset = 0x70080

    # Decompress arm9 with ndspy
    decompressed_arm9 = comp.decompress(rom.arm9)
    print(f'Decompressed arm9 byte size: {len(decompressed_arm9)}')

    print(f"\nOld Shiny Rate: {decompressed_arm9[shiny_offset]}/65536")
    decompressed_arm9[shiny_offset] = new_shiny_rate
    print(f"New Shiny Rate after: {decompressed_arm9[shiny_offset]}/65536")

    # Mark the arm9 as decompressed
    decompressed_arm9[0xBB4] = 0x00
    decompressed_arm9[0xBB5] = 0x00
    decompressed_arm9[0xBB6] = 0x00
    decompressed_arm9[0xBB7] = 0x00

    # Note that we do not recompress to avoid crashes.
    rom.arm9 = decompressed_arm9
    rom.saveToFile('shiny_rate_patched.nds')


if __name__ == "__main__":
    argc = len(sys.argv)
    if 2 <= argc <= 3:
        filename = sys.argv[1]
        new_shiny_rate = int(sys.argv[2], 16) if argc >= 3 else 0xFF
        modify_shiny_rate(filename, new_shiny_rate)
    else:
        print("Usage: python shiny_editor.py <filename> [<shiny_offset>] [<new_shiny_rate>]")
