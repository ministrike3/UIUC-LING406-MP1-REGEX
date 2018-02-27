# UIUC-LING406-MP1-REGEX
MP1 for Ling 406@UIUC; features regex to detect date/time/season words in a newspaper article


The problem that I tried to solve for the first assignment of LING406 is to extract information relating to dates in a News Article.
Things like 'Thanksgiving', "January 1st 2018", 'The 3rd of December', 'Monday the 3rd', etc.

____________________________________

The program I have written is named DateExtractor.py .
I solved the problem using 4 regex equations. One to hunt down big terms like January 1st 2018.
The second to hunt down things like 'Monday the 3rd'.
The third to find stuff like 'The 3rd of December', and the last to find holidays like 'Thanksgiving'.
I kept track of where in the text each thing appeared so that at the end I could display them chronologically by article position.

____________________________________

You should be able to run it in terminal (using 'python3 Datextractor.py') or in an IDE.
It was written being tested with Python 3.5.2, but should be functional with any of the python3 releases.

____________________________________

It currently runs on the testarticle file in the Test_Inputs Folder; the article came from the Wall Street Journal's website.
I added a line about the Holidays at the bottom of the article so that I could also test for those.

____________________________________

To test it against the TA's output, please either copy and paste the text into this test article file
or
Put a copy of the TA file into Test Inputs and change the path in Line 6 of my python code accordingly.
