# autograder-hungs3

First, I tried to get Sketch working by downloading the tar ball from Armando Solar-Lezama's website [link](https://people.csail.mit.edu/asolar/) but after going through the compilation and make commands, sketch wouldn't work since my Java version wasn't 1.6. Efforts to find OpenJDK 6 failed as it seems to have been obsoleted:

![image](https://user-images.githubusercontent.com/4023674/117716679-bda34b80-b18e-11eb-8a4b-d11a008ee056.png)

A quick look into ubuntu's [package library](https://packages.ubuntu.com/search?keywords=openjdk) shows that the earliest openjdk they have is openjdk8 but Sketch requires Java 1.6.
