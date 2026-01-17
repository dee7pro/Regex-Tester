from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def regex_tester():
    regex = ""
    text = ""
    matches = []
    error = None

    if request.method == "POST":
        regex = request.form.get("regex", "")
        text = request.form.get("text", "")

        try:
            # finditer gives better control than findall
            matches = [match.group() for match in re.finditer(regex, text)]
        except re.error as e:
            error = f"Invalid Regular Expression: {e}"

    return render_template(
        "index.html",
        regex=regex,
        text=text,
        matches=matches,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
