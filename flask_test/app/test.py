import os
from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
 patch_request_class

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()  # 文件储存地址
# print(os.getcwd() + '\\tmp')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # 文件大小限制，默认为16MB

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=上传>
    </form>
    '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        file_url = photos.url(filename)
        return html + '<br><img src=' + file_url + '>'
    return html


# if __name__ == '__main__':
#     app.run()



# test 1
# from flask import Flask, render_template, flash, session, redirect, url_for
# from wtforms import TextAreaField
# from wtforms.validators import DataRequired
# from flask_wtf import FlaskForm
# from flask_wtf.recaptcha import RecaptchaField


# DEBUG = True
# SECRET_KEY = 'secret'


# # google的验证？？
# # keys for localhost. Change as appropriate.

# RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

# app = Flask(__name__)
# app.config.from_object(__name__)


# class CommentForm(FlaskForm):

#     comment = TextAreaField("Comment", validators=[DataRequired()])
#     recaptcha = RecaptchaField()


# @app.route("/")
# def index(form=None):
#     if form is None:
#         form = CommentForm()
#     comments = session.get("comments", [])
#     return render_template("test.html",
#                            comments=comments,
#                            form=form)


# @app.route("/add/", methods=("POST",))
# def add_comment():

#     form = CommentForm()
#     if form.validate_on_submit():
#         comments = session.pop('comments', [])
#         comments.append(form.comment.data)
#         session['comments'] = comments
#         flash("You have added a new comment")
#         return redirect(url_for("index"))
#     return index(form)


# if __name__ == "__main__":
#     app.run()