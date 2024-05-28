from flask import (
    Flask,
    request,
    abort,
    jsonify,
    render_template,
)
from auth import AuthError, requires_auth
from models import Actors, Movies, setup_db
from flask_cors import CORS
from models import db
from urllib.parse import urlencode
from flask import (
    url_for,
)


from setup import (
    API_AUDIENCE,
    AUTH0_CLIENT_ID,
    AUTH0_DOMAIN,
)


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, supports_credentials=True)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Headers", "GET, POST, PATCH, DELETE, OPTIONS"
        )

        return response

    # home route
    @app.route("/", methods=["GET", "POST"])
    def home():
        login_link = build_login_link()
        return render_template("home.html", login_link=login_link)

    @app.route("/callback", methods=["GET", "POST"])
    def callback():
        return render_template("home.html")

    # Get /movies
    @app.route("/movies", methods=["GET"])
    @requires_auth("get:movies")
    def get_movies(auth_data):
        try:
            movies = Movies.query.all()

            return (
                jsonify(
                    {"success": True, "movies": [movie.format() for movie in movies]}
                ),
                200,
            )
        except Exception:
            abort(500)

    # Create /movies
    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movies")
    def create_movie(auth_data):
        data = request.get_json()

        movie = Movies(title=data["title"], release_date=data["release_date"])

        if movie.title == "" or movie.release_date == "":
            abort(422)

        try:
            movie.insert()

            return jsonify({"success": True, "movie": movie.format()}), 200
        except Exception:
            db.session.rollback()
            abort(500)

    # Update /movies
    @app.route("/movies/<int:id>", methods=["GET", "PATCH"])
    @requires_auth("path:movies")
    def update_movie(auth_data, id):
        data = request.get_json()
        movie = Movies.query.filter(Movies.id == id).one_or_none()

        if movie:
            if data["title"]:
                movie.title = data["title"]

            if data["release_date"]:
                movie.release_date = data["release_date"]
        else:
            abort(404)

        try:
            movie.update()
            return jsonify({"success": True, "movie": [movie.format()]}), 200
        except Exception:
            db.session.rollback()
            abort(500)

    # Delete /movies
    @app.route("/movies/<int:id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(auth_data, id):
        movie = Movies.query.filter(Movies.id == id).one_or_none()

        if movie:
            try:
                movie.delete()
                return jsonify({"success": True, "delete": id}), 200
            except Exception:
                db.session.rollback()
                abort(500)
        else:
            abort(404)

    # Get /actors
    @app.route("/actors", methods=["GET"])
    @requires_auth("get:actors")
    def get_actors(auth_data):
        try:
            actors = Actors.query.all()
            return (
                jsonify(
                    {"success": True, "actors": [actor.format() for actor in actors]}
                ),
                200,
            )
        except Exception:
            abort(500)

    # Create /actors
    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actors")
    def create_actor(auth_data):
        data = request.get_json()

        actor = Actors(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            movie_id=data["movie_id"],
        )

        if actor.name == "" or actor.age == "" or actor.gender == "":
            abort(422)

        try:
            actor.insert()
            return jsonify({"success": True, "actor": actor.format()}), 200
        except Exception:
            db.session.rollback()
            abort(500)

    # Update /actors
    @app.route("/actors/<int:id>", methods=["GET", "PATCH"])
    @requires_auth("path:actors")
    def update_actor(auth_data, id):
        data = request.get_json()
        actor = Actors.query.filter(Actors.id == id).one_or_none()

        if actor:
            if data["name"]:
                actor.name = data["name"]

            if data["age"]:
                actor.age = data["age"]

            if data["gender"]:
                actor.gender = data["gender"]

            if data["movie_id"]:
                actor.movie_id = data["movie_id"]

            try:
                actor.update()
                return jsonify({"success": True, "actor": [actor.format()]}), 200
            except Exception:
                db.session.rollback()
                abort(500)
        else:
            abort(404)

    # Delete /actors
    @app.route("/actors/<int:id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(auth_data, id):
        actor = Actors.query.filter(Actors.id == id).one_or_none()

        if actor:
            try:
                actor.delete()
                return jsonify({"success": True, "delete": id}), 200
            except Exception:
                db.session.rollback()
                abort(500)
        else:
            abort(404)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": 404, "message": "Not Found"}), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return (
            jsonify(
                {"success": False, "error": 422, "message": "Unprocessable Entity"}
            ),
            422,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify(
                {"success": False, "error": 500, "message": "Internal Server Error"}
            ),
            500,
        )

    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        response = jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        })
        response.status_code = error.status_code
        return response

    return app

def build_login_link():

    return (
        "https://"
        + AUTH0_DOMAIN
        + "/authorize?"
        + urlencode(
            {
                "redirect_uri": url_for("callback", _external=True),
                "client_id": AUTH0_CLIENT_ID,
                "audience": API_AUDIENCE,
                "response_type": "token",
            }
        )
    )

app = create_app()

if __name__ == "__main__":
    app.run()
