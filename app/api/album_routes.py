from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Album

album_routes = Blueprint('album', __name__)

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