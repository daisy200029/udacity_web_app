# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader =jinja2.FileSystemLoader(template_dir),
                    autoescape=True)



class Handler(webapp2.RequestHandler):
    # *a is a list
    # **kw is a  dictionary
    def write(self, *a, **kw):
    	self.response.out.write(*a,**kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class FizzBuzzHandler(Handler):
    def get(self):
        n=self.request.get('n',0)        
        n = n and int(n)
        print  n
        self.render('fizzbuzz.html',n=n)
class MainPage(Handler):
    def get(self):
        items=self.request.get_all("food")
        self.render("shopping_list.html",items=items)
    	# output = form_html
    	# output_hidden = ""
    	# items = self.request.get_all("food")
    	# if items:
    	# 	output_items=""
	    # 	for item in items:
	    # 		## store data in the url
	    # 		output_hidden += hidden_html % item
	    # 		output_items += item_html % item
    		
    	# 	output_shopping = shopping_list_html % output_items
    	# 	output += output_shopping
    	# output = output % output_hidden
     #    self.write(output)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fizzbuzz', FizzBuzzHandler)
], debug=True)
