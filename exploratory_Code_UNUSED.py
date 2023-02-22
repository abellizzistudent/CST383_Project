"""
We need to code each breed with a numeric value. Here is where breeds from df_md and df_be are compared for duplicates, duplicates were removed, and the remaining list of unique breed_group values across both datasets are assigned a numeric value. The values are stored in df_breeds
"""

#Compare breed names used in NY and SF data files to those in the enriched breed

#sfBreeds = pd.Series(df_sf['breed_group'])
#nyBreeds = pd.Series(df_ny['breed_group'])
breeds = pd.Series(df_be['breed_group'])
df_breeds = pd.Series(df_md['breed_group'])

ser = pd.Series(dtype='object')
#ser = ser.append(sfBreeds.str.lower())
#ser = ser.append(nyBreeds.str.lower())
ser = ser.append(breeds.str.upper())
ser = ser.append(df_breeds.str.upper())
#print(ser.unique())

a = df_md['breed_group'].unique()
#print(sorted(a))
#print(df_md.breed_group.unique().sort_values())
b = df_be['breed_group'].str.upper().unique()
#print(sorted(b))

d = {
    'breed_code':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,
                  28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,
                  52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,
                  76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,
                  100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,
                  118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,
                  136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,
                  154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,
                  172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,
                  190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,
                  208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,
                  226,227,228,229,230,231,232,233,234,235,236,237,238,239,240],
    'breed_group':['AFFENPINSCHER', 'AFGHAN HOUND', 'AIDI', 'AIREDALE TERR', 'AKBASH DOG',
                   'AKITA', 'ALASK KLEE KAI', 'ALASK MALAMUTE', 'ALASKAN HUSKY', 'AMER BULLDOG',
                   'AMER ESKIMO', 'AMER FOXHOUND', 'AMERICAN BULLY', 'AMERICAN COCKER SPANIEL',
                   'AMERICAN ESKIMO DOG', 'AMERICAN FOXHOUND', 'AMERICAN HAIRLESS TERRIER', 
                   'AMERICAN LEOPARD HOUND', 'AMERICAN PIT BULL TERRIER', 'AMERICAN STAFFORDSHIRE TERRIER',
                   'AMERICAN WATER SPANIEL', 'ANATOL SHEPHERD', 'AUST CATTLE DOG', 'AUST KELPIE',
                   'AUST SHEPHERD', 'AUST TERRIER', 'AUSTRALIAN CATTLE DOG', 'AUSTRALIAN KELPIE', 'AUSTRALIAN SHEPHERD',
                   'BARBET', 'BASENJI', 'BASSET HOUND', 'BEAGLE', 'BEARDED COLLIE', 'BEAUCERON', 'BEDLINGTON TERRIER',
                   'BELG MALINOIS', 'BELG SHEEPDOG', 'BERNESE HOUND', 'BERNESE MTN DOG', 'BICHON FRISE', 'BLACK & TAN COONHOUND',
                   'BLACK MOUTH CUR', 'BLACK RUSSIAN TERRIER', 'BLOODHOUND', 'BLUETICK COONHOUND', 'BORDER COLLIE',
                   'BORDER TERRIER', 'BORZOI', 'BOSTON TERRIER', 'BOUV FLANDRES', 'BOXER', 'BOYKIN SPANIEL', 'BRIARD',
                   'BRITTANY', 'BRUSS GRIFFON', 'BULL TERR MIN', 'BULL TERRIER', 'BULLDOG', 'BULLMASTIFF', 'CAIRN TERRIER',
                   'CANAAN DOG', 'CANE CORSO', 'CARDIGAN WELSH CORGI', 'CAROLINA DOG', 'CATAHOULA', 'CAVALIER SPAN',
                   'CHESA BAY RETR', 'CHIHUAHUA', 'CHINESE CRESTED', 'CHINESE SHARPEI', 'CHOW CHOW', 'CLUMBER SPANIEL', 
                   'COCKER SPAN', 'COLLIE ROUGH', 'COLLIE SMOOTH', 'COTON DE TULEAR', 'COYOTE HYBRID', 'CURLY COATED RETRIEVER', 
                   'DACHSHUND', 'DALMATIAN', 'DANDIE DINMONT TERRIER', 'DANISH-SWEDISH FARMDOG', 'DOBERMAN PINSCH',
                   'DOGO ARGENTINO', 'DOGUE DE BORDX', 'DUTCH SHEEPDOG', 'DUTCH SHEPHERD', 'ENG BULLDOG', 'ENG COCKER SPAN',
                   'ENG POINTER', 'ENG SHEPHERD', 'ENG SPRNGR SPAN', 'ENGLISH BULLDOG', 'ENGLISH COONHOUND', 
                   'ENGLISH FOXHOUND', 'ENGLISH SETTER', 'ENGLISH SHEPHERD', 'ENGLISH TOY SPANIEL', 'FIELD SPANIEL', 
                   'FINNISH SPITZ', 'FLAT COAT RETR', 'FOX TERR SMOOTH', 'FOX TERR WIRE', 'FRENCH BULLDOG', 'GERM SH POINT',
                   'GERM SHEPHERD', 'GERM WH POINT', 'GERMAN LONGHAIRED POINTER', 'GERMAN PINSCHER', 'GERMAN SHEPHERD DOG', 
                   'GERMAN SHORTHAIRED POINTER', 'GERMAN WH POINT', 'GIANT SCHNAUZER', 'GLEN OF IMAAL TERRIER', 'GOLDEN RETR',
                   'GORDON SETTER', 'GREAT DANE', 'GREAT PYRENEES', 'GREATER SWISS MOUNTAIN DOG', 'GREYHOUND', 'HARRIER', 
                   'HAVANESE', 'IBIZAN HOUND', 'IRISH SETTER', 'IRISH TERRIER', 'IRISH WATER SPANIEL', 'IRISH WOLFHOUND', 
                   'ITALIAN GREYHOUND', 'JACK RUSS TERR', 'JAPANESE CHIN', 'JINDO', 'KANGAL', 'KEESHOND', 'KERRY BLUE TERRIER', 
                   'KOMONDOR', 'KUVASZ', 'LABRADOR RETR', 'LAKELAND TERRIER', 'LHASA APSO', 'MALTESE', 'MANCHESTER TERR', 'MASTIFF',
                   'MEX HAIRLESS', 'MIN PINSCHER', 'MINIATURE BULL TERRIER', 'MINIATURE PINSCHER', 'MIX', 'NEAPOLITAN MASTIFF',
                   'NEDERLANDSE KOOIKERHONDJE', 'NEWFOUNDLAND', 'NORFOLK TERRIER', 'NORRBOTTENSPETS', 'NORWEGIAN ELKHOUND', 
                   'NORWICH TERRIER', 'NOVA SCOTIA DUCK TOLLING RETRIEVER', 'NS DUCK TOLLING', 'OLDE ENGLISH BULLDOGGE', 
                   'OLDENG SHEEPDOG', 'OTHER', 'OTTERHOUND', 'PAPILLON', 'PARSON RUSS TER', 'PATTERDALE TERRIER', 'PEKINGESE',
                   'PEMBROKE WELSH CORGI', 'PERRO DE PRESA CANARIO', 'PERUVIAN INCA ORCHID', 'PETIT BASSET GRIFFON VENDEEN', 
                   'PHARAOH HOUND', 'PIT BULL', 'PLOTT HOUND', 'POINTER', 'POLISH LOWLAND SHEEPDOG', 'POMERANIAN', 'POODLE MIN',
                   'POODLE STND', 'POODLE TOY', 'PORT WATER DOG', 'PRESA CANARIO', 'PUG', 'PULI', 'PUMI', 'RAT TERRIER', 
                   'REDBONE HOUND', 'RETRIEVER', 'RHOD RIDGEBACK', 'ROTTWEILER', 'SAINT BERNARD', 'SALUKI', 'SAMOYED', 
                   'SC WHEAT TERR', 'SCHAPENDOES', 'SCHIPPERKE', 'SCHNAUZER', 'SCHNAUZER GIANT', 'SCHNAUZER MIN', 'SCHNAUZER STAND', 
                   'SCOT TERRIER', 'SCOTTISH DEERHOUND', 'SEALYHAM TERRIER', 'SHARPEI', 'SHETLD SHEEPDOG', 'SHIBA INU', 'SHIH TZU',
                   'SIBERIAN HUSKY', 'SILKY TERRIER', 'SKYE TERRIER', 'SMOOTH FOX TERRIER', 'SOFT-COATED', 'SPANIEL', 'SPINONE ITALIANO',
                   'ST BERNARD RGH', 'STAFFORDSHIRE', 'SUSSEX SPANIEL', 'SWISS HOUND', 'TERRIER', 'TIBETAN MASTIFF', 'TIBETAN SPANIEL',
                   'TIBETAN TERR', 'TOY FOX TERRIER', 'TR WALKER HOUND', 'TREEING TENNESSEE BRINDLE', 'TREEING WALKER COONHOUND',
                   'UNKNOWN', 'VIZSLA', 'WEIMARANER', 'WELSH CORGI', 'WELSH CORGI CAR', 'WELSH CORGI PEM', 'WELSH SPRINGER SPANIEL',
                   'WELSH TERRIER', 'WEST HIGHLAND', 'WEST HIGHLAND WHITE TERRIER', 'WH PT GRIFFON', 'WHEATEN TERRIER', 'WHIPPET',
                   'WIRE FOX TERRIER', 'WIREHAIRED POINTING GRIFFON', 'YORKSHIRE TERR']
}
df_breeds = pd.DataFrame(d)
df_breeds.info()
#df_be['breed_group'] = df_be['breed_group'].str.upper()




