from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    ## users = User.get_all()
    ## print(users)
    return render_template("create_user.html") ##, all_users = users)

@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create(data)
    return redirect("/read_all")

@app.route("/read_all")
def show_all():
    users = User.get_all()
    print(users)
    return render_template("/read_all.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)