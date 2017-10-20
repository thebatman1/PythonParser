# PythonParser
A python script to parse through ns2 tracefiles, calculate the throughput and plot the throughputs against packetsizes using gnuplot.
# Usage
Make sure you have already generated the tracefiles for the different packetsizes and named them as \'packet_size_(packetsize).tr\'<br>
<b>eg.</b> For a tracefile for packetsize 64 bytes, the name should be <b>packet_size_64.tr</b><br><br>
usage: python pythonparser.py \<tracefile1\> \<tracefile2\> ..........
<br>
This will generate a gnuplot script file ready to plot the values stored in a DAT file.

# Example
python pythonparser.py packet_size_*.tr (for Linux and Unix)<br>
python pythonparser.py packet_size_64.tr packet_size_128.tr packet_size_256.tr ...... (For Windows cmd)<br>
A file called throughputplot.gp will be created<br>
gnuplot throughputplot.gp

