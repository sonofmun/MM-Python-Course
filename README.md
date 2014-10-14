# Python Programming for the Humanities

The programming language [Python](http://www.python.org) is widely used within many scientific domains nowadays and the language is readily accessible to scholars from the Humanities. Python is an excellent choice for dealing with (linguistic as well as literary) textual data, which is so typical of the Humanities. In this book you will be thoroughly introduced to the language and be taught to program basic algorithmic procedures. The book expects no prior experience with programming, although we hope to provide some interesting insights and skills for more advanced programmers as well. The book consists of 10 chapters. Chapter 5 and Chapter 6 are still in draft status and not ready for use.

This document describes the installation procedure for all the software needed for the Python class. If your stuck anywhere in the installation procedure, please do not hesitate to contact Folgert Karsdorp (folgert.karsdorp@meertens.knaw.nl).

## Sublime text

We advice you to install a good text editor, Sublime text 2 for example. However, you are absolutely free to use your own favorite editor. For Sublime Text 2 go to http://www.sublimetext.com/ download the version for your operating system and install.

In the course we will be using software that works best with Google Chrome. Firefox 6 (or above) and Safari will also work. Internet Explorer is not supported. 

We will be using Python 3 for our course. Lower versions are more or less supported, but not recommended.


## Installation
### Windows and OS X

**We strongly advice you to install the Anaconda Python Distribution.** This distribution contains all the necessary modules and packages needed for this course. It is available for all platforms and provides a simple installation procedure/ You can download it from: http://continuum.io/downloads. More detailed installation instructions can be found here: http://docs.continuum.io/anaconda/install.html 

Anaconda's default installation is Python 2.7. However, we will use Python 3 in this course. To install all necessary packages for Python 3, type 

    conda create -n py34 python=3.4 anaconda

followed by

    source activate py34

at the command line. If you work on a Windows machine, use the following command instead:

    activate py34

(If this doesn't work, have a look here: http://continuum.io/blog/anaconda-python-3). After that you can start the course with double clicking the file start-windows.bat (if you are working on Windows) or start-unix.sh if you work with Linux or start-osx.command if you work on Mac OS X.

### Windows
Download and install the Anaconda Python Distribution (see above).

Double click the file start-windows.bat.

If everything goes right, this should open your browser (preferably Google Chrome or Firefox) on a page http://127.0.0.1:8888/ (or something similar) which says `IP[y]: Notebook'. If for some reason, the notebook is opened by Internet Explorer, copy the URL and paste that in either Google Chrome or Firefox.

### OS X 
Only take these steps if you know what you are doing. Otherwise, simply download and install the Anaconda Python Distribution (see above). After that, double click the file start-osx.command.

First you will need to install Xcode from the App Store. After you have successfully installed Xcode, open Xcode and go to Xcode -> preferences -> Downloads. Now click on the install button next to commandline tools. 

Open spotlight and type in `terminal' to open the terminal application. (You can also go to your applications folder and then to utilities where you'll find the terminal.app)

Cd to the folder where you downloaded or saved the file mac-installer.sh (probably in ~/Downloads) by using

    cd /folder/of/mac-installer.sh 

Run the installer with the following command. The installer will download some packages and will request for your password to install them.

    . mac-installer.sh

To check your installation, relaunch the terminal.app. Then type in 

    ipython3 notebook --matplotlib=inline

If everything went well this should open your browser (best with Google Chrome or Firefox) on the page http://127.0.0.1:8888/ which says IP[y]: Notebook.

### Linux (Ubuntu/Debian)

Because of some problems with Anaconda, matplotlib, and Linux, we advise you to install Python 3.4 and a virtualenv instead of using Anaconda.
Note, you will need administrator privileges on your computer to do this.

First, open a terminal and type (Freetype is necessary to install matplotlib)

    sudo apt-get install python3, libfreetype6-dev
    
Once Python 3 has finished installing, go to your 'home' directory (i.e., ~) and type

    virtualenv WS2014 --python=usr/bin/python3
    
This will create a virtualenv using Python3 into which you can install all the necessary packages for this course.  Once this is finished, type

    cd WS2014
    
then

    source bin/activate
    
Your virtualenv is now active.  Notice the (WS2014) before your current path in your terminal.  Now, copy the 'requirements.txt' file from the directory where this readme file is located to your ~/WS2014 folder.  
Go back to your WS2014 folder in your terminal and then type

    pip install -r requirements.txt
    
This will start installing all of the packages that are necessary for this course.
Once all of the packages finish installing, in your terminal cd to the directory where this readme file and all of the IPython Notebooks are located and type

    ipython3 notebook

If everything went well this should open your browser (best with Google Chrome or Firefox) to the page http://127.0.0.1:8888/ which says IP[y]: Notebook.

If you run another Linux distribution, similar packages should be available.

## Contributors
- Folgert Karsdorp
- Maarten van Gompel
- Matt Munson
