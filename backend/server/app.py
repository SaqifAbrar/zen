from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/")
def hello_world():
    return "<p>You've accessed /api</p>"

@app.route("/api/generate", methods=["POST"])
def generate():
    query = request.args["query"]

    # This is where a RAG would determine what kind of information to break the webpage down.
    # E.g. for a query such as "What are koi fish?", the RAG would determine that the page
    # should be broken down into sections such as "Description", "Top 5 Results and Summaries", 
    # "Generic info" ("Habitat", "Diet", etc.).
    #
    # Due to time contstraints, the pipline is not implemented here, however for the example of a
    # web browser, refer to the Figma design. This is an example test for a RAG model to generate
    # content for the query "What are koi fish?".


    response = {
        "heading_sum": {
            "result": "Koi are a type of colored variant of the common carp, Cyprinus carpio, that are kept for decorative purposes in outdoor koi ponds or water gardens. They are known for their bright colors and patterns, and there are many varieties recognized by the Japanese, including the Gosanke category which consists of the Kōhaku, Taishō Sanshoku, and Shōwa Sanshoku varieties. Koi can live up to 100-200 years, with reports of individuals reaching ages of over 200 years in captivity. They are omnivorous and eat a wide variety of foods, including peas, lettuce, and watermelon, as well as commercial koi food designed to be nutritionally balanced and float so that they can be encouraged to come to the surface to eat. In winter, their digestive systems slow nearly to a halt, and they require fewer meals but larger ones to maintain weight. Temperatures for feeding koi vary depending on the location and time of year, with a general rule of not feeding during the winter months when water temperatures are below 40°F",
            "source":"https://en.wikipedia.org/wiki/koi",
            "image":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Ojiya_Nishikigoi_no_Sato_ac_%283%29.jpg/2560px-Ojiya_Nishikigoi_no_Sato_ac_%283%29.jpg",
        },
        "result_1": {
            "result": "Koi are a type of colored variant of the common carp, Cyprinus carpio, that are kept for decorative purposes in outdoor koi ponds or water gardens. They are known for their bright colors and patterns, and there are many varieties recognized by the Japanese, including the Gosanke category which consists of the Kōhaku, Taishō Sanshoku, and Shōwa Sanshoku varieties. Koi can live up to 100-200 years, with reports of individuals reaching ages of over 200 years in captivity. They are omnivorous and eat a wide variety of foods, including peas, lettuce, and watermelon, as well as commercial koi food designed to be nutritionally balanced and float so that they can be encouraged to come to the surface to eat. In winter, their digestive systems slow nearly to a halt, and they require fewer meals but larger ones to maintain weight. Temperatures for feeding koi vary depending on the location and time of year, with a general rule of not feeding during the winter months when water temperatures are below 40°F",
            "source":"https://en.wikipedia.org/wiki/koi",
        }
    }
    
    print(response)


    return response
