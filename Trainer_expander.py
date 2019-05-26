from gen_v_booster import *


#list of base forms in the format [type1, type2, index#]


base_form = [[11,3,1],[9,9,4],[10,10,7],[6,6,10],[6,3,13],[0,2,16],[3,3,29],[3,3,32],[3,2,41],[11,3,43],[10,10,60],[13,13,63],[1,1,66],[11,3,69],[5,4,74],[12,8,81],[7,3,92],[4,5,111],[10,10,116],[0,0,137],[15,15,147],[11,11,152],[9,9,155],[10,10,158],[12,12,172],[0,0,173],[0,0,174],[0,0,175],[12,12,179],[11,2,187],[14,4,220],[12,12,239],[9,9,240],[5,4,246],[11,11,252],[9,9,255],[10,10,258],[6,6,265],[10,11,270],[11,11,273],[13,13,280],[0,0,287],[0,0,293],[0,0,298],[8,5,304],[4,4,328],[14,10,363],[15,15,371],[8,13,374],[11,11,387],[9,9,390],[10,10,393],[0,2,396],[12,12,403],[11,3,406],[0,0,440],[15,4,443],[11,11,495],[9,9,498],[10,10,501],[0,0,506],[0,2,519],[5,5,524],[1,1,532],[10,10,535],[6,11,540],[6,3,543],[4,16,551],[13,13,574],[13,13,577],[14,14,582],[8,8,599],[12,12,602],[7,9,607],[15,15,610],[16,15,633],[11,3,2],[9,9,5],[10,10,8],[6,6,11],[6,3,14],[0,2,17],[0,0,19],[0,2,21],[3,3,23],[12,12,25],[4,4,27],[3,3,30],[3,3,33],[0,0,35],[9,9,37],[0,0,39],[3,2,42],[11,3,44],[6,11,46],[6,3,48],[4,4,50],[0,0,52],[10,10,54],[1,1,56],[9,9,58],[10,10,61],[13,13,64],[1,1,67],[11,3,70],[10,3,72],[5,4,75],[9,9,77],[10,13,79],[12,8,82],[0,2,84],[10,10,86],[3,3,88],[10,10,90],[7,3,93],[5,4,95],[13,13,96],[10,10,98],[12,12,100],[11,13,102],[4,4,104],[0,0,108],[3,3,109],[4,5,112],[0,0,113],[11,11,114],[10,10,117],[10,10,118],[10,10,120],[12,12,125],[9,9,126],[10,10,129],[0,0,133],[5,10,138],[5,10,140],[15,15,148],[11,11,153],[9,9,156],[10,10,159],[0,0,161],[0,2,163],[6,2,165],[6,3,167],[10,12,170],[0,2,176],[13,2,177],[12,12,180],[10,10,183],[11,2,188],[0,0,190],[11,11,191],[6,2,193],[10,4,194],[16,2,198],[7,7,200],[6,6,204],[4,2,207],[0,0,209],[16,14,215],[0,0,216],[9,9,218],[14,4,221],[10,10,223],[16,9,228],[4,4,231],[1,1,236],[14,13,238],[5,4,247],[11,11,253],[9,1,256],[10,4,259],[16,16,261],[0,0,263],[6,6,266],[6,6,268],[10,11,271],[11,16,274],[0,2,276],[10,2,278],[13,13,281],[6,10,283],[11,11,285],[0,0,288],[6,4,290],[0,0,294],[1,1,296],[5,5,299],[0,0,300],[8,5,305],[1,13,307],[12,12,309],[11,3,315],[3,3,316],[10,16,318],[10,10,320],[9,4,322],[13,13,325],[4,15,329],[11,11,331],[0,2,333],[10,4,339],[10,10,341],[4,13,343],[5,11,345],[5,6,347],[10,10,349],[7,7,353],[7,7,355],[13,13,360],[14,14,361],[14,10,364],[10,10,366],[15,15,372],[8,13,375],[11,11,388],[9,1,391],[10,10,394],[0,2,397],[0,0,399],[6,6,401],[12,12,404],[5,5,408],[5,8,410],[6,6,412],[6,2,415],[10,10,418],[11,11,420],[10,10,422],[7,2,425],[0,0,427],[0,0,431],[13,13,433],[3,16,434],[8,13,436],[5,5,438],[13,13,439],[15,4,444],[0,0,446],[1,1,447],[4,4,449],[3,6,451],[3,1,453],[10,10,456],[10,2,458],[11,14,459],[11,11,496],[9,1,499],[10,10,502],[0,0,504],[0,0,507],[16,16,509],[11,11,511],[9,9,513],[10,10,515],[13,13,517],[0,2,520],[12,12,522],[5,5,525],[13,2,527],[4,4,529],[1,1,533],[10,4,536],[6,11,541],[6,3,544],[11,11,546],[11,11,548],[4,16,552],[9,9,554],[6,5,557],[16,1,559],[7,7,562],[10,5,564],[5,2,566],[3,3,568],[16,16,570],[0,0,572],[13,13,575],[13,13,578],[10,2,580],[14,14,583],[0,11,585],[6,6,588],[11,3,590],[10,7,592],[6,12,595],[11,8,597],[8,8,600],[12,12,603],[13,13,605],[7,9,608],[15,15,611],[14,14,613],[6,6,616],[1,1,619],[4,7,622],[16,8,624],[0,2,627],[16,2,629],[16,15,634],[6,9,636],[0,0,115],[0,0,128],[10,14,131],[0,0,132],[10,10,134],[12,12,135],[9,9,136],[5,2,142],[10,13,199],[13,13,201],[0,13,203],[0,0,206],[10,5,222],[14,2,225],[10,2,226],[8,2,227],[0,0,235],[1,1,237],[0,0,241],[16,7,302],[8,8,303],[12,12,311],[12,12,312],[6,6,313],[6,6,314],[0,0,327],[0,0,335],[3,3,336],[5,13,337],[5,13,338],[0,0,351],[0,0,352],[11,2,357],[16,16,359],[10,5,369],[10,10,370],[0,2,441],[7,16,442],[11,11,470],[14,14,471],[12,7,479],[0,0,531],[1,1,538],[1,1,539],[10,10,550],[13,2,561],[12,2,587],[10,10,594],[14,14,615],[4,12,618],[15,15,621],[0,0,626],[9,9,631],[6,8,632],[13,13,151],[13,11,251],[15,13,380],[15,13,381],[8,13,385],[13,13,386],[9,8,485],[13,13,488],[10,10,489],[10,10,490],[16,16,491],[11,11,492],[0,13,648],[14,2,144],[12,2,145],[9,2,146],[12,12,243],[9,9,244],[10,10,245],[5,5,377],[14,14,378],[8,8,379],[13,13,480],[13,13,481],[13,13,482],[0,0,486],[8,1,638],[5,1,639],[11,1,640],[2,2,641],[12,2,642],[4,2,645],[10,1,647]]

