# Technical interviews prep
Technical interviews, coding live, has it's own particularities, and one way to get better is to practice.

## Cache simulation in Python
Here is a problem: Write a class for least recently used (LRU) cache with input as capacity and implement the general methods needed (put and get). Solution: see `mycache.py` file.

## Verilog netlist parser
Write a Python program that reads a given Verilog file that includes a netlist, parses it, removes comments and line breaks, and stores the Verilog netlist in some kind of data structire. The program will identify modules, primitives, and be able to generate a report of number of instances from different levels. The solution provided in `VerilogInterpreter.py` implements a recursive tree search.

## Patterns match data structure
The program will model a stream processing unit that detects patterns. It implements a data structure for the patterns to be matched. There are no optimizations, the solution is in `patterns.c`.