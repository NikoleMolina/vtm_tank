from flask import Flask, redirect, request, url_for
from flask import render_template

app = Flask(__name__)


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
        radius = form['radius']
        height = form['height']
        area_top = 3.14 * radius**2
        area_side = 2*3.14*radius*height
        total_area = area_top + area_side
        square_feet = total_area/144
        material_cost = square_feet * 25
        labor_cost = square_feet * 15
        total_cost = material_cost + labor_cost
        total_costestimate = round(total_cost, 2)
        total_costestimate = str(total_costestimate)
        return render_template('estimate.html', pageTitle = 'Create An Estimate', Price = total_costestimate)
    return render_template('estimate.html', pageTitle = 'Create An Estimate')
 
if __name__ == '__main__':
    app.run(debug=True)