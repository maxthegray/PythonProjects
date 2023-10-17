import os
import random

with open("SATQuestions.txt", "w"):
    for i in range(1, 366):
        f.write("\n## Question {}\n".format(i))
        f.write("\nQ: This is question number {}?".format(i))
        f.write("\nA: Correct answer for question".format(i))
        f.write("\nB: Wrong answer 1 for question".format(i))
        f.write("\nC: Wrong answer 2 for question".format(i))
        f.write("\nD: Wrong answer 3 for question".format(i))
