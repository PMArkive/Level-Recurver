from first_thing import *
import random

evolve_array_bw = [0,2,3,3,5,6,6,8,9,9,11,12,12,14,15,15,17,18,18,20,20,22,22,24,24,25,26,28,28,30,31,31,33,34,34,36,36,38,38,40,40,42,169,45,182,45,47,47,49,49,51,51,53,53,55,55,57,57,59,59,62,186,62,64,65,65,67,68,68,70,71,71,73,73,75,76,76,78,78,80,80,82,462,83,85,85,87,87,89,89,91,91,93,94,94,208,97,97,99,99,101,101,103,103,105,105,106,107,463,110,110,112,464,242,465,115,117,230,119,119,121,121,122,123,124,466,467,127,128,130,130,131,132,133,134,135,136,233,139,139,141,141,142,143,144,145,146,148,149,149,150,151,153,154,154,156,157,157,159,160,160,162,162,164,164,166,166,168,168,169,171,171,25,35,39,176,468,178,178,180,181,181,182,184,184,185,186,188,189,189,424,192,192,469,195,195,196,197,430,199,429,201,202,203,205,205,206,472,208,210,210,211,212,213,214,461,217,217,219,219,221,473,222,224,224,225,226,227,229,229,230,232,232,474,234,235,237,237,124,125,126,241,242,243,244,245,247,248,248,249,250,251,253,254,254,256,257,257,259,260,260,262,262,264,264,266,267,267,269,269,271,272,272,274,275,275,277,277,279,279,281,282,282,284,284,286,286,288,289,289,291,291,292,294,295,295,297,297,183,476,301,301,302,303,305,306,306,308,308,310,310,311,312,313,314,407,317,317,319,319,321,321,323,323,324,326,326,327,329,330,330,332,332,334,334,335,336,337,338,340,340,342,342,344,344,346,346,348,348,350,350,351,352,354,354,356,477,357,358,359,202,362,362,364,365,365,367,367,368,369,370,372,373,373,375,376,376,377,378,379,380,381,382,383,384,385,386,388,389,389,391,392,392,394,395,395,397,398,398,400,400,402,402,404,405,405,315,407,409,409,411,411,413,413,414,416,416,417,419,419,421,421,423,423,424,426,426,428,428,429,430,432,432,358,435,435,437,437,185,122,113,441,442,444,445,445,143,448,448,450,450,452,452,454,454,455,457,457,226,460,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,496,497,497,499,500,500,502,503,503,505,505,507,508,508,510,510,512,512,514,514,516,516,518,518,520,521,521,523,523,525,526,526,527,528,530,530,531,533,533,534,536,537,537,538,539,541,541,542,544,545,545,547,547,549,549,550,552,553,553,555,555,556,558,558,560,560,561,563,563,565,565,567,567,569,569,571,571,573,573,575,576,576,578,579,579,581,581,583,584,584,586,586,587,589,589,591,591,593,593,594,596,596,598,598,600,601,601,603,604,604,606,606,608,609,609,611,612,612,614,614,615,617,617,618,620,620,621,623,623,625,625,626,628,628,630,630,631,632,634,635,635,637,637,638,639,640,641,642,643,644,645,646,647,648,649]


