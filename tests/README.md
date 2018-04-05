"
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Dev docstring
### TestDocstring2MD

````python
class TestDocstring2MD:
````

><br />
> Unittest class to test the package <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <br />
> <br />

#### TestCase.__call__
````python
def TestCase.__call__(self, *args, **kwds):
````
><br />
> Call self as a function. <br />
> <br />
#### TestCase.__eq__
````python
def TestCase.__eq__(self, other):
````
><br />
> Return self==value. <br />
> <br />
#### TestCase.__hash__
````python
def TestCase.__hash__(self):
````
><br />
> Return hash(self). <br />
> <br />
#### TestCase.__init__
````python
def TestCase.__init__(self, methodName='runTest'):
````
><br />
> Create an instance of the class that will use the named test <br />
> method when executed. Raises a ValueError if the instance does <br />
> not have a method with the specified name. <br />
> <br />
#### TestCase.__repr__
````python
def TestCase.__repr__(self):
````
><br />
> Return repr(self). <br />
> <br />
#### TestCase.__str__
````python
def TestCase.__str__(self):
````
><br />
> Return str(self). <br />
> <br />
#### TestCase._addExpectedFailure
````python
def TestCase._addExpectedFailure(self, result, exc_info):
````
><br />
>  <br />
> <br />
#### TestCase._addSkip
````python
def TestCase._addSkip(self, result, test_case, reason):
````
><br />
>  <br />
> <br />
#### TestCase._addUnexpectedSuccess
````python
def TestCase._addUnexpectedSuccess(self, result):
````
><br />
>  <br />
> <br />
#### TestCase._baseAssertEqual
````python
def TestCase._baseAssertEqual(self, first, second, msg=None):
````
><br />
> The default assertEqual implementation, not type specific. <br />
> <br />
#### TestCase._deprecate
````python
def TestCase._deprecate(original_func):
````
><br />
>  <br />
> <br />
#### TestCase._feedErrorsToResult
````python
def TestCase._feedErrorsToResult(self, result, errors):
````
><br />
>  <br />
> <br />
#### TestCase._formatMessage
````python
def TestCase._formatMessage(self, msg, standardMsg):
````
><br />
> Honour the longMessage attribute when generating failure messages. <br />
> <b> If longMessage is False this means: </b> <br />
> * Use only an explicit message if it is provided <br />
> * Otherwise use the standard message for the assert <br />
>  <br />
> <b> If longMessage is True: </b> <br />
> * Use the standard message <br />
> * If an explicit message is provided, plus ' : ' and the explicit message <br />
> <br />
#### TestCase._getAssertEqualityFunc
````python
def TestCase._getAssertEqualityFunc(self, first, second):
````
><br />
> Get a detailed comparison function for the types of the two args. <br />
>  <br />
> Returns: A callable accepting (first, second, msg=None) that will <br />
> raise a failure exception if first != second with a useful human <br />
> readable error message for those types. <br />
> <br />
#### TestCase._truncateMessage
````python
def TestCase._truncateMessage(self, message, diff):
````
><br />
>  <br />
> <br />
#### TestCase.addCleanup
````python
def TestCase.addCleanup(self, function, *args, **kwargs):
````
><br />
> Add a function, with arguments, to be called when the test is <br />
> completed. Functions added are called on a LIFO basis and are <br />
> called after tearDown on test failure or success. <br />
>  <br />
> Cleanup items are called even if setUp fails (unlike tearDown). <br />
> <br />
#### TestCase.addTypeEqualityFunc
````python
def TestCase.addTypeEqualityFunc(self, typeobj, function):
````
><br />
> Add a type specific assertEqual style function to compare a type. <br />
>  <br />
> This method is for use by TestCase subclasses that need to register <br />
> their own type equality functions to provide nicer error messages. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   typeobj: The data type to call this function on when both values <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   are of the same type in assertEqual(). <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   function: The callable taking two arguments and an optional <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg= argument that raises self.failureException with a <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   useful error message when the two arguments are not equal. <br />
> <br />
#### TestCase.assertAlmostEqual
````python
def TestCase.assertAlmostEqual(self, first, second, places=None, msg=None, delta=None):
````
><br />
> Fail if the two objects are unequal as determined by their <br />
> difference rounded to the given number of decimal places <br />
> (default 7) and comparing to zero, or by comparing that the <br />
> between the two objects is more than the given delta. <br />
>  <br />
> Note that decimal places (from zero) are usually not the same <br />
> as significant digits (measured from the most significant digit). <br />
>  <br />
> If the two objects compare equal then they will automatically <br />
> compare almost equal. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertCountEqual
````python
def TestCase.assertCountEqual(self, first, second, msg=None):
````
><br />
> An unordered sequence comparison asserting that the same elements, <br />
> regardless of order.  If the same element occurs more than once, <br />
> it verifies that the elements occur the same number of times. <br />
>  <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.assertEqual(Counter(list(first)), <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    Counter(list(second))) <br />
>  <br />
> <b>  Example: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   - [0, 1, 1] and [1, 0, 1] compare equal. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   - [0, 0, 1] and [0, 1] compare unequal. <br />
> <br />
#### TestCase.assertDictContainsSubset
````python
def TestCase.assertDictContainsSubset(self, subset, dictionary, msg=None):
````
><br />
> Checks whether dictionary is a superset of subset. <br />
> <br />
#### TestCase.assertDictEqual
````python
def TestCase.assertDictEqual(self, d1, d2, msg=None):
````
><br />
>  <br />
> <br />
#### TestCase.assertEqual
````python
def TestCase.assertEqual(self, first, second, msg=None):
````
><br />
> Fail if the two objects are unequal as determined by the '==' <br />
> operator. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertFalse
````python
def TestCase.assertFalse(self, expr, msg=None):
````
><br />
> Check that the expression is false. <br />
> <br />
#### TestCase.assertGreater
````python
def TestCase.assertGreater(self, a, b, msg=None):
````
><br />
> Just like self.assertTrue(a > b), but with a nicer default message. <br />
> <br />
#### TestCase.assertGreaterEqual
````python
def TestCase.assertGreaterEqual(self, a, b, msg=None):
````
><br />
> Just like self.assertTrue(a >= b), but with a nicer default message. <br />
> <br />
#### TestCase.assertIn
````python
def TestCase.assertIn(self, member, container, msg=None):
````
><br />
> Just like self.assertTrue(a in b), but with a nicer default message. <br />
> <br />
#### TestCase.assertIs
````python
def TestCase.assertIs(self, expr1, expr2, msg=None):
````
><br />
> Just like self.assertTrue(a is b), but with a nicer default message. <br />
> <br />
#### TestCase.assertIsInstance
````python
def TestCase.assertIsInstance(self, obj, cls, msg=None):
````
><br />
> Same as self.assertTrue(isinstance(obj, cls)), with a nicer <br />
> default message. <br />
> <br />
#### TestCase.assertIsNone
````python
def TestCase.assertIsNone(self, obj, msg=None):
````
><br />
> Same as self.assertTrue(obj is None), with a nicer default message. <br />
> <br />
#### TestCase.assertIsNot
````python
def TestCase.assertIsNot(self, expr1, expr2, msg=None):
````
><br />
> Just like self.assertTrue(a is not b), but with a nicer default message. <br />
> <br />
#### TestCase.assertIsNotNone
````python
def TestCase.assertIsNotNone(self, obj, msg=None):
````
><br />
> Included for symmetry with assertIsNone. <br />
> <br />
#### TestCase.assertLess
````python
def TestCase.assertLess(self, a, b, msg=None):
````
><br />
> Just like self.assertTrue(a < b), but with a nicer default message. <br />
> <br />
#### TestCase.assertLessEqual
````python
def TestCase.assertLessEqual(self, a, b, msg=None):
````
><br />
> Just like self.assertTrue(a <= b), but with a nicer default message. <br />
> <br />
#### TestCase.assertListEqual
````python
def TestCase.assertListEqual(self, list1, list2, msg=None):
````
><br />
> A list-specific equality assertion. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   list1: The first list to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   list2: The second list to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg: Optional message to use on failure instead of a list of <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   differences. <br />
> <br />
#### TestCase.assertLogs
````python
def TestCase.assertLogs(self, logger=None, level=None):
````
><br />
> Fail unless a log message of level *level* or higher is emitted <br />
> on *logger_name* or its children.  If omitted, *level* defaults to <br />
> INFO and *logger* defaults to the root logger. <br />
>  <br />
> This method must be used as a context manager, and will yield <br />
> a recording object with two attributes: `output` and `records`. <br />
> At the end of the context manager, the `output` attribute will <br />
> be a list of the matching formatted log messages and the <br />
> `records` attribute will be a list of the corresponding LogRecord <br />
> objects. <br />
>  <br />
> <b> Example:: </b> <br />
>  <br />
> <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   with self.assertLogs('foo', level='INFO') as cm: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   logging.getLogger('foo').info('first message') <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   logging.getLogger('foo.bar').error('second message') <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.assertEqual(cm.output, ['INFO:foo:first message', <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'ERROR:foo.bar:second message']) <br />
> <br />
#### TestCase.assertMultiLineEqual
````python
def TestCase.assertMultiLineEqual(self, first, second, msg=None):
````
><br />
> Assert that two multi-line strings are equal. <br />
> <br />
#### TestCase.assertNotAlmostEqual
````python
def TestCase.assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None):
````
><br />
> Fail if the two objects are equal as determined by their <br />
> difference rounded to the given number of decimal places <br />
> (default 7) and comparing to zero, or by comparing that the <br />
> between the two objects is less than the given delta. <br />
>  <br />
> Note that decimal places (from zero) are usually not the same <br />
> as significant digits (measured from the most significant digit). <br />
>  <br />
> Objects that are equal automatically fail. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertNotEqual
````python
def TestCase.assertNotEqual(self, first, second, msg=None):
````
><br />
> Fail if the two objects are equal as determined by the '!=' <br />
> operator. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertNotIn
````python
def TestCase.assertNotIn(self, member, container, msg=None):
````
><br />
> Just like self.assertTrue(a not in b), but with a nicer default message. <br />
> <br />
#### TestCase.assertNotIsInstance
````python
def TestCase.assertNotIsInstance(self, obj, cls, msg=None):
````
><br />
> Included for symmetry with assertIsInstance. <br />
> <br />
#### TestCase.assertNotRegex
````python
def TestCase.assertNotRegex(self, text, unexpected_regex, msg=None):
````
><br />
> Fail the test if the text matches the regular expression. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertRaises
````python
def TestCase.assertRaises(self, expected_exception, *args, **kwargs):
````
><br />
> Fail unless an exception of class expected_exception is raised <br />
> by the callable when invoked with specified positional and <br />
> keyword arguments. If a different type of exception is <br />
> raised, it will not be caught, and the test case will be <br />
> deemed to have suffered an error, exactly as for an <br />
> unexpected exception. <br />
>  <br />
> If called with the callable and arguments omitted, will return a <br />
> <b> context object used like this:: </b> <br />
>  <br />
> <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    with self.assertRaises(SomeException): </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    do_something() <br />
>  <br />
> An optional keyword argument 'msg' can be provided when assertRaises <br />
> is used as a context object. <br />
>  <br />
> The context manager keeps a reference to the exception as <br />
> the 'exception' attribute. This allows you to inspect the <br />
> <b> exception after the assertion:: </b> <br />
>  <br />
> <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   with self.assertRaises(SomeException) as cm: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   do_something() <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   the_exception = cm.exception <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.assertEqual(the_exception.error_code, 3) <br />
> <br />
#### TestCase.assertRaisesRegex
````python
def TestCase.assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs):
````
><br />
> Asserts that the message in a raised exception matches a regex. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   expected_exception: Exception class expected to be raised. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   expected_regex: Regex (re pattern object or string) expected <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   to be found in error message. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   args: Function to be called and extra positional args. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   kwargs: Extra kwargs. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg: Optional message used in case of failure. Can only be used <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   when assertRaisesRegex is used as a context manager. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertRegex
````python
def TestCase.assertRegex(self, text, expected_regex, msg=None):
````
><br />
> Fail the test unless the text matches the regular expression. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.assertSequenceEqual
````python
def TestCase.assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None):
````
><br />
> An equality assertion for ordered sequences (like lists and tuples). <br />
>  <br />
> For the purposes of this function, a valid ordered sequence type is one <br />
> which can be indexed, has a length, and has an equality operator. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   seq1: The first sequence to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   seq2: The second sequence to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   seq_type: The expected datatype of the sequences, or None if no <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   datatype should be enforced. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg: Optional message to use on failure instead of a list of <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   differences. <br />
> <br />
#### TestCase.assertSetEqual
````python
def TestCase.assertSetEqual(self, set1, set2, msg=None):
````
><br />
> A set-specific equality assertion. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   set1: The first set to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   set2: The second set to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg: Optional message to use on failure instead of a list of <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   differences. <br />
>  <br />
> assertSetEqual uses ducktyping to support different types of sets, and <br />
> is optimized for sets specifically (parameters must support a <br />
> difference method). <br />
> <br />
#### TestCase.assertTrue
````python
def TestCase.assertTrue(self, expr, msg=None):
````
><br />
> Check that the expression is true. <br />
> <br />
#### TestCase.assertTupleEqual
````python
def TestCase.assertTupleEqual(self, tuple1, tuple2, msg=None):
````
><br />
> A tuple-specific equality assertion. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   tuple1: The first tuple to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   tuple2: The second tuple to compare. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg: Optional message to use on failure instead of a list of <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   differences. <br />
> <br />
#### TestCase.assertWarns
````python
def TestCase.assertWarns(self, expected_warning, *args, **kwargs):
````
><br />
> Fail unless a warning of class warnClass is triggered <br />
> by the callable when invoked with specified positional and <br />
> keyword arguments.  If a different type of warning is <br />
> triggered, it will not be handled: depending on the other <br />
> warning filtering rules in effect, it might be silenced, printed <br />
> out, or raised as an exception. <br />
>  <br />
> If called with the callable and arguments omitted, will return a <br />
> <b> context object used like this:: </b> <br />
>  <br />
> <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    with self.assertWarns(SomeWarning): </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    do_something() <br />
>  <br />
> An optional keyword argument 'msg' can be provided when assertWarns <br />
> is used as a context object. <br />
>  <br />
> The context manager keeps a reference to the first matching <br />
> warning as the 'warning' attribute; similarly, the 'filename' <br />
> and 'lineno' attributes give you information about the line <br />
> of Python code from which the warning was triggered. <br />
> <b> This allows you to inspect the warning after the assertion:: </b> <br />
>  <br />
> <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   with self.assertWarns(SomeWarning) as cm: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   do_something() <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   the_warning = cm.warning <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.assertEqual(the_warning.some_attribute, 147) <br />
> <br />
#### TestCase.assertWarnsRegex
````python
def TestCase.assertWarnsRegex(self, expected_warning, expected_regex, *args, **kwargs):
````
><br />
> Asserts that the message in a triggered warning matches a regexp. <br />
> Basic functioning is similar to assertWarns() with the addition <br />
> that only warnings whose messages also match the regular expression <br />
> are considered successful matches. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   expected_warning: Warning class expected to be triggered. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   expected_regex: Regex (re pattern object or string) expected <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   to be found in error message. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   args: Function to be called and extra positional args. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   kwargs: Extra kwargs. <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   msg: Optional message used in case of failure. Can only be used <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   when assertWarnsRegex is used as a context manager. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.countTestCases
````python
def TestCase.countTestCases(self):
````
><br />
>  <br />
> <br />
#### TestCase.debug
````python
def TestCase.debug(self):
````
><br />
> Run the test without collecting errors in a TestResult <br />
> <br />
#### TestCase.defaultTestResult
````python
def TestCase.defaultTestResult(self):
````
><br />
>  <br />
> <br />
#### TestCase.doCleanups
````python
def TestCase.doCleanups(self):
````
><br />
> Execute all cleanup functions. Normally called for you after <br />
> tearDown. <br />
> <br />
#### TestCase.fail
````python
def TestCase.fail(self, msg=None):
````
><br />
> Fail immediately, with the given message. <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase._deprecate.<locals>.deprecated_func
````python
def TestCase._deprecate.<locals>.deprecated_func(*args, **kwargs):
````
><br />
>  <br />
> <br />
#### TestCase.id
````python
def TestCase.id(self):
````
><br />
>  <br />
> <br />
#### TestCase.run
````python
def TestCase.run(self, result=None):
````
><br />
>  <br />
> <br />
#### TestCase.setUp
````python
def TestCase.setUp(self):
````
><br />
> Hook method for setting up the test fixture before exercising it. <br />
> <br />
#### TestCase.shortDescription
````python
def TestCase.shortDescription(self):
````
><br />
> Returns a one-line description of the test, or None if no <br />
> description has been provided. <br />
>  <br />
> The default implementation of this method returns the first line of <br />
> the specified test method's docstring. <br />
> <br />
#### TestCase.skipTest
````python
def TestCase.skipTest(self, reason):
````
><br />
> Skip this test. <br />
> <br />
#### TestCase.subTest
````python
def TestCase.subTest(self, msg=<object object at 0x7f0a83651160>, **params):
````
><br />
> Return a context manager that will return the enclosed block <br />
> of code in a subtest identified by the optional message and <br />
> keyword parameters.  A failure in the subtest marks the test <br />
> case as failed but resumes execution at the end of the enclosed <br />
> block, allowing further test code to be executed. <br />
> <br />
#### TestCase.tearDown
````python
def TestCase.tearDown(self):
````
><br />
> Hook method for deconstructing the test fixture after testing it. <br />
> <br />
#### TestDocstring2MD.test_docstring2md
````python
def TestDocstring2MD.test_docstring2md(self):
````
><br />
> Function to validate the package <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <br />
> <br />
