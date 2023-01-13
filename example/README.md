JSON (JavaScript Object Notation) <https://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import json
    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(json.dumps('\u1234'))
    "\u1234"
    >>> print(json.dumps('\\'))
    "\\"
    >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Compact encoding::

    >>> import json
    >>> mydict = {'4': 5, '6': 7}
    >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'

Pretty printing::

    >>> import json
    >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
        "4": 5,
        "6": 7
    }

Decoding JSON::

    >>> import json
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> json.load(io)[0] == 'streaming API'
    True

Specializing JSON object decoding::

    >>> import json
    >>> def as_complex(dct):
    ...     if '__complex__' in dct:
    ...         return complex(dct['real'], dct['imag'])
    ...     return dct
    ...
    >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    ...     object_hook=as_complex)
    (1+2j)
    >>> from decimal import Decimal
    >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
    True

Specializing JSON object encoding::

    >>> import json
    >>> def encode_complex(obj):
    ...     if isinstance(obj, complex):
    ...         return [obj.real, obj.imag]
    ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
    ...                     f'is not JSON serializable')
    ...
    >>> json.dumps(2 + 1j, default=encode_complex)
    '[2.0, 1.0]'
    >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
    '[2.0, 1.0]'
    >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
    '[2.0, 1.0]'


Using json.tool from the shell to validate and pretty-print::

    $ echo '{"json":"obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
## Dev notes
### Objects:

#### JSONDecodeError()
```python
class JSONDecodeError(ValueError):
```
<pre>
<b>
Subclass of ValueError with the following additional properties:</b>

msg: The unformatted error message
doc: The JSON document being parsed
pos: The start index of doc where parsing failed
lineno: The line corresponding to pos
colno: The column corresponding to pos

</pre>
#### _decode_uXXXX()
```python
def _decode_uXXXX(s, pos):
```
<pre>

None

</pre>
#### py_scanstring()
```python
def py_scanstring(s, end, strict = True, _b = BACKSLASH, _m = STRINGCHUNK.match):
```
<pre>

Scan the string s for a JSON string. End is the index of the
character in s after the quote that started the JSON string.
Unescapes all valid JSON string escape sequences and raises ValueError
on attempt to decode an invalid string. If strict is False then literal
control characters are allowed in the string.

Returns a tuple of the decoded string and the index of the character in s
after the end quote.

</pre>
#### JSONObject()
```python
def JSONObject(s_and_end, strict, scan_once, object_hook, object_pairs_hook, memo = None, _w = WHITESPACE.match, _ws = WHITESPACE_STR):
```
<pre>

None

</pre>
#### JSONArray()
```python
def JSONArray(s_and_end, scan_once, _w = WHITESPACE.match, _ws = WHITESPACE_STR):
```
<pre>

None

</pre>
#### JSONDecoder()
```python
class JSONDecoder(object):
```
<pre>

Simple JSON <https://json.org> decoder
<b>
Performs the following translations in decoding by default:</b>

+---------------+-------------------+
| JSON          | Python            |
+===============+===================+
| object        | dict              |
+---------------+-------------------+
| array         | list              |
+---------------+-------------------+
| string        | str               |
+---------------+-------------------+
| number (int)  | int               |
+---------------+-------------------+
| number (real) | float             |
+---------------+-------------------+
| true          | True              |
+---------------+-------------------+
| false         | False             |
+---------------+-------------------+
| null          | None              |
+---------------+-------------------+

It also understands ``NaN``, ``Infinity``, and ``-Infinity`` as
their corresponding ``float`` values, which is outside the JSON spec.

</pre>
##### JSONDecoder.decode()
```python
def JSONDecoder.decode(self, s, _w = WHITESPACE.match):
```
<pre>

Return the Python representation of ``s`` (a ``str`` instance
containing a JSON document).

</pre>
##### JSONDecoder.raw_decode()
```python
def JSONDecoder.raw_decode(self, s, idx = 0):
```
<pre>

Decode a JSON document from ``s`` (a ``str`` beginning with
a JSON document) and return a 2-tuple of the Python
representation and the index in ``s`` where the document ended.

