# Script: Tax.py
# Author: Martina Atkinson L00177769
# Purpose: To calculate total tax
# Prerequisites: None
# Tested: 29/9/2012

# create and assign values to variables
income = 100000
single_person_tax_allowance = 36800
# calculate taxable income @ 20%
taxable_at_20_percent = income - single_person_tax_allowance
# calculate taxable income @ 40%
taxable_at_40_percent = income - taxable_at_20_percent
# income taxable @ 20% and 40%
percent_tax_20 = taxable_at_20_percent * .2
percent_tax_40 = taxable_at_40_percent * .4
# total tax paid equals amount paid at 20% plus 40%
total_tax = percent_tax_20 + percent_tax_40
# print total tax
print(total_tax)
