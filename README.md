# autograder-hungs3

First, I tried to get Sketch working by downloading the tar ball from Armando Solar-Lezama's website [link](https://people.csail.mit.edu/asolar/) but after going through the compilation and make commands, sketch wouldn't work since my Java version wasn't 1.6. Efforts to find OpenJDK 6 failed as it seems to have been obsoleted:

![image](https://user-images.githubusercontent.com/4023674/117716679-bda34b80-b18e-11eb-8a4b-d11a008ee056.png)

A quick look into ubuntu's [package library](https://packages.ubuntu.com/search?keywords=openjdk) shows that the earliest openjdk they have is openjdk8 but Sketch requires Java 1.6.

After this I pivoted to trying to work out the first part of the paper which was the `Program Rewriter`. This was the part of the program that was dedicated to turning python files into .mpy files. This was done by applying the EML (error model language) rules created by the instructor. As part of my implementation I essentially used regex to identify variables and the associated rules. Then I replaced the areas matching the EMl rules with the original and the applied code. This process mostly works and can be seen in a conversion form `test.py` to `test.mpy`. One issue I ran into was the fine-tuning of regex as it seemed to mess up the "range" rule.
