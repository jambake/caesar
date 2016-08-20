# Formation Assignment

import webapp2
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar - Rot13</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Caesar - Rot13</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):

    def get(self):

        edit_header = "<h3>New Title Goes Here</h3>"

        user_form="""
        <form method="post">
            <textarea name="text" style="height: 50px; width: 200px;"></textarea>
            <br>
            <input type="submit">
        </form>
        """

        main_content = edit_header + user_form
        response = page_header + main_content + page_footer
        self.response.write(response)

    def post(self):

        text_answer = self.request.get("text")
        answer = encrypt(text_answer, 13)
        self.redirect("/?text=" + answer)
        #self.response.write(answer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
