from flask import Flask, render_template
import pandas as pd
import glob,pathlib

# create website object
app = Flask("website")

# extract station data from .txt file
station_data = pd.read_csv("data/stations.txt",skiprows=17)
station_data = station_data[["STAID","STANAME                                 "]]

@app.route("/")
def go_home():
    return render_template("home.html",data = station_data.to_html())

@app.route("/api/v1/<station>/<date>/")
def weather(station,date):

    # # My approach
    # # get all the files from data
    # all_files = glob.glob("data/TG*.txt")
    # for file in all_files:
    #     station_id = int(pathlib.Path(file).stem[8:])
    #     if station_id ==station:
    #         df = pd.read_csv(file,skiprows=20)
    #         finite_df = df.loc(df['   TG']!=-9999)
    #         temperature = finite_df.loc(finite_df["    DATE"]==date)['   TG']/10
    #         break

    # return {"station":station,
    #         "date":date,
    #         "temperature":temperature}

    # Faster approach
    filename = "data/TG_STAID"+str(station).zfill(6)+".txt"
    print(filename)
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    # finite_df = df.loc(df['   TG']!=-9999)
    temperature = df.loc[df["    DATE"]==date]['   TG'].squeeze()/10
    print(temperature)
    return {"station":station,
            "date":date,
            "temperature":temperature}


if __name__=="__main__":
    app.run(debug=True)
