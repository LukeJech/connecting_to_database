from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    friends = Friend.get_all()
    return render_template("index.html", all_friends = friends)

# relevant code snippet from server.py
from friend import Friend
@app.route('/create_friend', methods=["POST"])
def create_friend():
    Friend.save(request.form)
    return redirect('/')
            

@app.route('/profile')
def show_friend():
    friend = Friend.read()
    print(friend)
    return render_template('profile.html', friend = friend[0])

if __name__ == "__main__":
    app.run(debug=True)

