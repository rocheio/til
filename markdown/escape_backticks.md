Escaping Backticks in Markdown
==============================

In a normal text section, backticks (\`) must be escaped with a backslash to appear as intended. In plain text, this looks like `` \` ``.

In a code block, in order to 'escape' a backtick, the code containing the backtick must be surrounded by double backticks. If the backtick to be escaped starts or ends the code block, you must include an extra space between the single backtick and the surrounding ones. In plain text, this looks like ``` ``ctrl + ` `` ```.  Markdown will remove this extra space when styling your text. 

This method of escaping backticks works for many levels, so in order to escape five backticks, you just need to wrap them in six backticks. Compare the output of the code block `````` ````` `````` to its plain text for an example.
