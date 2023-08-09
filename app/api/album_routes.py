from flask import Blueprint, jsonify, request
from flask_login import login_required
from ..forms import AlbumForm
from app.models import db, Album, User
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

album_routes = Blueprint('albums', __name__)

@album_routes.route('/')
def get_all_albums():
    """
    Query for all albums
    """
    albums = Album.query.all()

    return { "albums": [album.to_dict() for album in albums] }

@album_routes.route('/<int:id>')
def get_album_info(id):
    album = Album.query.get(id)

    if album is None:
        return { 'errors': ['Album not found'] }, 404
    
    return {'album': album.to_dict()}

@album_routes.route('/<int:id>', methods=['DELETE'])
def delete_album_by_id(id):
    album = Album.query.get(id)

    if album is None:
        return { 'errors': ['Album not found'] }, 404
    
    db.session.delete(album)
    db.session.commit()
    return { 'message': 'Successfully deleted' }


@album_routes.route("/new", methods=["POST"])
@login_required
def upload_image():
    form = AlbumForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        image = form.data["art"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when you tried to upload
        # so you send back that error message (and you printed it above)
            return { 'errors': 'URL not in upload' }

        url = upload["url"]
        # new_image = Post(image= url)
        # db.session.add(new_image)
        # db.session.commit()
        return { 'message': 'Success' }

    if form.errors:
        print(form.errors)
        return { 'errors': form.errors }

    # return render_template("post_form.html", form=form, errors=None)