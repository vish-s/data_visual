import matplotlib.pyplot as plt
import pandas as pd

#Data Source
data_source = "http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv"

# Read data into Pandas Dataframe
gender_degree_data = pd.read_csv(data_source)

# Tableau 20 RGB
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]


# Each of the 20 colors
for each in range(len(tableau20)):
	r, g, b = tableau20[each]
	tableau20[i] = (r / 255., g / 255., b / 255.)

# Resolution
plt.figure(figsize=(12, 14))

# Remove plot frame lines
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Avoid unnecessary whitespaces
plt.ylim(0,90)
plt.xlim(1968, 2014)

# Set font size
plt.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)
plt.xticks(fontsize=14)


for each in range(10,91,10):
	plt.plot(range(1968, 2012), [each] * len(range(1968, 2012)), "--", lw = 0.5, color="black", alpha=0.3)


plt.tick_params(axis="both", which="both", bottom="off", top="off",labelbottom="on", left="off", right="off", labelleft="on")  


# Set column titles

majors = ['Health Professions', 'Public Administration', 'Education', 'Psychology',    
          'Foreign Languages', 'English', 'Communications\nand Journalism',    
          'Art and Performance', 'Biology', 'Agriculture',    
          'Social Sciences and History', 'Business', 'Math and Statistics',    
          'Architecture', 'Physical Sciences', 'Computer Science',    
          'Engineering']  

for rank, column in enumerate(majors):
	# Plot each line using a new color from T20
	plt.plot(gender_degree_data.Yea.values, gender_degree_data[column.replace("\n", "")].values, lw=2.5, color = tableau20[rank]) 

	# Label each graph
	y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5 
	if column == "Foreign Languages":
		y_pos +=0.5
	elif column == "English":    
        	y_pos -= 0.5    
    	elif column == "Communications\nand Journalism":    
        	y_pos += 0.75    
    	elif column == "Art and Performance":    
        	y_pos -= 0.25    
    	elif column == "Agriculture":    
        	y_pos += 1.25    
    	elif column == "Social Sciences and History":    
        	y_pos += 0.25    
    	elif column == "Business":    
        	y_pos -= 0.75    
    	elif column == "Math and Statistics":    
        	y_pos += 0.75    
    	elif column == "Architecture":    
        	y_pos -= 0.75    
    	elif column == "Computer Science":    
        	y_pos += 0.75    
    	elif column == "Engineering":    
        	y_pos -= 0.25

	# Set font size
	plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])
	
plt.text(1995, 93, "Percentage of Bachelors degrees conferred to worn in the USA", fontsize=17, ha="center")
plt.savefig("percent-bachelors-degrees-women-usa.png", bbox_inches="tight") 
