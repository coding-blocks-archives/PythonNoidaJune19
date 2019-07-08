from flask import Flask, render_template

app = Flask("My Application")

# Create a json file of articles
# with following fields
# {
#   "slug": "",
#   "authors": "",
#   "title": "",
#   "body": ""
# }

USERS = [
  {
    "id": 1,
    "name": "Jatin Katyal"
  },
  {
    "id": 2,
    "name": "Chirag Malhotra"
  },
  {
    "id": 3,
    "name": "Sakshi Malhotra"
  }
]

@app.route('/')
def index():
  return "Hello World !"

@app.route('/users')
def users():
  return render_template('users.html', users=USERS)

@app.route('/users/<int:id>')
def user(id):
  try:
    user = next(filter(lambda x: x["id"] == id, USERS))
    return render_template('user.html', **user)
    # return render_template('user.html', id=user["id"], name=user["name"])
    # return "{} - {}".format(user['id'], user['name'])
  except StopIteration:
    return "404 Not Found"

if __name__ == "__main__":
  app.run(port = 8080, debug = True)
