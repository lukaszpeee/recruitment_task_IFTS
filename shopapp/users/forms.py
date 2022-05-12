from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ShoppingListForm(FlaskForm):
    shopping_list_name = StringField('List name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('create')