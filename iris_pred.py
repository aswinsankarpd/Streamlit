import streamlit as st 
import pandas as pd 
from sklearn import datasets 
from sklearn.ensemble import RandomForestClassifier

st.write("Flower Prediction App")

st.sidebar.header("User Input features")

def user_input_features():
    sepal_length = st.sidebar.slider('sepal length',4.3,7.9,5.4)
    sepal_width = st.sidebar.slider('sepal_width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('petal_length',1.0,6.9,1.3)
    petal_width = st.sidebar.slider('petal_width',0.1,2.5,0.2)

    data = {'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width':petal_width
    }

    features = pd.DataFrame(data,index=[0])

    return features 

df = user_input_features()

st.subheader("User Inputs")
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader("class label and corresponding index number")
st.write(iris.target_names)


st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_proba)