from flask import Flask , render_template ,request 
import requests

app= Flask(__name__)
API_KEY ="a0e1e3df147647ebad9110730251105"

@app.route("/", methods = ["GET" , "POST"])

def weather():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(url)
        data= response.json()

        if "error" not in data:
             weather = {
                'city': data['location']['name'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'humidity': data['current']['humidity'],
                'wind': data['current']['wind_kph']
            }
        
        else:
            return "City Not Found"
        
    return render_template("index.html", weather = weather)

if __name__ == "__main__":
    app.run(debug=True)