#at index i, [type1, type2]

type_index = [[0,0],[11,3],[11,3],[11,3],[9,9],[9,9],[9,2],[10,10],[10,10],[10,10],[6,6],[6,6],[6,2],[6,3],[6,3],[6,3],[0,2],[0,2],[0,2],[0,0],[0,0],[0,2],[0,2],[3,3],[3,3],[12,12],[12,12],[4,4],[4,4],[3,3],[3,3],[3,4],[3,3],[3,3],[3,4],[0,0],[0,0],[9,9],[9,9],[0,0],[0,0],[3,2],[3,2],[11,3],[11,3],[11,3],[6,11],[6,11],[6,3],[6,3],[4,4],[4,4],[0,0],[0,0],[10,10],[10,10],[1,1],[1,1],[9,9],[9,9],[10,10],[10,10],[10,1],[13,13],[13,13],[13,13],[1,1],[1,1],[1,1],[11,3],[11,3],[11,3],[10,3],[10,3],[5,4],[5,4],[5,4],[9,9],[9,9],[10,13],[10,13],[12,8],[12,8],[0,2],[0,2],[0,2],[10,10],[10,14],[3,3],[3,3],[10,10],[10,14],[7,3],[7,3],[7,3],[5,4],[13,13],[13,13],[10,10],[10,10],[12,12],[12,12],[11,13],[11,13],[4,4],[4,4],[1,1],[1,1],[0,0],[3,3],[3,3],[4,5],[4,5],[0,0],[11,11],[0,0],[10,10],[10,10],[10,10],[10,10],[10,10],[10,13],[13,13],[6,2],[14,13],[12,12],[9,9],[6,6],[0,0],[10,10],[10,2],[10,14],[0,0],[0,0],[10,10],[12,12],[9,9],[0,0],[5,10],[5,10],[5,10],[5,10],[5,2],[0,0],[14,2],[12,2],[9,2],[15,15],[15,15],[15,2],[13,13],[13,13],[11,11],[11,11],[11,11],[9,9],[9,9],[9,9],[10,10],[10,10],[10,10],[0,0],[0,0],[0,2],[0,2],[6,2],[6,2],[6,3],[6,3],[3,2],[10,12],[10,12],[12,12],[0,0],[0,0],[0,0],[0,2],[13,2],[13,2],[12,12],[12,12],[12,12],[11,11],[10,10],[10,10],[5,5],[10,10],[11,2],[11,2],[11,2],[0,0],[11,11],[11,11],[6,2],[10,4],[10,4],[13,13],[16,16],[16,2],[10,13],[7,7],[13,13],[13,13],[0,13],[6,6],[6,8],[0,0],[4,2],[8,4],[0,0],[0,0],[10,3],[6,8],[6,5],[6,1],[16,14],[0,0],[0,0],[9,9],[9,5],[14,4],[14,4],[10,5],[10,10],[10,10],[14,2],[10,2],[8,2],[16,9],[16,9],[10,15],[4,4],[4,4],[0,0],[0,0],[0,0],[1,1],[1,1],[14,13],[12,12],[9,9],[0,0],[0,0],[12,12],[9,9],[10,10],[5,4],[5,4],[5,16],[13,2],[9,2],[13,11],[11,11],[11,11],[11,11],[9,9],[9,1],[9,1],[10,10],[10,4],[10,4],[16,16],[16,16],[0,0],[0,0],[6,6],[6,6],[6,2],[6,6],[6,3],[10,11],[10,11],[10,11],[11,11],[11,16],[11,16],[0,2],[0,2],[10,2],[10,2],[13,13],[13,13],[13,13],[6,10],[6,2],[11,11],[11,1],[0,0],[0,0],[0,0],[6,4],[6,2],[6,7],[0,0],[0,0],[0,0],[1,1],[1,1],[0,0],[5,5],[0,0],[0,0],[16,7],[8,8],[8,5],[8,5],[8,5],[1,13],[1,13],[12,12],[12,12],[12,12],[12,12],[6,6],[6,6],[11,3],[3,3],[3,3],[10,16],[10,16],[10,10],[10,10],[9,4],[9,4],[9,9],[13,13],[13,13],[0,0],[4,4],[4,15],[4,15],[11,11],[11,16],[0,2],[15,2],[0,0],[3,3],[5,13],[5,13],[10,4],[10,4],[10,10],[10,16],[4,13],[4,13],[5,11],[5,11],[5,6],[5,6],[10,10],[10,10],[0,0],[0,0],[7,7],[7,7],[7,7],[7,7],[11,2],[13,13],[16,16],[13,13],[14,14],[14,14],[14,10],[14,10],[14,10],[10,10],[10,10],[10,10],[10,5],[10,10],[15,15],[15,15],[15,2],[8,13],[8,13],[8,13],[5,5],[14,14],[8,8],[15,13],[15,13],[10,10],[4,4],[15,2],[8,13],[13,13],[11,11],[11,11],[11,4],[9,9],[9,1],[9,1],[10,10],[10,10],[10,8],[0,2],[0,2],[0,2],[0,0],[0,10],[6,6],[6,6],[12,12],[12,12],[12,12],[11,3],[11,3],[5,5],[5,5],[5,8],[5,8],[6,6],[6,11],[6,2],[6,2],[6,2],[12,12],[10,10],[10,10],[11,11],[11,11],[10,10],[10,4],[0,0],[7,2],[7,2],[0,0],[0,0],[7,7],[16,2],[0,0],[0,0],[13,13],[3,16],[3,16],[8,13],[8,13],[5,5],[13,13],[0,0],[0,2],[7,16],[15,4],[15,4],[15,4],[0,0],[1,1],[1,8],[4,4],[4,4],[3,6],[3,16],[3,1],[3,1],[11,11],[10,10],[10,10],[10,2],[11,14],[11,14],[16,14],[12,8],[0,0],[4,5],[11,11],[12,12],[9,9],[0,2],[6,2],[11,11],[14,14],[4,2],[14,4],[0,0],[13,1],[5,8],[7,7],[14,7],[12,7],[13,13],[13,13],[13,13],[8,15],[10,15],[9,8],[0,0],[7,15],[13,13],[10,10],[10,10],[16,16],[11,11],[0,0],[13,9],[11,11],[11,11],[11,11],[9,9],[9,1],[9,1],[10,10],[10,10],[10,10],[0,0],[0,0],[0,0],[0,0],[0,0],[16,16],[16,16],[11,11],[11,11],[9,9],[9,9],[10,10],[10,10],[13,13],[13,13],[0,2],[0,2],[0,2],[12,12],[12,12],[5,5],[5,5],[5,5],[13,2],[13,2],[4,4],[4,8],[0,0],[1,1],[1,1],[1,1],[10,10],[10,4],[10,4],[1,1],[1,1],[6,11],[6,11],[6,11],[6,3],[6,3],[6,3],[11,11],[11,11],[11,11],[11,11],[10,10],[4,16],[4,16],[4,16],[9,9],[9,9],[11,11],[6,5],[6,5],[16,1],[16,1],[13,2],[7,7],[7,7],[10,5],[10,5],[5,2],[5,2],[3,3],[3,3],[16,16],[16,16],[0,0],[0,0],[13,13],[13,13],[13,13],[13,13],[13,13],[13,13],[10,2],[10,2],[14,14],[14,14],[14,14],[0,11],[0,11],[12,2],[6,6],[6,8],[11,3],[11,3],[10,7],[10,7],[10,10],[6,12],[6,12],[11,8],[11,8],[8,8],[8,8],[8,8],[12,12],[12,12],[12,12],[13,13],[13,13],[7,9],[7,9],[7,9],[15,15],[15,15],[15,15],[14,14],[14,14],[14,14],[6,6],[6,6],[4,12],[1,1],[1,1],[15,15],[4,7],[4,7],[16,8],[16,8],[0,0],[0,2],[0,2],[16,2],[16,2],[9,9],[6,8],[16,15],[16,15],[16,15],[6,9],[6,9],[8,1],[5,1],[11,1],[2,2],[12,2],[15,9],[15,12],[4,2],[15,14],[10,1],[0,13],[6,8]]