#A more elegant way to do the same as above, but still does not solve how to add breed_code to wach row in df_md

#code from https://stackoverflow.com/questions/68111941/how-to-assign-numeric-values-to-multile-strings-in-a-dataframe-column-using-pyth

breed_strings = ('AFFENPINSCHER', 'AFGHAN HOUND', 'AIDI', 'AIREDALE TERR', 'AKBASH DOG',
                   'AKITA', 'ALASK KLEE KAI', 'ALASK MALAMUTE', 'ALASKAN HUSKY', 'AMER BULLDOG',
                   'AMER ESKIMO', 'AMER FOXHOUND', 'AMERICAN BULLY', 'AMERICAN COCKER SPANIEL',
                   'AMERICAN ESKIMO DOG', 'AMERICAN FOXHOUND', 'AMERICAN HAIRLESS TERRIER', 
                   'AMERICAN LEOPARD HOUND', 'AMERICAN PIT BULL TERRIER', 'AMERICAN STAFFORDSHIRE TERRIER',
                   'AMERICAN WATER SPANIEL', 'ANATOL SHEPHERD', 'AUST CATTLE DOG', 'AUST KELPIE',
                   'AUST SHEPHERD', 'AUST TERRIER', 'AUSTRALIAN CATTLE DOG', 'AUSTRALIAN KELPIE', 'AUSTRALIAN SHEPHERD',
                   'BARBET', 'BASENJI', 'BASSET HOUND', 'BEAGLE', 'BEARDED COLLIE', 'BEAUCERON', 'BEDLINGTON TERRIER',
                   'BELG MALINOIS', 'BELG SHEEPDOG', 'BERNESE HOUND', 'BERNESE MTN DOG', 'BICHON FRISE', 'BLACK & TAN COONHOUND',
                   'BLACK MOUTH CUR', 'BLACK RUSSIAN TERRIER', 'BLOODHOUND', 'BLUETICK COONHOUND', 'BORDER COLLIE',
                   'BORDER TERRIER', 'BORZOI', 'BOSTON TERRIER', 'BOUV FLANDRES', 'BOXER', 'BOYKIN SPANIEL', 'BRIARD',
                   'BRITTANY', 'BRUSS GRIFFON', 'BULL TERR MIN', 'BULL TERRIER', 'BULLDOG', 'BULLMASTIFF', 'CAIRN TERRIER',
                   'CANAAN DOG', 'CANE CORSO', 'CARDIGAN WELSH CORGI', 'CAROLINA DOG', 'CATAHOULA', 'CAVALIER SPAN',
                   'CHESA BAY RETR', 'CHIHUAHUA', 'CHINESE CRESTED', 'CHINESE SHARPEI', 'CHOW CHOW', 'CLUMBER SPANIEL', 
                   'COCKER SPAN', 'COLLIE ROUGH', 'COLLIE SMOOTH', 'COTON DE TULEAR', 'COYOTE HYBRID', 'CURLY COATED RETRIEVER', 
                   'DACHSHUND', 'DALMATIAN', 'DANDIE DINMONT TERRIER', 'DANISH-SWEDISH FARMDOG', 'DOBERMAN PINSCH',
                   'DOGO ARGENTINO', 'DOGUE DE BORDX', 'DUTCH SHEEPDOG', 'DUTCH SHEPHERD', 'ENG BULLDOG', 'ENG COCKER SPAN',
                   'ENG POINTER', 'ENG SHEPHERD', 'ENG SPRNGR SPAN', 'ENGLISH BULLDOG', 'ENGLISH COONHOUND', 
                   'ENGLISH FOXHOUND', 'ENGLISH SETTER', 'ENGLISH SHEPHERD', 'ENGLISH TOY SPANIEL', 'FIELD SPANIEL', 
                   'FINNISH SPITZ', 'FLAT COAT RETR', 'FOX TERR SMOOTH', 'FOX TERR WIRE', 'FRENCH BULLDOG', 'GERM SH POINT',
                   'GERM SHEPHERD', 'GERM WH POINT', 'GERMAN LONGHAIRED POINTER', 'GERMAN PINSCHER', 'GERMAN SHEPHERD DOG', 
                   'GERMAN SHORTHAIRED POINTER', 'GERMAN WH POINT', 'GIANT SCHNAUZER', 'GLEN OF IMAAL TERRIER', 'GOLDEN RETR',
                   'GORDON SETTER', 'GREAT DANE', 'GREAT PYRENEES', 'GREATER SWISS MOUNTAIN DOG', 'GREYHOUND', 'HARRIER', 
                   'HAVANESE', 'IBIZAN HOUND', 'IRISH SETTER', 'IRISH TERRIER', 'IRISH WATER SPANIEL', 'IRISH WOLFHOUND', 
                   'ITALIAN GREYHOUND', 'JACK RUSS TERR', 'JAPANESE CHIN', 'JINDO', 'KANGAL', 'KEESHOND', 'KERRY BLUE TERRIER', 
                   'KOMONDOR', 'KUVASZ', 'LABRADOR RETR', 'LAKELAND TERRIER', 'LHASA APSO', 'MALTESE', 'MANCHESTER TERR', 'MASTIFF',
                   'MEX HAIRLESS', 'MIN PINSCHER', 'MINIATURE BULL TERRIER', 'MINIATURE PINSCHER', 'MIX', 'NEAPOLITAN MASTIFF',
                   'NEDERLANDSE KOOIKERHONDJE', 'NEWFOUNDLAND', 'NORFOLK TERRIER', 'NORRBOTTENSPETS', 'NORWEGIAN ELKHOUND', 
                   'NORWICH TERRIER', 'NOVA SCOTIA DUCK TOLLING RETRIEVER', 'NS DUCK TOLLING', 'OLDE ENGLISH BULLDOGGE', 
                   'OLDENG SHEEPDOG', 'OTHER', 'OTTERHOUND', 'PAPILLON', 'PARSON RUSS TER', 'PATTERDALE TERRIER', 'PEKINGESE',
                   'PEMBROKE WELSH CORGI', 'PERRO DE PRESA CANARIO', 'PERUVIAN INCA ORCHID', 'PETIT BASSET GRIFFON VENDEEN', 
                   'PHARAOH HOUND', 'PIT BULL', 'PLOTT HOUND', 'POINTER', 'POLISH LOWLAND SHEEPDOG', 'POMERANIAN', 'POODLE MIN',
                   'POODLE STND', 'POODLE TOY', 'PORT WATER DOG', 'PRESA CANARIO', 'PUG', 'PULI', 'PUMI', 'RAT TERRIER', 
                   'REDBONE HOUND', 'RETRIEVER', 'RHOD RIDGEBACK', 'ROTTWEILER', 'SAINT BERNARD', 'SALUKI', 'SAMOYED', 
                   'SC WHEAT TERR', 'SCHAPENDOES', 'SCHIPPERKE', 'SCHNAUZER', 'SCHNAUZER GIANT', 'SCHNAUZER MIN', 'SCHNAUZER STAND', 
                   'SCOT TERRIER', 'SCOTTISH DEERHOUND', 'SEALYHAM TERRIER', 'SHARPEI', 'SHETLD SHEEPDOG', 'SHIBA INU', 'SHIH TZU',
                   'SIBERIAN HUSKY', 'SILKY TERRIER', 'SKYE TERRIER', 'SMOOTH FOX TERRIER', 'SOFT-COATED', 'SPANIEL', 'SPINONE ITALIANO',
                   'ST BERNARD RGH', 'STAFFORDSHIRE', 'SUSSEX SPANIEL', 'SWISS HOUND', 'TERRIER', 'TIBETAN MASTIFF', 'TIBETAN SPANIEL',
                   'TIBETAN TERR', 'TOY FOX TERRIER', 'TR WALKER HOUND', 'TREEING TENNESSEE BRINDLE', 'TREEING WALKER COONHOUND',
                   'UNKNOWN', 'VIZSLA', 'WEIMARANER', 'WELSH CORGI', 'WELSH CORGI CAR', 'WELSH CORGI PEM', 'WELSH SPRINGER SPANIEL',
                   'WELSH TERRIER', 'WEST HIGHLAND', 'WEST HIGHLAND WHITE TERRIER', 'WH PT GRIFFON', 'WHEATEN TERRIER', 'WHIPPET',
                   'WIRE FOX TERRIER', 'WIREHAIRED POINTING GRIFFON', 'YORKSHIRE TERR')

