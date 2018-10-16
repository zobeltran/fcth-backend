"""
    Client Vue
"""

import os
from flask import Blueprint, render_template

client_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',
                      status_folder='./dist/static/'
                      template_folder='./dist/')