trainer_offset = [0, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 18, 18, 18, 18, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 18, 8, 16, 18, 18, 18, 18, 8, 8, 8, 8, 8, 8, 18, 18, 18, 16, 16, 18, 18, 18, 8, 8, 8, 8, 8, 16, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 8, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 16, 8, 8, 16, 8, 8, 8, 8, 8, 16, 16, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8, 18, 8, 8, 18, 18, 8, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 18, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 10, 10, 10, 8, 18, 18, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 16, 16, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 16, 16, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 18, 18, 18, 16, 16, 16, 8, 8, 8, 16, 18, 18, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 16, 16, 18, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 8, 8, 8, 10, 8, 18, 16, 16, 8, 8, 8, 10, 10, 10, 18, 18, 8, 16, 16, 16, 16, 16, 16, 16, 8, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 8, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 18, 18, 18, 16, 16, 16, 8, 8, 8, 18, 18, 18, 18, 18, 18, 8, 16, 10, 10, 10, 8, 8, 16, 16, 16, 18, 18, 18, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 18, 18, 18, 18, 18, 18, 8, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 18]


#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = "", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)

def expand(trpoke):
	
	trainer_array = []
	pokemon_array = []
	
	pointer_poke = 0
	trainer_number = 1
	trainer_party = 1

	pointer_data = 6580
	max_trainer_index = 813




	pointer_poke = 6572 #first at 0x19AC = 6572
		
	pokemon_count = 0
	total_pokemon = 813 * 6
	
	last_skip = 0

	edit_array = []
	
	#pull all the levels, check that they are good:
	while True:
		
		skip_number = trainer_offset[trainer_number]
		
		#pointer_poke + 2 is low, pointer_poke + 3 is high
		
		#check if the current Pokemon is blank
		if(trpoke[pointer_poke + 4] == 0 and trpoke[pointer_poke + 5] == 0):
			#copy the difficulty
			trpoke[pointer_poke] = trpoke[pointer_poke - last_skip] 
			
			#copy the gender/ability
			trpoke[pointer_poke + 1] = trpoke[pointer_poke + 1 - last_skip] 
			
			#copy the level
			lvl = min(max(trpoke[pointer_poke + 2 - last_skip] + random.randint(-2,2), 1),100)
			
			if(lvl >= 100 or lvl == 0):
				print("problem at", pointer_poke)
			
			trpoke[pointer_poke + 2] = lvl
			
			
			#get the previous Pokemon index #
			last_index = trpoke[pointer_poke + 4 - last_skip]
			last_index += 256*trpoke[pointer_poke + 5 - last_skip]
			
			#get the types
			type1 = type_index[last_index][0]
			type2 = type_index[last_index][1]
			
			#get the list of pokemon with the same type1 or type2
			temp_index = []
			for thing in base_form:
				if(thing[0] == type1 or thing[1] == type2 or thing[0] == type2 and thing[1] == type1):
					temp_index.append(thing[2])
			
			#if this is a unique type combo, just use the same one again
			if(len(temp_index) == 1):
				output_index = last_index
			else:
				#choose a random pokemon out of the temp_index
				output_index = temp_index[random.randint(0, len(temp_index) - 1)]
			
			print("trainer", trainer_number, 'as party member number', trainer_party, "added", output_index, 'difficulty', trpoke[pointer_poke], 'gender', trpoke[pointer_poke + 1], 'level', trpoke[pointer_poke + 2])
			
			
			
			#write new index number
			trpoke[pointer_poke + 4] = output_index%256
			
			trpoke[pointer_poke + 5] = int((output_index - output_index%256)/256)
			
			
			#item or move 1
			if(skip_number > 8):
				trpoke[pointer_poke + 8] = trpoke[pointer_poke + 8 - last_skip]
				trpoke[pointer_poke + 9] = trpoke[pointer_poke + 9 - last_skip]
			
			#move 1/2
			if(skip_number > 10):
				trpoke[pointer_poke + 10] = trpoke[pointer_poke + 10 - last_skip]
				trpoke[pointer_poke + 11] = trpoke[pointer_poke + 11 - last_skip]
			
			#move 2/3
			if(skip_number > 10):
				trpoke[pointer_poke + 12] = trpoke[pointer_poke + 12 - last_skip]
				trpoke[pointer_poke + 13] = trpoke[pointer_poke + 13 - last_skip]
			
			#move 3/4
			if(skip_number > 10):
				trpoke[pointer_poke + 14] = trpoke[pointer_poke + 14 - last_skip]
				trpoke[pointer_poke + 15] = trpoke[pointer_poke + 15 - last_skip]
			
			#move 4
			if(skip_number > 14):
				trpoke[pointer_poke + 16] = trpoke[pointer_poke + 16 - last_skip]
				trpoke[pointer_poke + 17] = trpoke[pointer_poke + 17 - last_skip]
				
			
		
		
		
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#move to the next pokemon
			last_skip = trainer_offset[trainer_number]
			pointer_poke += last_skip
			#increment the pokemon count
			pokemon_count += 1
			
			#if we just did the 6th Pokemon, move to the next trainer:
			if(trainer_party == 6):
				trainer_party = 1
				trainer_number += 1
			#otherwise, move to the next party member
			else:
				trainer_party += 1
	
	return(trpoke)

def main():
	
	gen_number = 5.1
	
	#get the files using the TLB
	
	trpoke, output_path = get_files_gen_v(5.99)
	
	trpoke = expand(trpoke)

	save_binary_file(trpoke, '2.narc', output_path)

main()