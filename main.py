# Copyright 2015 Google Inc. All Rights Reserved.
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

# [START app]

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/500')
def err_500():
    """Return a friendly HTTP greeting."""
    # return '500 page', 500
    import json, os, errno, random, traceback
    try:
        raise ValueError('value')
    except Exception as e:
        data = {
          "serviceContext": {
            "service": "default",
            # "version": 'v1'
          },
          "message": traceback.format_exc(),
        }
        filename = '/var/log/app_engine/custom_logs/errors.log.json'
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename), 0777)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, 'a+') as outfile:
            msg = json.dumps(data)
            outfile.write('\n'+msg)
        # raise
        return '500 page', 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
# [END app]
