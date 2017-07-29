# Author: Matt Xiao
# Data frame from ThinkStats

import nsfg
import thinkstats2
import thinkplot

df = nsfg.ReadFemPreg()


hist = thinkstats2.Hist([1, 2, 2, 3, 5])

thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')



