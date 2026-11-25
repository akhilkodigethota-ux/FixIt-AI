from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    diagnosis = ""

    if request.method == "POST":
        problem = request.form.get("problem")

        solutions = {
            "slow": "Close unnecessary apps, restart your device, and check storage space.",
            "overheating": "Clean ventilation areas, avoid using the device on soft surfaces, and close heavy applications.",
            "wifi": "Restart your router, turn Wi-Fi off and on, and check whether other devices can connect.",
            "battery": "Reduce brightness, close background applications, and check battery usage.",
            "no_sound": "Check volume, audio output settings, and reconnect your headphones if connected.",
            "not_starting": "Check the power connection, charger, and battery. Try holding the power button for 10 seconds."
        }

        diagnosis = solutions.get(
            problem,
            "Please select a valid problem."
        )

    return render_template("index.html", diagnosis=diagnosis)


if __name__ == "__main__":
    app.run(debug=True)