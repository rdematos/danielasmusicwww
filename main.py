#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        sender = self.request.get("email")
        name = self.request.get("name")
        body = self.request.get("message")
        message = mail.EmailMessage(sender="rdematos@gmail.com", subject='Danielas Music - Message from: ' + name + ' (' + sender + ')')
        message.to = "rdematos@gmail.com"
        message.body = body
        message.send()
        notification_text = 'Message sent. Thank you!'
        template_values = {
        'notification': notification_text
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))

class MobilePage(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'templates/mobile.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        sender = self.request.get("email")
        name = self.request.get("name")
        body = self.request.get("message")
        message = mail.EmailMessage(sender="rdematos@gmail.com", subject='Danielas Music - Message from: ' + name + ' (' + sender + ')')
        message.to = "rdematos@gmail.com"
        message.body = body
        message.send()
        notification_text = 'Message sent. Thank you!'
        template_values = {
        'notification': notification_text
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/mobile.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/mobile', MobilePage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()