from flask import Flask, jsonify, request
from rag import zen_rag

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>You've zengine backend</p>"

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

    result = zen_rag(query)


    response = {
        "heading_sum": {
            "generated": result,
            "source":"https://en.wikipedia.org/wiki/koi",
            "image":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Ojiya_Nishikigoi_no_Sato_ac_%283%29.jpg/2560px-Ojiya_Nishikigoi_no_Sato_ac_%283%29.jpg",
        },
        "result_1": {
            "generated": "Koi are a type of colored variant of the common carp, Cyprinus carpio, that are kept for decorative purposes in outdoor koi ponds or water gardens. They are known for their bright colors and patterns, and there are many varieties recognized by the Japanese, including the Gosanke category which consists of the Kōhaku, Taishō Sanshoku, and Shōwa Sanshoku varieties. Koi can live up to 100-200 years, with reports of individuals reaching ages of over 200 years in captivity.",
            "source":"https://en.wikipedia.org/wiki/koi",
        }
    }

    print(response)


    return response
