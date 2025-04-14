# IAS Processor Design

## Overview
This project implements an IAS processor in C++ with a 200 MHz clock frequency, simulating the fetch, decode, and execute cycles according to the IAS architecture. It includes an assembler to convert IAS assembly programs into machine code and supports custom instructions with new opcodes.

## Features
- IAS processor simulation with internal signal generation for MemRead and MemWrite.
- Assembler to translate assembly code into machine code.
- Custom instructions integrated into the ISA.
- Supports Load, Store, Jump, and ALU instructions.
- Tested with programs like matrix multiplication and array sorting.

## Project Structure
- `processor.py` - Main processor simulation code.(It will take output from assembler and use it as input)
- `assembler.py` - Assembler for converting assembly to binary.
- `ASSEMBLY.txt` - Sample assembly program input.

## How to Run
1. **Compile the Code:**  
   python3 assembler.py ASSEMBLY.txt
   python3 processor.py 

