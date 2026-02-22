# This function works, but not as I wish. I still need to order by name of country wuen they are even in medals
def count_medals_v_01(winners):
    # Create an empty dictionary
    country_medals_dic = {}
    # Iterate over each list of places
    for places in winners:
        # create a medal pointer to define the color of the medal
        medal = 0
        # iterate over each country in the list of places
        for country in places:
            # if the country is not in the dictionary
            if not country in country_medals_dic:
                # add new country
                country_medals_dic[country] = [0,0,0]
            # assign medal to the country in the right color
            country_medals_dic[country][medal]+=1
            # point to the next medal
            medal +=1
    # sort the dictionay by medals colors and stored in a tuple
    sorted_tuple = (sorted(country_medals_dic.items(), key=lambda medal: medal[1], reverse=True))
    # Init variable str_to_return
    str_to_return = 'Country,Gold,Silver,Bronze,Total\n'
    # Iterate over each sorted element in the tuple and fill out the string to return 
    for item in sorted_tuple:
        str_to_return += item[0] + ',' + str(item[1][0]) + ','+ str(item[1][1]) + ','+ str(item[1][2]) + ','+ str(sum(item[1])) + '\n'
    # return answer
    return str_to_return.strip()

def count_medals(winners):

    return winners


if __name__ == '__main__':
    print(count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]))
    print('-------------------------------')
    print(count_medals([["NOR","SWE","FIN"]]))
    print('-------------------------------')
    print(count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]))
    print('-------------------------------')
    print(count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]]))
    print('-------------------------------')
    print(count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]))
    print('-------------------------------')
    print(count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]))