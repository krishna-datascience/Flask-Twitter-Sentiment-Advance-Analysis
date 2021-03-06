#IMPORTING REQUIREMENTS
from flask import Flask
from flask import render_template
import pandas as pd
from flask import request
import os

#ASSINGNING APP AS__NAME_ FOR CALLING TO MAIN
app = Flask(__name__)

#DEFAULT ROUTING
@app.route('/')

#ROUTING TO HOME
@app.route('/home')
def home():
    print('Home Page')
    return render_template('home.html')

#ROUTING TO HASHTAGS SENTIMENTS
@app.route("/HashtagSentiment")
def HashtagSentiment():

    print('Hashtags Sentiments Page')

    #CALLING CSV FILE IN A DATAFRAME
    # dataframe = pd.read_csv(r"C:\Users\Manomay\Desktop\App\Source\sample.csv")    #BY DEFAULT IT DEOSEN'T NEED LOCATION BUT DUE TO ERRORS I HAD TO ASSIGN LOCATION

    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

    #PARAMETERS
    datalist = []
    datalist_1 = []


    #SENDING COLOUMNS IN THE PARAMENTERS (TRIAL PURPOSE)
    # datalist = dataframe.columns
    # for col in dataframe.columns:
    #     print(col)
    #     datalist.append(col)
    #     print(datalist)


    #GETTING HASHTAGS ROWS
    for rows in dataframe.get_values():
        datalist_1.append(rows[2])
        #print(rows[0])
        datalist.append(rows[0])
    #print (datalist)

    print('Hashtags Sentiments Dataframe Generated')

    #ASSIGN VALUES TO GRAPH VARIABLES
    Cities = datalist
    Sentiment = datalist_1
    legend = 'Tweets'

    print('Hashtags Sentiments Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('HashtagSentiment.html', values=Sentiment, labels=Cities, legend=legend)



#ROUTING TO CITY SENTIMENTS
@app.route("/CitySentiments")
def CitySentiments():

    print('City Sentiments Page')

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = dataframe[['Cities', 'Sentiment_Rating']]

    #GROUPING BY CITIES WITH MEAN OF INDEXES
    data_gpd = data.groupby(['Cities']).mean().reset_index()            #USING ".reset_index()" TO RESET THE INDEXING LOST WHEN GROUPING THE VALUES

    print('City Sentiments Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []

    #FORLOOP APPENDING ROWS
    for rows in data_gpd.get_values():
        datalist.append(float(rows[1]))                                 #COMBINED TWO FOR LOOPS
        datalist_1.append(str(rows[0]).replace(" ", ""))

    #ASSIGINING PARAMETERS TO RETURN CALLS
    legend = 'Top Tweeting Cities'
    Cities = datalist_1
    Sentiment = datalist

    print('City Sentiments Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('CitySentiments.html', values=Sentiment, labels=Cities, legend=legend)


@app.route("/TopTweetingCities")
def TopTweetingCities():

    print('Top Tweeting Cities Page')

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = dataframe[['Cities','Hashtags']]

    #GROUPING BY CITIES
    data_gd = data.groupby(['Cities']).count().reset_index()

    #extracting greatest 500
    data_order = data_gd.nlargest(500, "Hashtags")

    print('Top Tweeting Cities Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in data_order.get_values():
        datalist.append(int(rows[1]))

    #ITTERATING ROWS FOR CITY NAMES
    for rows in data_order.get_values():
        datalist_1.append(str(rows[0]).replace(" ", ""))

    #PASSING PARAMENTERS
    legend = 'Tweets'
    Sentiments = datalist
    Cities = datalist_1

    print('Top Tweeting Cities Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('TopTweetingCities.html', values=Sentiments, labels=Cities, legend=legend)


@app.route("/OverallSentiments")
def OverallSentiments():

    print('Overall Sentiments Page')

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = dataframe[['Sentiment','Cities']]

    #GROUPING BY CITIES
    data_gd = data.groupby(['Sentiment']).count().reset_index()

    print('Overall Sentiments Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in data_gd.get_values():
        datalist.append(int(rows[1]))

    #ITTERATING ROWS FOR CITY NAMES
    for rows in data_gd.get_values():
        datalist_1.append(str(rows[0]).replace(" ", "_"))

    #PASSING PARAMENTERS
    legend = 'Tweets'
    Sentiment = datalist
    Cities = datalist_1

    print('Overall Sentiments Datafame Passed ')

    #RETURNING THE CHART.JS VALUES
    return render_template('OverallSentiments.html', values=Sentiment, labels=Cities, legend=legend)


@app.route("/TopHashtags")
def TopHashtags():

    print('Top Hashtags Page')

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = dataframe[['Hashtags','Cities']]

    #GROUPING BY CITIES
    data_gd = data.groupby(['Hashtags']).count().reset_index()

    #extracting greatest 500
    large500 = data_gd.nlargest(500, "Cities")

    print('Top Hashtags Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in large500.get_values():
        datalist.append(int(rows[1]))

    #ITTERATING ROWS FOR CITY NAMES
    for rows in large500.get_values():
        datalist_1.append(str(rows[0]).replace(" ", "_"))

    #PASSING PARAMENTERS
    legend = 'Tweet Count'
    CityCount = datalist
    Hashtags = datalist_1

    print('Top Hashtags Datafame Passed ')

    #RETURNING THE CHART.JS VALUES
    return render_template('TopHashtags.html', values=CityCount, labels=Hashtags, legend=legend)



@app.route("/MostSpokenWord")
def MostSpokenWord():

    print('Most Spoken words')

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\MostSpokenWord.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Word', 'Count']

    #extracting greatest 30
    large30 = dataframe.nlargest(30, "Count")

    print('Most Spoken Word Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in large30.get_values():
        datalist.append(int(rows[1]))

    #ITTERATING ROWS FOR CITY NAMES
    for rows in large30.get_values():
        datalist_1.append(str(rows[0]).replace(" ", " "))

    #PASSING PARAMENTERS
    legend = 'Count'
    Count = datalist
    Words = datalist_1

    print('Most Spoken Word Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('MostSpokenWord.html', values=Count, labels=Words, legend=legend)


@app.route("/CitywiseHashtagsSentiments", methods=['GET', 'POST'])
def CitywiseHashtagsSentiments():

    print('Citywise Hashtags Sentiments Page')

    #GETTING VALUES FROM THE DROP DOWN USING REQUEST
    select = request.form.get('comp_select')

    print(select)

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

#------------------------------------------------DROP DOWN DATA CALLS START-----------------------------------------------------------------------

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data_Dropdown = dataframe[['Cities', 'Hashtags']]

    data_Dropdown_1 = data_Dropdown.groupby(['Cities']).count().reset_index()

#------------------------------------------------DROP DOWN DATA CALLS END-------------------------------------------------------------------------

    #FILTER DATA BY WORD IN DATAFRAMES
    FTR_data = dataframe[(dataframe.Cities == select)]

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = FTR_data[['Cities', 'Hashtags', 'Sentiment_Rating']]

    #GROUPING BY CITIES
    data_gd = data.groupby(['Hashtags']).sum().reset_index()

    print(data_gd)

    print('Citywise Hashtags Sentiments Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []
    datalist_2 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in data_gd.get_values():
        datalist.append(int(rows[1]))

    #ITTERATING ROWS FOR CITY NAMES
    for rows in data_gd.get_values():
        datalist_1.append(str(rows[0]).replace(" ", " "))

    #ITTERATING ROWS FOR CITY NAMES FOR DROPDOWN
    for rows in data_Dropdown_1.get_values():
        datalist_2.append(str(rows[0]).replace(" ", " "))

    #PASSING PARAMENTERS
    legend = 'Hashtag'
    Sentiment = datalist
    Cities = datalist_1
    dropdown_val = datalist_2

    print('Citywise Hashtags Sentiments Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('CitywiseHashtagsSentiments.html', values=Sentiment, labels=Cities, legend=legend, dropdown_val=dropdown_val, selected_value=select)


@app.route("/CitywiseTopHashtags", methods=['GET', 'POST'])
def CitywiseTopHashtags():

    print('Citywise Top Hashtags Page')

    #GETTING VALUES FROM THE DROP DOWN USING REQUEST
    select = request.form.get('comp_select')

    print(select)

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\sample.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Hashtags', 'Cities', 'Sentiment_Rating', 'Sentiment']

#------------------------------------------------DROP DOWN DATA CALLS START------------------------------------------------------------------------------

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data_Dropdown = dataframe[['Cities', 'Hashtags']]

    data_Dropdown_1 = data_Dropdown.groupby(['Cities']).count().reset_index()

#------------------------------------------------DROP DOWN DATA CALLS END---------------------------------------------------------------------------------

    #FILTER DATA BY WORD IN DATAFRAMES
    FTR_data = dataframe[(dataframe.Cities == select)]

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = FTR_data[['Hashtags','Cities']]

    #GROUPING BY CITIES
    data_gd = data.groupby(['Hashtags']).count().reset_index()

    data_gd2 = data_gd.groupby(['Hashtags']).sum().reset_index()

    print(data_gd2)

    print('Citywise Top Hashtags Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []
    datalist_2 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in data_gd2.get_values():
        datalist.append(int(rows[1]))

    print(datalist)

    #ITTERATING ROWS FOR CITY NAMES
    for rows in data_gd2.get_values():
        datalist_1.append(str(rows[0]).replace(" ", " "))

    #ITTERATING ROWS FOR CITY NAMES FOR DROPDOWN
    for rows in data_Dropdown_1.get_values():
        datalist_2.append(str(rows[0]).replace(" ", " "))

    #PASSING PARAMENTERS
    legend = 'Tweets'
    Sentiment = datalist
    Cities = datalist_1
    dropdown_val = datalist_2

    print('Citywise Top Hashtags Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('CitywiseTopHashtags.html', values=Sentiment, labels=Cities, legend=legend, dropdown_val=dropdown_val, selected_value=select)


@app.route("/CitywiseMostSpokenWord", methods=['GET', 'POST'])
def CitywiseMostSpokenWord():

    print('Citywise Most Spoken Word Page')

    #GETTING VALUES FROM THE DROP DOWN USING REQUEST
    select = request.form.get('comp_select')

    print(select)

    #CALLING CSV FILE IN A DATAFRAME
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "Source\MostUsedWord.csv"))

    #MAKING COLOUMNS FOR A IMPORTED CSV FILE
    dataframe.columns = ['Cities', 'Words']

#------------------------------------------------DROP DOWN DATA CALLS START------------------------------------------------------------------------------

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data_Dropdown = dataframe[['Cities', 'Words']]

    data_Dropdown_1 = data_Dropdown.groupby(['Cities']).count().reset_index()

#------------------------------------------------DROP DOWN DATA CALLS END---------------------------------------------------------------------------------

    #FILTER DATA BY WORD IN DATAFRAMES
    FTR_data = dataframe[(dataframe.Cities == select)]

    #EXTRACTING COLOUMNS DATA FROM DATAFRAME
    data = FTR_data[['Cities','Words']]

    #GROUPING BY CITIES
    data_gd = data.groupby(['Words']).count().reset_index()

    data_gd2 = data_gd.groupby(['Words']).sum().reset_index()

    #extracting greatest 30
    large30 = data_gd2.nlargest(30, "Cities")

    print(large30)

    print('Citywise Most Spoken Word Datafame Generated')

    #PARAMETERS
    datalist = []
    datalist_1 = []
    datalist_2 = []

    #ITTERTATING ROWS CITY COUNT
    for rows in large30.get_values():
        datalist.append(int(rows[1]))

    print(datalist)

    #ITTERATING ROWS FOR CITY NAMES
    for rows in large30.get_values():
        datalist_1.append(str(rows[0]).replace(" ", " "))

    #ITTERATING ROWS FOR CITY NAMES FOR DROPDOWN
    for rows in data_Dropdown_1.get_values():
        datalist_2.append(str(rows[0]).replace(" ", " "))

    #PASSING PARAMENTERS
    legend = 'Word Count'
    Sentiment = datalist
    Cities = datalist_1
    dropdown_val = datalist_2

    print('Citywise Most Spoken Word Datafame Values Passed')

    #RETURNING THE CHART.JS VALUES
    return render_template('CitywiseMostSpokenWord.html', values=Sentiment, labels=Cities, legend=legend, dropdown_val=dropdown_val, selected_value=select)


#MAIN CALL FUNCTION CALLING FLASK =_NAME_
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
