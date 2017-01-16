Lily = {"Age" : "22",
        "City" : "Beijing",
        "School" : "PKU",
        "Job" : "Teacher",}
Charly = {"Age" : "41",
          "City" : "Shenzhen",
          "School" : "DUT",
          "Job" : "Docter",}
Bob = {"Age" : "32",
       "City" : "Haerbin",
       "School" : "NTU",
       "Job" : "Manager"}
classmates = [Lily, Charly, Bob]
for classmate in classmates:
	print(classmate)

favor_places = {"Lily" : "Beijing, Shanghai, Kunming",
                "Charly" : "Huanggang, Xian, Zhuhai",
                "Bob" : "Nanjing, Wuhan, Liuzhou",}
for key,value in favor_places.items():
	print(key+" 's favorite citys are : "+value+".")

cities = {
         "Beijing" : {"country" : "china",
           "population" : "45789029",
           "mark" : "The Palace Museum",
           "areacode" : "010",
           "privoce" : "Beijing",},
	     "Kunming" : {"country" : "china",
           "populstion" : "3098742",
           "mark" : "Golden Horse and Jade Rooster ",
           "areacode" : "0871",
           "privoce" : "Yunnan",},
		 "Shenyang" : {"country" : "china",
           "populstion" : "5623723",
           "mark" : "Dongbeihua",
           "areacode" : "024",
           "privoce" : "Liaoning",},
		}
for  city,city_info in cities.items():
	print("\nI am from "+city+", and this city's information is in "+city_info['country']+" "+city_info['privoce']+". The areacode is "+city_info['areacode']+". And the mark is "+city_info['mark']+".")    
