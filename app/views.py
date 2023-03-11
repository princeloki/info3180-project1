"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, abort,send_from_directory, url_for
from werkzeug.utils import secure_filename
from app.models import PropertiesProfile
from app.forms import PropertiesForm


###
# Routing for your application.
###



def get_uploaded_images():
    uploads_dir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
    filenames = []
    for filename in os.listdir(uploads_dir):
        if os.path.isfile(os.path.join(uploads_dir, filename)) and ('jpg' in filename or 'png' in filename):
            filenames.append(filename)
    return filenames

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET','POST'])
def create():
    form = PropertiesForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validate_on_submit():
                title = form.title.data
                no_bedrooms = form.no_bedrooms.data
                no_bathrooms = form.no_bathrooms.data
                location = form.location.data
                price = form.price.data
                type = form.type.data
                description = form.description.data
                photo = form.photo.data
                
                photo_path = secure_filename(photo.filename)
                joined = os.path.join(app.config['UPLOAD_FOLDER'], photo_path)
                photo.save(joined)
                
                propsmodel = PropertiesProfile(
                    title = title,
                    no_bedrooms = no_bedrooms,
                    no_bathrooms = no_bathrooms,
                    location = location,
                    price = price,
                    type = type,
                    description = description,
                    photo = photo_path
                )
                db.session.add(propsmodel)
                db.session.commit()
                flash('Property saved', 'success')
                return redirect(url_for('properties'))
            flash_errors(form)
    return render_template('create.html', form=form)

@app.route('/properties')
def properties():
    properties = PropertiesProfile.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def get_property(propertyid):
    property = PropertiesProfile.query.filter_by(id=propertyid).first()
    return render_template('view.html', property=property)
    
@app.route('/uploads/<path:filename>')
def get_image(filename):
    uploads_folder = app.config['UPLOAD_FOLDER']
    print(uploads_folder)
    return send_from_directory(uploads_folder, filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
