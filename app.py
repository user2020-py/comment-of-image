from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def main():
    name = ""
    if request.method == "POST":
        name = request.form.get("FULLname")
        comment = request.form.get("comment")
        with open("data.json") as data:
            json_data = json.load(data)
        json_data.append({
            "fullname": name if bool(name) else "Unknown User",
            "user_comment": comment
        })
        with open("data.json", 'w') as appending:
            json.dump(json_data, appending, indent=4, separators=(',',': '))

        print(name, comment)
    return render_template("index.html", 
                            FULLname=name, 
                            comments=json.load(open("data.json")))

if __name__ == '__main__':
    app.run()