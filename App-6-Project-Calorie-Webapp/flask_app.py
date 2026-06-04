import temperature
from temperature import Temperature
from calorie import Calorie
from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform= calories_form)

    def post(self):
        caloriesform = CaloriesForm(request.form)

        temp = Temperature(city=caloriesform.city.data, country=caloriesform.country.data).get()

        calorie = Calorie(weight=float(caloriesform.weight.data),
                           height=float(caloriesform.height.data),
                           age=float(caloriesform.age.data),
                           temperature=float(temp))

        return render_template('calories_form_page.html', caloriesform = caloriesform, calories = calorie.calculate(), temperature=temp, result=True)



class CaloriesForm(Form):

    weight = StringField("Enter Weight: ", default=75)
    height = StringField("Enter Height (in cm): ", default=170)
    age = StringField("Enter Age: ", default=18)
    city = StringField("Enter City: ", default='Pune')
    country = StringField("Enter Country: ", default='India')
    button = SubmitField("Calculate calories")


app.add_url_rule("/", view_func=HomePage.as_view('home_page'))
app.add_url_rule("/calories", view_func=CaloriesFormPage.as_view('calories_form_page'))
app.run(debug=True)