bridge_df = pd.DataFrame(breed_strings, columns=['breed_group'])

# converting type of columns to 'category'
bridge_df['breed_group'] = bridge_df['breed_group'].astype('category')

# Assigning numerical values and storing in another column
bridge_df['breed_group_code'] = bridge_df['breed_group'].cat.codes

bridge_df.head()

#######################################
df_breedsF = pd.concat([df_breeds, df_md], axis=1, join='inner')
#df_breedsF = df_breedsF.dropna()
#df_breedsF['gender']=df_breedsF['gender'].astype(float)

df_breedsF.info()
#reset index of both frames didn't work
#Seemed to have worked

###########################################
df_breedsF = df_breedsF.fillna(0)
df_breedsF['gender'] = df_breedsF['gender'].astype(int)
print(df_breedsF['gender'].dtype)
#changed gender to int!

df_breedsF.info()
#NOOOOOOOO idk why it keeps clearing the data

##########################################
df_beavg = pd.DataFrame({'breed_group': ['PIT BULL', 'BASENJI', 'GREAT DANE', 'POODLE MIN', 'PEKINGESE', 'DACHSHUND', 'CHIHUAHUA', 'YORKSHIRE TERR', 'SHIH TZU', 'PUG', 'MALTESE', 'BICHON FRISE', 'GERM SHEPHERD', 'LABRADOR RETR', 'ROTTWEILER', 'NORFOLK TERRIER', 'COCKER SPAN', 
                                         'SIBERIAN HUSKY', 'BOXER', 'BEAGLE', 'JACK RUSS TERR', 'LHASA APSO', 'AKITA', 'CANE CORSO', 'DACHSHUND', 'SHIBA INU', 'FRENCH BULLDOG', 'TERRIER', 'BULLDOG', 'ENG BULLDOG', 'BOSTON TERRIER', 'WEST HIGHLAND', 
                                         'AUST CATTLE DOG', 'POMERANIAN', 'GREYHOUND', 'MIN PINSCHER',  'COLLIE ROUGH', 'BASENJI', 'TIBETAN TERR','SC WHEAT TERR', 'DOBERMAN PINSCH', 'SAMOYED', 'CAIRN TERRIER', 
                                         'HAVANESE', 'BEAGLE', 'BULLDOG', 'CHOW CHOW', 'NEWFOUNDLAND', 'RAT TERRIER', 'DALMATIAN', 'BULLMASTIFF', 'WEIMARANER'],
                         'average_height': [20, 16.5, 31, 20, 9, 13, 7.5, 7, 9.5, 12, 8.5, 10.5, 23.5, 23, 24.5, 9.5, 18.5, 
                                            21.5, 23, 15, 11, 10.5, 27, 25.5, 13, 15, 12, 15, 14.5, 14.5, 15.5, 11,
                                            18, 9.5, 28.5, 11.5, 23, 16.5, 15.5, 18.5, 26.5, 21.5, 25.5, 
                                            10, 15, 14.5, 20, 27, 16.75, 21.5, 25.5, 25],
                         'average_weight': [45, 22.5, 149.5, 55,10, 22,4, 5.5, 13.5, 16, 16.5, 12.5, 69, 65.3, 112.5, 11, 70, 
                                            47.5, 67.5, 26.5, 13.5, 13, 100, 95,22,  20,22, 20.5,  49, 49, 18.5, 18.5, 
                                            41, 5, 65, 10.5, 16, 22.5, 24, 35, 80, 15,110,  
                                            10.5, 26.5, 49, 57.5,126, 50, 58, 110, 72.5],
                         'average_lifespan': [11, 13.5, 8.5, 14, 13, 14, 15, 13, 14, 14, 13.5, 14.5, 13, 11, 9.5, 14, 11, 
                                              13, 11, 12.5, 13, 13.5, 11.5, 10.5, 14, 14.5, 11, 15.5, 9, 9, 12, 14,
                                              14, 14, 11.5, 14, 13, 13, 15.5, 13, 11, 13, 8, 
                                              15, 12.5, 9, 10, 9.5, 13, 12, 8, 11.5]})

#df_finalF = pd.merge(df_md, df_final)
#MAYBE USE CONCAT INSTEAD OF MERGE

#CONVERT EVERYTHING TO NUMBERS
df_final = pd.concat([df_beavg, df_md])
df_final.info()
df_final.head(15)

#SOME HEIGHT WEIGHT DATA IS ALREADY IN df_md
# condition mask
mask = df_md['breed_group'] == 'ALASKAN HUSKY'
 
# new dataframe with selected rows
df_new = pd.DataFrame(df_md[mask])
 
print(df_new)

####################################################################

#print(df_be['breed_group'])