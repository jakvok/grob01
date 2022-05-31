# CSYS convert utility

The script is used to convert dimensional values between two rotated coordinate systems in CNC program.<br>
CNC milling machine operator can easy set dimm corrections into machine using the script.
<br><br>
# Using of the script
- Choose side of clamping fixture, operation 10 or 20,
- set desired dimm corrections in rotated CSYS using +-0.01mm buttons,
- hit EXECUTE button to provide calculation,
- see result values and put them to offset table in the machine.

- The NULL button delete input values
<br><br>
## linux
Python 3.8+, only standard modules required on linux.<br>
Make the script executable:<br>
`$ chmod +x ./grob01.py`

Run the script:<br>
`$ ./grob01.py`
<br><br>
## windows
When python 3.8+ installed, using is the same as on linux system.

Or when python is not available on your win system, use the standalone executable `grob01_vx.x.x.exe`.<br>
