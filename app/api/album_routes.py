from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..forms import AlbumForm, UpdateAlbumForm
from app.models import db, Album, User, Song
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
    """
    Query for an album by Id
    """
    # album = Album.query.get(id)
    album = db.session.query(Album, User) \
        .join(User, Album.created_by_id == User.id) \
        .filter(Album.id == id).first()

    if album is None:
        return { 'errors': ['Album not found'] }, 404

    return { **album[0].to_dict(), 'created_by': album[1].private_to_dict() }

@album_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_album_by_id(id):
    """
    Delete an album by Id
    """
    album = Album.query.get(id)

    if current_user.id != album.created_by_id:
        return { 'error': 'Unauthorized' }, 401

    if album is None:
        return { 'errors': ['Album not found'] }, 404
    
    remove_file_from_s3(album.art)
    db.session.delete(album)
    db.session.commit()
    return { 'message': 'Successfully deleted' }


@album_routes.route("/new", methods=["POST"])
@login_required
def create_new_album():
    """
    Create a new album
    """
    user = User.query.get(current_user.id)
    form = AlbumForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        image = form.data["art"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        # print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when you tried to upload
        # so you send back that error message (and you printed it above)
            return { 'errors': 'URL not in upload' }

        url = upload["url"]
        new_album = Album(
            name=form.data['name'],
            description=form.data['description'],
            art=url,
            created_by_id=current_user.id
        )
        db.session.add(new_album)
        db.session.commit()
        # new_image = Post(image= url)
        # db.session.add(new_image)
        # db.session.commit()
        return { **new_album.to_dict(), 'created_by': user.private_to_dict() }, 200

    if form.errors:
        print(form.errors)
        return { 'errors': form.errors }

@album_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_album(id):
    """
    Update an existing album
    """
    album = Album.query.get(id)
    user = User.query.get(current_user.id)
    form = UpdateAlbumForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if album is None:
        return { 'error': 'Resource not found'}, 404
    
    if current_user.id != album.created_by_id:
        return { 'error': 'Unauthorized' }, 401

    if form.validate_on_submit():

        if form.data['art']:
            remove_file_from_s3(album.art)

            image = form.data["art"]
            image.filename = get_unique_filename(image.filename)
            upload = upload_file_to_s3(image)
            # print(upload)

            if "url" not in upload:
            # if the dictionary doesn't have a url key
            # it means that there was an error when you tried to upload
            # so you send back that error message (and you printed it above)
                return { 'errors': 'URL not in upload' }, 400

            url = upload["url"]
            album.name = form.data['name']
            album.description = form.data['description']
            album.art = url
            db.session.commit()
            return { **album.to_dict(), 'created_by': user.private_to_dict() }, 200
        else:
            album.name = form.data['name']
            album.description = form.data['description']
            db.session.commit()
            return { **album.to_dict(), 'created_by': user.private_to_dict() }, 200

    if form.errors:
        print(form.errors)
        return { 'errors': form.errors }, 401