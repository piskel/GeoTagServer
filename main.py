
from geotag import GeoTag
from tag_manager import TagManager
from flask import Flask, request, jsonify


# Must open port on the server machine
HOST = "0.0.0.0" 
PORT = 1234


app = Flask(__name__)
tm = TagManager()


@app.route("/")
def index():
    return "GeoTag API Server"


# POST /api/geotag
# Adds a new geotag
@app.route("/api/geotag", methods=["POST"])
def api_geotag_post():
    """
    API endpoint to add a geotag to the database
    """
    # Get the data from the POST request
    data = request.get_json()
    print(data)
    # Create a GeoTag object from the data
    tag = GeoTag(data["latitude"], data["longitude"])
    tm.add_tag(tag )# Add the tag to the database
    # Return a success message
    return jsonify({"message": "Successfully added tag"})


# GET /api/geotag
# Returns all the geotags in the database
@app.route("/api/geotag", methods=["GET"])
def api_geotag_get():
    """
    API endpoint to get all the geotags in the database
    """
    # Get all the tags from the database
    tags = tm.get_all_tags()
    return jsonify(tags)


# tm.reset_db() # Uncomment to reset the database
app.run(host=HOST, port=PORT, debug=True)
