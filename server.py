from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('./web_server/database.txt', mode='a') as database:
		email = data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('./web_server/database2.csv', newline='',mode='a') as database2:
		email = data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(database2, delimiter=",",quotechar="'") # Check documentation for the parameters meanings
		csv_writer.writerow([email,subject,message])

@app.route("/submit_form", methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/thankyou.html')
    else:
    	return "Something went wromg. Try Again"
# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')