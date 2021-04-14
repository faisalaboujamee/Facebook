import time
import os
from facebook_scraper import get_posts
from textblob import TextBlob
import json
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

#Plots number of sentiment Vs post time (This has not been used for data visualization)

def plot_stacked():
    df1 = pd.read_csv("post_data.csv")
    df1 = df1.sort_values(by=['Post_Time'])
    df1['Post_Time'] = pd.to_datetime(df1['Post_Time']).dt.to_period('M')

    plt.figure()
    plt.xlabel('Months of the year')

    plt.xticks()
    plt.ylabel('Post Sentiments')
    df2 = df1.groupby(['Post_Time', 'Post_Sentiment']).size().unstack()
    df2.plot(kind='bar', stacked=True)
    plt.savefig("Stacked_Group_Plot.png", bbox_inches='tight')



def makeSeprateSheets():
    df1 = pd.read_csv("post_data.csv")
    asd = open("post_data.csv", "r", encoding="utf-8").readlines()
    sheets = df1["Post_From"]
    sheets = sheets.drop_duplicates()
    if os.path.exists("seprate_sheets"):
        pass
    else:
        os.mkdir("seprate_sheets")
    for name in sheets:
        open_file = open("seprate_sheets/" + name + ".csv", "w", encoding="utf-8")
        open_file.write("Post_ID,Post_Time,Post_Text,Post_Sentiment,Numbered_Sentiment,Post_From\n")
        for line in asd:
            if line.__contains__(name):
                open_file.write(
                    line.replace("Very Negative", "Very Negative,0").replace("Negative",
                                                                             "Negative,1").replace("Neutral",
                                                                                             "Neutral,2").replace(
                        "Positive", "Positive,3").replace("Very Positive", "Very Positive,4"))


def plot_Pie():
    print("Plotting the Pie Chart")
    asd = Counter(df['Post_Sentiment'])
    plt.pie([float(v) for v in asd.values()], labels=[k for k in asd],
            autopct='%1.2f%%')
    plt.savefig("pie_chart.png")


def senti_checker(text):
    asd = TextBlob(text).sentiment.polarity
    if asd < -0.1:
        return "Very Negative"
    elif -0.1 < asd < 0:
        return "Negative"
    elif 0 < asd < 0.1:
        return "Positive"
    elif asd > 0.1:
        return "Very Positive"
    else:
        return "Neutral"


def Scrape_group():
    print("Getting Posts from Groups...")
    for group in data["groups"]:
        for post in get_posts(group=group, pages=int(data["number_of_pages"])):
            post_text = str(post["text"]).replace("\n", "").replace(",", "")
            post_id = str(post["post_id"])
            post_date = str(post["time"])
            if str(post["text"]).__contains__("covid"):
                senti = senti_checker(post_text)
                write_csv.write(post_id + "," + post_date + "," + post_text + "," + senti + "," + group + "\n")


def Scrape_pages():
    print("Getting Posts from Pages...")
    for page in data["pages"]:
        for post in get_posts(page, pages=int(data["number_of_pages"])):
            post_text = str(post["text"]).replace("\n", "").replace(",", "")
            post_id = str(post["post_id"])
            post_date = str(post["time"])
            if any(lixt_of_words in post_text for lixt_of_words in list_of_words):
                senti = senti_checker(post_text)
                write_csv.write(post_id + "," + post_date + "," + post_text + "," + senti + "," + page + "\n")


if __name__ == '__main__':
    while True:
        with open("config2.json") as json_data_file:
            data = json.load(json_data_file)
            print("Checking Configurations...")

        print("Getting Details From Config File...")

        list_of_words = []
        for words in data["Keywords"]:
            list_of_words.append(words)

        print(list_of_words)

        if os.path.exists("post_data.csv"):
            i = False
        else:
            i = True
        write_csv = open("post_data.csv", "a", encoding="utf-8")
        if i:
            write_csv.write("Post_ID,Post_Time,Post_Text,Post_Sentiment,Post_From\n")
        # Scrape_group()
        Scrape_pages()
        write_csv.close()
        df = pd.read_csv("post_data.csv")
        df = df.drop_duplicates()
        df.to_csv("post_data.csv", index=False)
        plot_Pie()
        makeSeprateSheets()
        print("Going to Sleep...")
        plot_stacked()
        time.sleep(int(data["time_to_sleep"]))
