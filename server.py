from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    ## users = User.get_all()
    ## print(users)
    return render_template("/read_all.html", users = users)


# Create User
@app.route("/create_page")
def create_page():
    return render_template("/create_user.html")

@app.route("/create_user", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create(data)
    return redirect("/read_all")

# Show All Users
@app.route("/read_all")
def show_all():
    users = User.get_all()
    print(users)
    return render_template("/read_all.html", users = users)

# Show One User
@app.route("/user/show/<int:id>")
def show(id):
    data = {"id":id}
    return render_template("show_one_user.html", user = User.edit(data))

# Go to Edit One User Page
@app.route("/user/edit/<int:id>")
def edit(id):
    data = {"id":id}
    return render_template("edit_user.html", user = User.edit(data))

# Update User Information
@app.route("/user/update", methods = ['POST'])
def update():
    User.update(request.form)
    return redirect("/read_all") # <-------------------------------

# Delete User
@app.route("/user/delete/<int:id>")
def delete_user(id):
    data = {"id":id}
    User.delete_user(data)
    return redirect("/read_all")

if __name__ == "__main__":
    app.run(debug=True)
    