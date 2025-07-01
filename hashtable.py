# #reading data from file converting into hash and storing in simple array
# weather_dict = {}

# with open("nyc_weather.csv","r") as f:
#     for line in f:
#         data = line.strip().split(',')
#         try:
#             date = data[0]
#             temperature = int(data[1])
#             weather_dict[date] = temperature
#             #weather_dict.append(temperature)
#         except:
#             print("Invalid temperature Ignore the row")

# print(weather_dict)

# # What was the average temperature in first week of Jan

# first_week_temps = list(weather_dict.values())[:7]
# average_temperature = sum(first_week_temps) / len(first_week_temps)
# print("Average Temperature: ", round(average_temperature, 1), "'F", sep="")

# # # What was the maximum temperature in first 10 days of Jan
# print("Maximum Temperature: ",max(weather_dict.values()), "'F", sep="")

# #What was the temperature on Jan 9?
# x = input("Enter date to search temp e.g (Jan 1): ")
# x_capitalize = x.capitalize()
# print(f"Temprature on {x} is: ",weather_dict.get(x_capitalize,'Data not avaliable'), "'F", sep="")

# # What was the temperature on Jan 4?
# y = input("Enter date to search temp e.g (Jan 1): ")
# y_capitalize = y.capitalize()
# print(f"Temprature on {y} is: ",weather_dict.get(y_capitalize,'Data not Avaliable'), "'F", sep="")

#---------------------------------------------------------

# Create an empty dictionary to store word counts

words_count = {}

with open("poem.txt", "r") as poem_file:
    for line in poem_file:
        words = line.strip().split()
        
        # Loop through each word in the line
        for word in words:
            word = word.strip('.,;:!?"\'').lower()
            
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

# for word, count in words_count.items():
#     print(f"{word} : {count}")

# Print only the first 10 words and their counts
# for word, count in list(words_count.items())[:10]:
#     print(f"{word} : {count}")
print("WORDS\t  COUNT")
for word, count in list(words_count.items())[:10]:
    print(f"{word.ljust(12)}{count}")

