import os
import sys
import argparse
import re

def psize(name):
	ps = re.split('_|\.' , name)
	return int(ps[len(ps)-2])

def throughput(filenames):
	data = []
	for filename in filenames:
		name = re.split('_|\.', filename)
		packetsize = int(name[len(name)-2])
		data.append((packetsize, throughput_helper(filename , packetsize)))
	return data

def throughput_helper(filename , packetsize):
	trace = open(filename ,  'r')
	count = 0
	start = 0.0
	end = 0.0
	prev = 0.0
	for line in trace:
		if line.startswith('+') and 'tcp' in line and str(packetsize + 40) in line:
			words = line.split(' ')
			prev = float(words[1])	
			if count == 0:
				start = prev		
			count += 1
	end = prev
	throughput = (count*8.0*(packetsize + 40))/((end-start)*1000000)
	trace.close()
	return throughput

def create_file(data):
	datfile = open('plotvalues.dat', 'w')
	datfile.write('#X\tY\n')
	for (k , v) in data:
		datfile.write(str(k) + '\t' + str(v) + '\n')
	datfile.close()

def plot(data):
	gp = open('throughputplot.gp' , 'w')
	gp.write('set grid\n')
	gp.write('set title \"Performance of Stop-n-wait\"\n')
	gp.write('set xlabel \"Packet Size(bytes)\"\n')
	gp.write('set ylabel \"Throughput(mbps)\"\n')
	gp.write('set xrange [64:5000]\n')
	gp.write('set xtics (64 , 128 , 256 , 512 , 1024 , 2048 , 4096)\n')
	gp.write('set logscale x\n')
	gp.write('plot \"plotvalues.dat\" using 1:2:(sprintf(\"(%d,%f)\", $1 , $2)) with labels center offset 3.4,0.5 notitle, \'\' with linespoints pointtype 7\n')
	gp.write('pause -1')
	print 'Done!!'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Process the tracefiles and print the throughput')
	parser.add_argument('filenames' , metavar='filename', type=str , nargs='+',
						help='An ns2 tracefile for which you want the throughput in mbps')
	args = parser.parse_args()
	data = throughput(sorted(args.filenames, key=psize))
	create_file(data)
	plot(data)

