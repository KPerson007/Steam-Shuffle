import os
import os.path
import sys
import random


print("Don't know what to play?  Let me pick a game...")
print("INFO: Loading list of Steam libraries from libraries.conf...")

if os.path.isfile("libraries.conf") == False:
	#if libraries.conf doesn't exist, create a blank one and exit
	open("libraries.conf", "w")
	print("ERROR: libraries.conf does not exist.  A blank libraries.conf has been created.  Populate this with the path to your Steam libraries.  The program will now exit.")
	sys.exit(1)

libraries = [line.rstrip('\n') for line in open("libraries.conf")]
games = list()
print("INFO: Scanning Steam libraries for games...")
for library in libraries:
	if os.path.isdir(library) == False:
		print("ERROR: the directory at " + library + " does not exist.  Moving on to next Steam library...")
	else:
		print("INFO: Now scanning Steam library at " + library + " for SteamApps...")
		files = os.listdir(library)
		for file in files:
			if file.startswith("appmanifest") == True: #appmanifest files in library root contain an installed SteamApp id, so check for them
				id = file.strip('appmanifest_.acf')
				print("INFO: Found SteamApp " + id + "...")
				games.append(id)

print("INFO: Library scan complete.  Now choosing randome SteamApp...")
gameToStart = random.choice(games)
print("INFO: Chose SteamApp " + gameToStart + ".  Now launching SteamApp...")
os.system("start steam://rungameid/" + gameToStart)