from flask import render_template

from . import recipes_blueprint
from .crud import get_all_shoplists


@recipes_blueprint.route("/")
def home():
    shoplists = get_all_shoplists()
    return render_template('recipes/home.html', shoplists=shoplists)