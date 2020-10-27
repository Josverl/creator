"Just create new dummy stubfile"

import tempfile

tf = tempfile.NamedTemporaryFile(delete=False,prefix='stub_',dir='./stubs',suffix='.py', mode="w+")
print(tf.name)
tf.write("# Just a stubfile")
tf.close()

# X
