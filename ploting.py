import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

only_files = [f for f in listdir("seprate_sheets/") if isfile(join("seprate_sheets/", f))]
print(only_files)

for files in only_files:
    df2 = pd.read_csv("seprate_sheets/"+files)
    df2 = df2.sort_values(by=['Post_Time'])
    i=0
    j=30


    asd = round(len(df2)/30)
    counter = 0
    while counter <= asd:
        df1 = df2[i:j]

        x = df1['Post_Time']
        y = df1['Numbered_Sentiment']
        print(x)

        plt.figure()
        plt.plot(x, y)
        plt.bar(x, y, alpha=0.2)
        plt.title(f"Time VS Posts Sentiments")
        plt.xlabel("Date")
        plt.ylabel("Sentiment Value")
        plt.xticks(x, [str(i) for i in x], rotation=90)

        #set parameters for tick labels
        plt.tick_params(axis='x', which='major', labelsize=10)

        plt.tight_layout()
        plt.savefig("Scatter_plot-"+files+"_"+str(counter)+".png")

        counter +=1
        i += 30
        j += 30