This can be used to decode a JSON document from a string that may
have extraneous data at the end.

</pre>
#### py_encode_basestring()
```python
def py_encode_basestring(s):
```
<pre>

Return a JSON representation of a Python string

    

</pre>
##### py_encode_basestring.replace()
```python
def py_encode_basestring.replace(match):
```
<pre>

None

</pre>
#### py_encode_basestring_ascii()
```python
def py_encode_basestring_ascii(s):
```
<pre>

Return an ASCII-only JSON representation of a Python string

    

</pre>
##### py_encode_basestring_ascii.replace()
```python
def py_encode_basestring_ascii.replace(match):
```
<pre>

None

</pre>
#### JSONEncoder()
```python
class JSONEncoder(object):
```
<pre>

Extensible JSON <https://json.org> encoder for Python data structures.
<b>
Supports the following objects and types by default:</b>

+-------------------+---------------+
| Python            | JSON          |
+===================+===============+
| dict              | object        |
+-------------------+---------------+
| list, tuple       | array         |
+-------------------+---------------+
| str               | string        |
+-------------------+---------------+
| int, float        | number        |
+-------------------+---------------+
| True              | true          |
+-------------------+---------------+
| False             | false         |
+-------------------+---------------+
| None              | null          |
+-------------------+---------------+

To extend this to recognize other objects, subclass and implement a
``.default()`` method with another method that returns a serializable
object for ``o`` if possible, otherwise it should call the superclass
implementation (to raise ``TypeError``).

</pre>
##### JSONEncoder.default()
```python
def JSONEncoder.default(self, o):
```
<pre>

Implement this method in a subclass such that it returns
a serializable object for ``o``, or calls the base implementation
(to raise a ``TypeError``).

For example, to support arbitrary iterators, you could
<b>implement default like this::</b>
<b>
    def default(self, o):</b>
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)

</pre>
##### JSONEncoder.encode()
```python
def JSONEncoder.encode(self, o):
```
<pre>

Return a JSON string representation of a Python data structure.

>>> from json.encoder import JSONEncoder
>>> JSONEncoder().encode({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'

</pre>
##### JSONEncoder.iterencode()
```python
def JSONEncoder.iterencode(self, o, _one_shot = False):
```
<pre>

Encode the given object and yield each string
representation as available.
<b>
For example::</b>
<b>
    for chunk in JSONEncoder().iterencode(bigobject):</b>
        mysocket.write(chunk)

</pre>
###### JSONEncoder.iterencode.floatstr()
```python
def JSONEncoder.iterencode.floatstr(o, allow_nan = self.allow_nan, _repr = float.__repr__, _inf = INFINITY, _neginf = -INFINITY):
```
<pre>

None

</pre>
#### _make_iterencode()
```python
def _make_iterencode(markers, _default, _encoder, _indent, _floatstr, _key_separator, _item_separator, _sort_keys, _skipkeys, _one_shot, ValueError = ValueError, dict = dict, float = float, id = id, int = int, isinstance = isinstance, list = list, str = str, tuple = tuple, _intstr = int.__repr__):
```
<pre>

None

</pre>
##### _make_iterencode._iterencode_list()
```python
def _make_iterencode._iterencode_list(lst, _current_indent_level):
```
<pre>

None

</pre>
##### _make_iterencode._iterencode_dict()
```python
def _make_iterencode._iterencode_dict(dct, _current_indent_level):
```
<pre>

None

</pre>
##### _make_iterencode._iterencode()
```python
def _make_iterencode._iterencode(o, _current_indent_level):
```
<pre>

None

</pre>
#### py_make_scanner()
```python
def py_make_scanner(context):
```
<pre>

None

</pre>
##### py_make_scanner._scan_once()
```python
def py_make_scanner._scan_once(string, idx):
```
<pre>

None

</pre>
##### py_make_scanner.scan_once()
```python
def py_make_scanner.scan_once(string, idx):
```
<pre>

None

</pre>
#### main()
```python
def main():
```
<pre>

None

</pre>