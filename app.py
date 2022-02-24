#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


print(__name__)


# In[4]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income,age,loan)
        model = joblib.load("CCdefault")
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        if pred == 1:
            pred = "Will default"
        else:
            pred = "Will not default"
        s = "The default result is : " + str(pred)
        return(render_template("index2.html", result = s))
    else:
        return(render_template("index2.html", result = "Default result"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




