from flask import Flask, request, jsonify
import blood_calculator

blood_calculator.hdl_analysis

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "The class server is on."


@app.route("/info", methods=["GET"])
def provide_info():
    msg = "This server was written for BME 547.<br>"
    msg += "For questions, contact pratt@duke.edu"
    return msg


@app.route("/hdl", methods=["POST"])
def hdl_handler():
    """
    {"name": "David Ward", "HDL_value": 60}
    """
    in_json = request.get_json()
    hdl_value = in_json["HDL_value"]
    if type(hdl_value) is not int:
        return "You did not send the HDL value as an int", 400
    hdl_result = blood_calculator.hdl_analysis(hdl_value)
    answer = "For an hdl value of {}, it is {}".format(hdl_value,
                                                       hdl_result)
    return jsonify(in_json)


@app.route("/hdl/<hdl_value>", methods=["GET"])
def hdl_get_handler(hdl_value):
    hdl_value = int(hdl_value)
    hdl_result = blood_calculator.hdl_analysis(hdl_value)
    answer = "For an hdl value of {}, it is {}".format(hdl_value,
                                                       hdl_result)
    return answer


if __name__ == "__main__":
    app.run()
