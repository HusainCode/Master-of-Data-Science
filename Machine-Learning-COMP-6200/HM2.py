import pandas
import numpy

file_path = "earthquakes.csv"
DATA_FRAME = pandas.read_csv(file_path)


# # This function to computer the  distance using the provided formula
def determine_distance(latitude1, longitude1, latitude2, longitude2):
    latitude1, longitude1, latitude2, longitude2 = map(numpy.radians, [latitude1, longitude1, latitude2, longitude2])
    return numpy.arccos(
        numpy.sin(latitude1) * numpy.sin(latitude2) +
        numpy.cos(latitude1) * numpy.cos(latitude2) * numpy.cos(longitude2 - longitude1)
    ) * 6371

# Order the data by decreasing value
top_10_earthquakes = DATA_FRAME.nlargest(10, 'impact.magnitude')

# Saving the top 10 worst earthquakes
top_10_earthquakes.to_csv("top 10 worst earthquakes.txt", index=False, sep='\t')

# Tennessee State University (TSU) location
TSU_LATIUDE = 36.16963449238665
TSU_LONGITUDE= -86.82562299320742

# DO the math to determine the distance
top_10_earthquakes['distance_to_TSU'] = top_10_earthquakes.apply(lambda row: determine_distance(row['location.latitude'], row['location.latitude'], TSU_LATIUDE, TSU_LONGITUDE), axis=1)

# Save the distances to a text file
top_10_earthquakes[['location.latitude', 'location.longitude', 'distance_to_TSU']].to_csv("Distance to TSU.txt", index=False, sep='\t')

print("The process is successfully completed1")
