from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/second', methods=['POST'])
def second():
    house_price = int(request.form.get('home_price'))
    loan_term = int(request.form.get('loan_term'))
    down_payment = int(request.form.get('down_payment'))

    months = loan_term * 12

    principal = house_price - down_payment
    mort_yearly = principal / loan_term
    monthly_pay = mort_yearly / 12
    total_paid = monthly_pay * months



    return render_template('second.html',
    monthly_pay=str(round(monthly_pay, 2)),
    mort_yearly=str(round(mort_yearly, 2)),
    house_price=str(house_price),
    loan_amount= str(principal),
    down_payment= str(down_payment),
    months=str(months), total_paid=str(total_paid)

    )
