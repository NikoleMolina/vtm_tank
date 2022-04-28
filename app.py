from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

price_estimate = [{"price" = ""}]
@app.route('/')
def index():
    return render_template('index.html', pageTitle = 'Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate', methods=['GET', 'POST'])
def estimator():
    if request.method == 'POST':
        form = request.form
        radius = int(form['radius'])
        height = int(form['height'])
        pi = 3.14
        area_top = pi * (radius*radius)
        area_side = 2*(pi*(radius * height))
        total_area = area_top + area_side
        square_feet = total_area/144
        material_cost = square_feet * 25
        labor_cost = square_feet * 15
        total_cost = material_cost + labor_cost
        total_costestimate = "$" + str(round(total_cost, 2))
        Price = total_costestimate
        return render_template('estimate.html', pageTitle = 'Create An Estimate', Price = Price)
    return render_template('estimate.html', pageTitle = 'Create An Estimate')
 
if __name__ == '__main__':
    app.run(debug=True)