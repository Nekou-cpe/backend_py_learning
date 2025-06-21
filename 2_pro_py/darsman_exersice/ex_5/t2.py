
city_List = ["city1","city2","city3","city4","city5","city6"]
population_List = [300000,1000000,3800000,500000,1900000,100000]
area_List_squarekilometer = [100,200,500,150,300,100]
area_List_hektar=[i*100 for i in area_List_squarekilometer]

def tarakom(population,hektar):
    tarakom_list=[]
    for p in population:
        for h in hektar:
            tarakom_list.append(int(p/h))
    return tarakom_list

def show_tarakom(cityList,tarkomList):
    city_destiny={city:destiny for city , destiny in zip(cityList,tarkomList)}
    for c,d in city_destiny.items():
        print(c,'\t',d)
    return city_destiny

tarakom_dict=show_tarakom(city_List,tarakom(population_List,area_List_hektar)) 
high_tarakom_dict={city:destiny for city,destiny in tarakom_dict.items() if destiny>=50 }
for c,d in high_tarakom_dict.items():
    print(c,'\t',d)