evolve_level_barrier_array_bw = [0,16,32,0,16,36,0,16,36,0,7,10,0,7,10,0,18,36,0,20,0,20,0,22,0,0,0,22,0,16,21,0,16,21,0,5,0,5,0,5,0,22,27,21,26,0,24,0,31,0,26,0,28,0,33,0,28,0,5,0,25,30,0,16,21,0,28,33,0,21,26,0,30,0,25,30,0,40,0,37,0,30,35,0,31,0,34,0,38,0,5,0,25,30,0,5,26,0,28,0,30,0,5,0,28,0,0,0,5,35,0,42,47,52,57,0,32,37,33,0,5,0,0,0,0,5,10,0,0,20,0,0,0,0,0,0,0,30,40,0,40,0,0,0,0,0,0,30,55,0,0,0,16,32,0,14,36,0,18,30,0,15,0,20,0,18,0,22,0,0,27,0,10,10,10,10,30,25,0,15,30,0,0,18,0,0,0,18,27,0,40,5,0,5,40,0,0,0,40,0,40,0,0,0,31,0,0,40,0,23,0,0,0,0,0,30,30,0,38,0,33,38,0,25,0,0,0,0,24,0,0,25,0,40,0,0,20,0,30,30,30,0,0,0,0,0,30,55,0,0,0,0,16,36,0,16,36,0,16,36,0,18,0,20,0,7,10,0,10,0,14,19,0,14,19,0,22,0,25,0,20,30,0,22,0,23,0,18,36,0,20,0,0,20,40,0,24,0,15,30,20,0,0,0,32,42,0,37,0,26,0,0,0,0,0,36,26,0,30,0,40,0,33,0,0,32,0,0,35,45,0,32,0,35,0,0,0,0,0,30,0,30,0,36,0,40,0,40,0,5,0,0,0,37,0,37,42,0,0,0,15,42,0,32,44,0,5,0,0,0,0,30,50,0,20,45,0,0,0,0,0,0,0,0,0,0,0,18,32,0,14,36,0,16,36,0,14,34,0,15,0,10,0,15,30,0,10,0,30,0,30,0,20,0,0,21,0,0,26,0,25,0,30,0,0,28,0,5,0,0,0,38,0,10,34,0,33,0,10,10,10,0,0,24,48,0,30,35,0,34,0,40,0,37,0,0,31,0,30,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,36,0,17,36,0,17,36,0,20,0,16,32,0,20,0,30,0,30,0,30,0,30,0,21,32,0,27,0,25,36,0,0,0,31,0,0,25,0,0,25,36,0,0,0,20,0,0,22,30,0,30,0,30,0,0,29,40,0,35,0,0,34,0,39,0,0,34,0,37,0,37,0,36,0,30,0,30,0,32,41,0,32,41,0,35,0,35,47,0,34,0,0,30,0,39,0,40,0,0,36,0,40,0,38,49,0,39,50,0,42,0,41,50,0,38,48,0,37,0,0,30,0,0,50,0,0,43,0,52,0,0,54,0,54,0,0,0,50,64,0,59,0,0,0,0,0,0,0,0,0,0,0,0,0]

doubles_set = {0, 1, 10, 11, 12, 38, 40, 61, 62, 78, 79, 80, 81, 89, 97, 100, 102, 112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,180,181,182,183,184,185,186,189,190,191,192,193,194,195,196,197,198,199,200,201,227,234,235}

