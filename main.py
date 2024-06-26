from flask import Flask , jsonify , request 
app = Flask('Contacts')

{
  "data" : [
    {
      "Contact" : "998844466" ,
      "Name" : "Ram" , 
      "done" : False , 
      "id" : 1
    },
    {
      "Contact" : "998844466" ,
      "Name" : "Riddhi" ,
      "done" : False ,
      "id" : 2
    }
  ]
}

@app.route("/add-data" , methods=["POST"])
def add_task() :
  if not request.json :
    return jsonify({
      "status" : "error" ,
      "message" : "Please provide the data!"
    } , 400)