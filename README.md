Getting Started with the Python Adapter in TestStand


1.  Introduction

2.  Installation of Required Software

    1.  TestStand 2019 (32-bit and 64-bit)

    2.  Python (32-bit and 64-bit)

    3.  Configuring the Environment Variable

3.  Running a Code Module Step

    1.  Calling a Python Function from TestStand

    2.  Passing Data Structures

        1.  Native TestStand Support

        2.  Object References

    3.  Loading and Calling Functions from a Python Class in TestStand

    4.  Edit Time vs Run Time Interpreters

4.  Configuring Multiple Interpreters

    1.  Global, Per Execution and Per Thread

    2.  Interpreters at Run Time

    3.  Shared Resources Between Executions and Threads

Introduction 
=============

TestStand 2019 introduced the Python Adapter which allows Python code to be
called from TestStand sequences. TestStand has supported adapters for other
language such as LabVIEW, .NET, C++, and CVI, and now Python allows developers
additional flexibility in their test design. Python steps can be used for
offloading data analysis and hardware control. Python modules for NI-DAQmx,
NI-SCOPE, NI-FGEN, NI-DMM, NI-DCPower, NI-SWITCH, and NI-ModInst can be found at
[NI Modular Instruments Python
Documentation](https://nimi-python.readthedocs.io/en/master/).

Installation of Required Software
=================================

TestStand
---------

The latest version of TestStand can be downloaded from our [TestStand Download
Page](http://www.ni.com/en-us/support/downloads/software-products/download.teststand.html#305461).
For Python Adapter support, TestStand 2019 or later will be required. Verify
that you have a supported operating system, listed in the right-hand pane on the
download page, for TestStand 2019. TestStand has both 32-bit and 64-bit
versions. It is important to maintain the same bitness across the different
software tools used in development. If you use particular bitness of TestStand,
then you must use the same bitness of Python.

Python
------

Python can be installed from <https://www.python.org/downloads/>. TestStand 2019
supports Python 2.7+ and 3.6+. Again, the bitness of the Python installation
must match the bitness of your installed TestStand.

Configuring the Environment 
----------------------------

In order for TestStand to find the Python Interpreter to use, Python will need
to be added to the PATH environment variable. Many installations of Python will
automatically add their path to the PATH environment variable, and TestStand
looks in some default locations. However, to ensure TestStand has access to
Python, it is recommended the path be added. You can change the PATH environment
variable on Windows 10 with the following steps:

1.  Open **File Explorer**.

2.  Right click on **This PC** and select **Properties**.

3.  Click on **Advanced system settings**.

4.  Make sure you are on the **Advanced** tab and click on **Environment
    Variables**.

5.  Select the **Path** variable under **User variables of \<username\>** and
    click **Edit**.

6.  Click **New** to add additional environment variables. You should add paths
    to the Python Installation and the scripts folder.

    An example of a properly configured PATH environment variable is provided
    below for a Windows 10 machine with Python installed at the top of the C
    drive. Paths to both the Python folder and the Scripts folder should be
    included.

    ![](media/d736fe2cd2e3d6f2c25f9b47bc7cdee3.tiff)

Figure 1: Configured PATH Environment Variable

You will need to restart TestStand and any TestStand tools for the Python
Adapter to utilize the edited environment variable.

Once your operating system’s environment is configured, you can configure the
Python Adapter in TestStand. The Python Adapter Configuration window can be
accessed via **Configure\>\>Adapters\>\>Configure (with Python Selected)**. Here
the default interpreter and Python version can be set. The Python version is
pulled from the interpreters configured in your PATH environment variable. For
instance, if you have both Python 2.7 and Python 3.6, you will have those two
options will be available.

![](media/09d83852ec73937d4784e854671af9b9.tiff)

Figure 2: Python Adapter Configuration

Running a Code Module Step
==========================

Calling a Python Function from TestStand
----------------------------------------

Python can be selected as the default for code modules using the Selected
Adapter dropdown. Once an action step is added to a sequence, the adapter can
also be selected in the **General** section of the **Properties** tab of **Step
Settings**.

Any IDE or text editor can be used to develop Python functions to be called from
TestStand. To show how a function can be called from TestStand, the following
function will be used. The function simply returns whatever is passed into it.

def hello_world(string_to_return):

return string_to_return

This function can be added to a Python action step within a sequence. Within the
**Module** tab of the **Step Settings**, the script that contains this function,
getting_started.py, is referenced. The **Operation Scope** is set to **Module**
and the **Operation Type** is set to **Call Method**. The creation and use of a
class will be covered later in this guide. When you select the function name,
the function prototype is loaded into the **Step Settings**. Here TestStand
loads **Return Value** and **string_to_return**. You can select how you want to
pass arguments and store the return value of the function using the **Type** and
**Value** fields.

![](media/08ddcacc667f37e8263451b5da403f67.tiff)

Figure 3: Step Settings Example for Calling a Python Method

When the step is run as configured, it will pass the string Hello World into the
Python function and which will return the same string to be stored in
Locals.MethodReturnVal.

Passing Data Structures 
------------------------

### Native TestStand Support

It is important to note that TestStand is strictly typed while Python is
dynamically typed. TestStand supports several standard object types such as a
string, numeric, or Boolean. The full list of types can be seen in the type
dropdown to the right of the parameters for a Python step.

![TestStand_Types.PNG](media/c37a41208d4a40465f1feb910b7389a8.png)

Figure 4: Types for Python Parameters

When passing these data types between Python scripts and TestStand sequences,
care needs to be taken to insure proper type casting. TestStand offers the
Dynamic type to help with this process. In the example above, the type that was
being passed to and returned from TestStand was Dynamic. Strict types can be
used if you are certain of the type being passed into and received from your
Python module.

### Object References

More complex data structures can be stored in TestStand as object references and passed to Python functions. An example of this is provided below where the [date object](https://docs.python.org/2/library/datetime.html#date-objects) is returned to TestStand and stored as a Python object reference. This reference is passed into another function which returns the year data member of the date object. Below is the first function which returns a date object: 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def return_data_structure():

return date.today()

![](media/1730fa3ca00702c9e81cb2f1e81f815d.tiff)

Figure 5: Step Settings for Passing Data Structure to TestStand

The variable Locals.DateInstance is watched during execution, you will see that
the object reference is a Python Object.

![](media/219a0e9de30ef0111eebd503912571e0.tiff)

Figure 6: Python Object in Watch Expression Pane During Run-Time

The second function which accepts the variable returned from the previous
function as an argument is defined below.

def accept_object_reference(today):

return today.year

![](media/13a16ad06d3d1af8d8ccfa581952d1df.tiff)

Figure 7: Passing Data Structure to Python Function

The numeric that is returned and stored in Locals.ReturnYear is the year
associated with the date object.

Loading and Calling Functions from a Python Class in TestStand
--------------------------------------------------------------

Classes can also be loaded into TestStand, and other steps can be used to get
and set their data members and call their methods. For this guide, we will load
the class HelloWorld and call a method within the class, hello_world.

class HelloWorld:

def \__init__(self):

self.message = "Hello World Class"

def hello_world(self):

return self.message

For this example, another step was created, and the step settings were
configured with the same code module, getting_started.py. A class reference is
created by using the **Operation Type**, **Create Class Instance**. The class
instance is stored in the **Return Value** of the step. In the example below,
the reference is stored in FileGlobals.HelloWorld.

![](media/5e83b6618c5cb4f7c3a71e2d347a266c.tiff)

Figure 8: Step Settings Example for Creating a Class Reference

Once the class reference is loaded into TestStand, it can be used in other
Python steps. To use the class reference, the module is loaded again, the
**Operation Scope** is set to **Class Instance**, and the **Class Instance** is
obtained from the variable where it is stored, in this case
FileGlobals.HelloWorld. The **Class Name** is set to the class that is being
referenced, in this case it is **HelloWorld**. The **Operation Type** for the
example below is **Call Method** and the **Function Name** being called is
**hello_world**.

![](media/6fc4556706d7625d379927b1cb21c4dd.tiff)

Figure 9: Step Settings for Calling a Class Method

When these steps are executed, a class reference is created and stored in
TestStand. The class reference is then used to call the class method,
hello_world. It is important to note that the class instance must be used in the
same interpreter it was created in. Configuring the interpreter is covered in
the section below on Configuring Multiple Interpreters.

Edit-Time vs Run-Time Interpreters
----------------------------------

In order to populate the dropdown options for **Class Name** and **Function
Name** and expose function and class prototypes, TestStand uses an edit-time
interpreter to parse the code module. As such you should never have code outside
import statements, class definitions, and function definitions. This will cause
the interpreter to execute the code leading to undefined and unwanted behavior.

Configuring Multiple Interpreters
=================================

When a Python step accesses an interpreter, it grabs the [Global Interpreter
Lock](https://docs.python.org/2/glossary.html#term-global-interpreter-lock) for
that interpreter. This is a limitation of the Python interpreter to prevent it
from being used simultaneously from multiple threads. This prevents other code
modules from using the that interpreter and executing at the same time. This
slows down test time and reduces the parallelism of your test. Parallel calls to
the Python interpreter are serialized non-deterministically. To increase the
parallelism of your test, you can configure multiple interpreters in a variety
of ways.

Global, Per Execution and Per Thread
------------------------------------

The Python adapter can be configured within the Python Adapter Configuration
window found via **Configure\>\>Adapters\>\>Configure (with Python Selected)**.
For the Python interpreter to use these setting, there are three options to
choose from: Global, Per Execution, and Per Thread. These settings change the
scope of the default interpreter for Python steps. It is important to note that
objects cannot be shared between Python interpreters.

Interpreters at Run-Time
------------------------

Additional interpreters can also be instantiated at run-time and can be used
with a given class instance. This is done by selecting the Advanced Settings
button in the top right of the **Module** tab in **Step Settings**.

![](media/a58cb678b583d9e90ac593506cd494a8.tiff)

Figure 10: Configuring Interpreter Reference

The **Advanced Settings** window allows the user to configure the step to follow
the adapter settings for a Python interpreter or to use a specified Python
interpreter. Selecting **Object Reference** for the **Python Interpreter to
use** option allows you to input an **Interpreter Reference** and to **Create
Interpreter if it does not exist**. In the example above, the interpreter is
referenced in FileGlobals.HelloWorldInterpreter. If a class is instantiated with
an interpreter, that interpreter must be used for future steps with that class
reference.

Shared Resources Between Executions and Threads
-----------------------------------------------

If additional parallelism is needed when running a Batch or Parallel process
model, the additional interpreters can be created using the methods mention
above. However, two problems remain even with multiple interpreters. First,
hardware and class references cannot be shared between interpreters making
sharing between executions more difficult. Second, instantiating all hardware
and class references in a single interpreter will also cause execution threads
to wait for an interpreter to be released.

As sequence complexity grows, it is recommended that an interpreter is created
for each class to prevent interpreter locking. For example, consider a Batch
model where each execution needs access to a class that uses an FGEN and Scope,
a class that uses a SMU, and a class that uses a DMM. One recommended solution
is to create class references and interpreters for each class that are
accessible to each execution. This allows each execution to access the hardware
when they are available. If multiple steps must be executing without giving up a
hardware reference, [Synchronization Step
Types](https://zone.ni.com/reference/en-XX/help/370052W-01/tsref/infotopics/sync_step_types/)
can be used within TestStand.
