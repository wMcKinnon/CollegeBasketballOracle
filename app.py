from cbbo_form import CbboForm
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# YOU NEED A SECRET_KEY
# A secret key that will be used for securely signing the 
# session cookie and can be used for any other security 
# related needs by extensions or your application. It 
# should be a long random string of bytes, although 
# unicode is accepted too.
# kenpom adjusted efficiency margin
# ncaa net ranking
# barttorvik barthag 
app.config["SECRET_KEY"]='why_a_duck?'

@app.route("/")
def my_redirect():
   return redirect(url_for('college_basketball_oracle_form'))

@app.route('/college_basketball_oracle_form', methods=['GET', 'POST'])
def college_basketball_oracle_form():
   form = CbboForm()
   if form.is_submitted():
      result = request.form
      return render_template('cbbo_prediction_handler.html', 
                             title="College Basketball Oracle Prediction", 
                             header="College Basketball Oracle Prediction", 
                             result=result)
   return render_template('cbbo_form_select.html', 
                          title="College Basketball Oracle", 
                          header="College Basketball Oracle", 
                          form=form)

# debugging depending on how app is invoked in VS Code
if __name__ == "__main__":
   app.run()