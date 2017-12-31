import os
import re
from functions import *

import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
time_dict = {}
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

SPEED_RE = re.compile(r"^[0-9_-a-zA-Z]{3,12}$")
def valid_speed(speed):
    return SPEED_RE.match(speed)

SIZE_RE = re.compile(r"^[0-9_-a-zA-Z]{3,12}$")
def valid_size(speed):
    return SIZE_RE.match(size)

class Downtime(BaseHandler):

    def get(self):
        time_dict = dict(viz = "none")
        self.render('downtime.html', **time_dict)
	alpha = 21

    def post(self):
        has_error = False
        size = self.request.get('size')
        speed = self.request.get('speed')  
        time_dict, has_error = downtime(speed,size)
        self.render('downtime.html', **time_dict)

app = webapp2.WSGIApplication([('/', Downtime)], debug=True)