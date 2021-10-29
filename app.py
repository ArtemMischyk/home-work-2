from flask import Flask


app = Flask(__name__)

data: list[str] = ["29.10.2021, 15:20" "[Dinner at restaurant, Family]"
                  ,"31.10.2021, 21:00" "[Party at house, Other]"
                  ,"19.6.2021, 11:00" "[Playing volleyball at the beach w/ Mark]"
                  ,"4.7.2021, 13:45" "[Swimming in the pool at sport club, Work]"]



@app.route("/")
def index():
    return "<br>".join(data)

if __name__ == "__main__":
    app.run(debug=True)