def calc_v(trdata, trpoke, double_bool, double_all_bool, mix_it_up_bool, scale_bool):
	
	trainer_array = []
	pokemon_array = []
	
	
	pointer_data = 0
	pointer_poke = 0
	trainer_number = 1

	
	#Search for 0x47 4D 49 46, pointer should be the address of 0x47 plus 0x18 = 24.
	try:
		for j in range(len(trdata)):
				if(trdata[j] == 71 and trdata[j + 1] == 77 and trdata[j + 2] == 73 and trdata[j + 3] == 70):
					pointer_data = j+24
	#did not find, give up and use default
	except:
	#TRdata, start from 0x19B4 = 6580
		#current integer byte-offset for TRdata
		pointer_data = 6580
		
	
	#Fixes BlazeWhite2/VoltBlack2, they need to go forwards a few bytes
	while(trdata[pointer_data] != 0 or trdata[pointer_data+1] != 6):
		pointer_data +=1
	
	#sets proper bound for BW2VB2
	if(pointer_data == 6824):
		max_trainer_index = 843
		#First Pokemon is at 0x1B00
		pointer_poke = 6912 + 2 #first level at 0x1B02 = 6914
	else:
		max_trainer_index = 813
	#check if using an extended trainer index (add later)
	
	#will have bump at the trainer number location
	trainer_bump = []
	
	print("Trainer Pointer starts from: ", pointer_data)
	
	#parse trdata
	while True:
		skip_number = 8
	
		#get the "has items/has moves" booleans
		extra_space_bool = trdata[pointer_data]
		
		#if moves
		if(extra_space_bool & 1 == 1):
			skip_number += 8
		#if items
		if(extra_space_bool & 2 == 2):
			#Pokemon Trainer N gets an extra 2 for some reason
			if(trdata[pointer_data+1] == 40):
				skip_number += 2
			skip_number += 2
		
		#get # of Pokemon, which is the 3rd hex pair on
		number_pokemon = trdata[pointer_data + 3] & 7
		
		#Do battle-type modifying here:
		
		#special trainers (gym leaders, etc.)
		if(double_bool and trdata[pointer_data+1] in doubles_set and number_pokemon >= 2):
			#check if already set to a special battle type
			if(trdata[pointer_data + 2] & 3 == 0):
				trdata[pointer_data + 2] += 1
		#make everything possible double:
		if(double_all_bool and number_pokemon >= 2):
			#check if already set to a special battle type
			if(trdata[pointer_data + 2] & 3 == 0):
				trdata[pointer_data + 2] += 1
		#mix it up
		if(mix_it_up_bool and number_pokemon >= 2):
			#check if already set to a special battle type
			if(trdata[pointer_data + 2] & 3 == 0):
				#if only two Pokemon and won't freeze, just set to Double:
				if(number_pokemon == 2 and trdata[pointer_data+1] in doubles_set):
					trdata[pointer_data + 2] += 1
				#otherwise, randomly assign one of the battle types other than double
				elif(number_pokemon > 2):
					temp = random.randint(0,2)
					#if the outcome is not Double, set battle type to that (definitely won't cause a crash)
					if(temp != 1):
						trdata[pointer_data + 2] += temp
					#if the selection is double, if it won't crash the game, set it to double
					elif(trdata[pointer_data + 1] in doubles_set):
						trdata[pointer_data + 2] += temp
							
					#otherwise, leave the battle as a single battle
						
		#set AI to proper value (highest bit set to 1) for double/triple values (it prevents them from attacking their own Pokemon)
		if(trdata[pointer_data + 2] == 1 or trdata[pointer_data + 2] == 2):
			if(trdata[pointer_data + 12] & 128 == 0):
				trdata[pointer_data + 12] += 128
		
		#write as many skips as the trainer has Pokemon
		pokemon_count = 0
		while True:
			trainer_array.append([trainer_number, skip_number])
			pokemon_count += 1
			if(pokemon_count == number_pokemon):
				break
		
		trainer_bump.append(0)
		
		
		if(trainer_number == max_trainer_index):
			break
		else:
			trainer_number += 1
			pointer_data += 20
	
	
	if(scale_bool):
	

		if(pointer_poke == 0):		
			#offset initial for trpoke = 19AC = 6572
			pointer_poke = 6572 + 2 #first level at 0x19AE = 6574
			
		pokemon_count = 0
		total_pokemon = len(trainer_array)
		

		edit_array = []
		
		#max level
		#sum, number
		max_level_array = [50,1]
		
		level = 0
		#pull all the levels, check that they are good:
		while True:
			while True:
				level = trpoke[pointer_poke]
				if(level == 0 or level > 100):
					#For some reason, some trainer have an FF FF after their last Pokemon. This checks for that
					#in B2W2, it seems the only oddity is sometimes an extra two empty bytes?
					pointer_poke += 2
				else:
					break
			
			#level at address pokemon_count
			edit_array.append([level, pointer_poke])
			
			#keep track of highest and second highest levels, and their counts
			if(level > max_level_array[0]/max_level_array[1]  and level < 95):
				max_level_array[0] += level
				max_level_array[1] += 1
				
			
			#if this is the last Pokemon, break
			if(pokemon_count + 1 >= total_pokemon):
				break
			else:
				#move to the next pokemon
				pointer_poke += trainer_array[pokemon_count][1]
				if(pointer_poke > len(trpoke) - 1):
					total_pokemon -= 1
					break
				#increment the pokemon count
				pokemon_count += 1
				#print(round(pokemon_count/total_pokemon,2))
		
		
		
		
		#calculate level curve
		
		#The level that will the first level mapped to 100
		level_to_100 = max_level_array[0]/max_level_array[1]
		
		#avoid divide by zero, in this case rescaling is minimal anyway
		if(level_to_100 == 100):
			level_to_100 = 99
		
		curve_exponent = 0.35
		
		curve_divisor = level_to_100**(1+curve_exponent)/(100 - level_to_100)
		
		print('Mapping', level_to_100, 'to 100.', 'Curve divisor is', curve_divisor)
		
		
		#modification of Pokemon
		pokemon_count = 0
		while True:
			
		#edit Pokemon Level
			level = edit_array[pokemon_count][0]
			
			#function adds to level L (L^(curve_exponent))/(curve_divisor)*100% of L
			level = level*(1 + (level**curve_exponent)/curve_divisor)
			
			level = min(round(level), 100)
			
			pointer_poke = edit_array[pokemon_count][1]
			
			trpoke[edit_array[pokemon_count][1]] = level
			
			
		#evolve if possible
			low_digits = trpoke[pointer_poke + 2]
			high_digits = trpoke[pointer_poke + 3]*256
			
			index_number = low_digits + high_digits
			
			new_number = index_number
				
			#get the level that Pokemon should be evolved above. recurse in case a non-evolved pokemon is high enough to evolve twice
			while True:
				#get the level this Pokemon should evolve by
				try:
					evolve_level = evolve_level_barrier_array_bw[new_number]
				except:
					print("Error at", trainer_array[pokemon_count][0] + 1)
					break
					
				#if it's high enough, grab the index number of the next stage
				if(level >= evolve_level):
					new_number = evolve_array_bw[new_number]
				else:
					break
				if(new_number == evolve_array_bw[new_number]):
					break
			
			#write new index number if different
			if(new_number != index_number):
				#get low digit
				low_digits = new_number % 256
				high_digits = int((new_number - low_digits)/256)
				
				trpoke[pointer_poke + 2] = low_digits
				trpoke[pointer_poke + 3] = high_digits			
			#if this is the last Pokemon, break
			if(pokemon_count + 1 >= total_pokemon):
				break
			else:
				#increment the pokemon count
				pokemon_count += 1
	return(trpoke, trdata)

