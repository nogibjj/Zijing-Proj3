import streamlit as st
import pandas as pd
from dblib.querydb import find_job_avg_salary
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


@st.cache(persist=True)
def load_data():
    result = find_job_avg_salary()
    return pd.DataFrame(result, columns=["avg_salary", "job_title"])


st.title("Job Salary")
st.write("This app shows the average salary of a job title")
df = load_data()
# df.astype({"avg_salary": int})
st.write(df)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.write("word cloud for job title per salary")

index = df.index
number_of_rows = len(index)
words = ""
for i in index:
    words += ((df["job_title"][i]+";")*(number_of_rows-i))
wc = WordCloud(
    stopwords=STOPWORDS, background_color="white", height=640, width=800
).generate(words)
plt.imshow(wc)
plt.xticks([])
plt.yticks([])
st.pyplot()
