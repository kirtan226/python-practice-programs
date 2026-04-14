'''
Write a function to filter a list of dictionaries based on star rating.

input:[{'name": 'Hotel1', 'stars': 3}, {'name': 'Hotel2', 'stars': 4}, {'name': 'Hotel3', 'stars': 5}] , 4
output:[{'name': 'Hotel2', 'stars': 4}, {'name': 'Hotel3', 'stars': 5}]
Reason: The function filters out hotels with less than 4 stars. The remaining
hotels are Hote12 and Hotel3

Input:[{'name': 'HotelA', 'stars': 2}, {'name': 'HotelB', 'stars': 3}, {'name': 'HotelC', 'stars': 5}] ,3
output:[{'name': 'HotelB', 'stars': 3}, {'name': 'HotelC', 'stars': 5}]

'''

def filter_by_star_rating(hotels, min_stars):
    new=[]
    for i in hotels:
        print("i" , i)
        if i['stars']>=min_stars:
            new.append(i)

    return new

filter_by_star_rating([{"name":"Hotel1" ,"stars": 3 }, {"name": "Hotel2", "stars": 4}, {"name": "Hotel3", "stars": 5}] , 4)