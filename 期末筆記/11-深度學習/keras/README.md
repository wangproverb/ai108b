# Keras + Tensorflow

執行失敗

```
PS D:\ccc\course\ai\python\10-deepLearning\keras\mlpRegression> python mlpRegression.py
Using TensorFlow backend.
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: DLL load failed: 動態連結程式庫 (DLL) 初始化例行程序失敗。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "mlpRegression.py", line 1, in <module>
    from keras.datasets import boston_housing
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\__init__.py", line 3, in <module>
    from . import utils
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\__init__.py", line 6, in <module>
    from . import conv_utils
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\conv_utils.py", line 9, in <module>
    from .. import backend as K
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\backend\__init__.py", line 1, in <module>
    from .load_backend import epsilon
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\backend\load_backend.py", line 90, in <module>
    from .tensorflow_backend import *
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\backend\tensorflow_backend.py", line 5, in <module>
    import tensorflow as tf
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\__init__.py", line 28, in <module>
    from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 74, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: DLL load failed: 動態連結程式庫 (DLL) 初始化例行程序失敗。


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
```