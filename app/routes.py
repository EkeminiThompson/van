from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ContactForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/work')
def work():
    return render_template('work.html', title='Our Work')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent successfully!')
        return redirect(url_for('home'))
    return render_template('contact.html', title='Contact Us', form=form)
