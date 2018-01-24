#!/bin/python3.6
import sys

height = float(input("What is your height? (inches or meeters) "))
weight = float(input("What is your weight? ( pounds or kgs) "))
unit =  input("Are your measurements in metric or imperial units? ").lower().strip()

if unit.startswith('i'):
    bmi = 703 * ( weight / (height ** 2))
elif unit.startswith('m'):
    bmi = 703 * ( weight / (height ** 2))

print("Your BMI is %s" %bmi)
