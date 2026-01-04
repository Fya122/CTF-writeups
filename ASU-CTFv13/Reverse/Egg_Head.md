# File Identification
Start by analyzing the binary using Detect It Easy (DIE).
The analysis shows that the file is packed with UPX.

![alt text](<ss/Screenshot 2026-01-04 191627.png>)

# UPX Unpacking
Unpack the binary using UPX via the terminal:

upx -d egghead

This produces Egg_Head_Unpacked binary.

# PyInstaller Detection
Analyze the unpacked file again using DIE.
This time, DIE reports:

Packer: PyInstaller

This indicates that the binary is a Python application bundled with PyInstaller.

![alt text](<ss/Screenshot 2026-01-04 115150.png>)

# PyInstaller Extraction
To extract the PyInstaller contents, use PyInstaller Extractor:

🔗 https://github.com/extremecoders-re/pyinstxtractor

Running the extractor results in multiple .pyc files.

# Identifying the Relevant .pyc File
Among the extracted files, only one contains the challenge logic:

R3v3r530_1.pyc

# Decompilation
Decompile R3v3r530_1.pyc using Pylingual:

🔗 https://pylingual.io/

This converts the Python bytecode into readable Python source code.

![alt text](<ss/Screenshot 2026-01-04 191739.png>)

# Key & IV Extraction
Using the provided script on the decompiled Python code reveals the encryption key and IV, completing the challenge.

![alt text](<ss/Screenshot 2026-01-04 192116.png>)

# Final Key and IV
- Key: m0nk3y_d_l0f1_j0y_b0y 
- IV: 0n3p13c3


# Tools used
- Detect It Easy (DIE)
- UPX
- PyInstaller Extractor
- Pylingual