def get_files_gen_v(gen_number):

	#for B2W2, trdata is a091, trpoke is a092
	
	#get hex file locations:
	if(gen_number == 5.1):
		trdata_location = askopenfilename(filetypes = (("Select a/0/9/1", "*.*"), ("All Files", "*.*")))
		trpoke_location = askopenfilename(filetypes = (("Select a/0/9/2", "*.*"), ("All Files", "*.*")))
	

		trpoke = bytearray()
		trdata = bytearray()

		#read from file
		with open(trpoke_location, 'rb') as f:
			trpoke_bin = f.read()
		with open(trdata_location, 'rb') as f:
			trdata_bin = f.read()

		#convert the binary data into bytearrays. each index is one hex-pair
		trpoke = bytearray(trpoke_bin)
		trdata = bytearray(trdata_bin)
		return(trdata, trpoke, trpoke_location)
	
	if(gen_number == 5.99):
		trpoke_location = askopenfilename(filetypes = (("Select a/0/9/2", "*.*"), ("All Files", "*.*")))
	

		trpoke = bytearray()

		#read from file
		with open(trpoke_location, 'rb') as f:
			trpoke_bin = f.read()

		#convert the binary data into bytearrays. each index is one hex-pair
		trpoke = bytearray(trpoke_bin)
		return(trpoke, trpoke_location)
	
		
	