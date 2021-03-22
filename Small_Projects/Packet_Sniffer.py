import socket
import argparse

#Create a global parser object
parser = argparse.ArgumentParser()
#Gather Arguments

parser.add_argument('-i', '--interface', action='store', dest='intfc')
parser.add_argument('-d-port', '--dest-port', action='store', dest='dport')
parser.add_argument('-s-ip', '--src-ip', action='store', dest='sip')

print(parser.intfc)
#print('\n El comando funciono perfectamente, los argumentos Interface: {intfc}, Destination Port {dport}, Source IP {sip}', '\n'.format(intfc=parser.intfc, dport=parser.dport, sip=parser.sip))



