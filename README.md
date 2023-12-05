# GPTLint: A ChatGPT-based Code Linter
All tested Python scripts can be found and accessed within the "test_scripts" folder.

Results of testing both PyLint and GPTLint on these scripts can be found within the "outputs" folder. Each tool has its own folder, containing results with file names that indicate which original script was tested (e.g. test_code_GPTLint.txt). GPTLint's outputs contain both a text output and a modified python script (with added comments), as per the instructions given to it.

Other resources accessible from the root of this repository include a shortcut to GPTLint ("GPTLint.html"), the instruction prompt given to GPTLint ("GPTLint_prompt.txt"), the Presentation Slides ("Presentation_Slides.pdf"), and the Project Report ("Project_Report.pdf").

To run your own PyLint tests, PyLint must be installed locally. This can be done on most machines through the command prompt / terminal with the command "`pip install pylint`". Then, navigate to the file path of the desired Python script and call "`pylint [fileName].py`" with the proper file name. The results of the analysis should output within the terminal. [More details on how to run PyLint can be found here.](https://archive.mantidproject.org/How_to_run_Pylint.html) 

To run your own GPTLint tests, you must navigate to GPTLint, either through the HTML shortcut found in the repo ("GPTLint.html"), or [by clicking here](https://chat.openai.com/g/g-rfsmtTW58-gptlint). A ChatGPT Membership is required. Once there, simply attach the desired Python file and send the otherwise blank prompt, and you will recieve a response with the test results. The resulting output should display both the modified code (with added comments) and the plain text results, as well as download links for each. Once you have recieved the response, feel free to follow-up with additional queries and questions as desired, such as for clarification on any suggestions.