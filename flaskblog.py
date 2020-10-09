from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'John',
		'title': 'Blog Post 1',
		'content': 'This is the content for the first blog',
		'data_posted': 'Oct 08, 2020'

	},
	{	'author': 'Tom',
		'title': 'Blog Post 2',
		'content': 'This is the content for the second blog',
		'date_posted': 'Oct 09, 2020'

	}
	

]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__== '__main__':
	app.run(debug=True)