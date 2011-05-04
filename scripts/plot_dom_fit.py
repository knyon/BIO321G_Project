from avida_file_tools import *
from pylab import *
from numpy import *

def dom_fitness(treatment):
    dom_files = get_dominant_fitness(treatment)
    trt = []

    for file in dom_files:
        trt.append(get_column(file,4))

    return trt

def extract_median(data):
    med = []
    n = data.shape[1]
    for x in range(0,n):
        med.append(median(data[:,x],axis=0)[0,0])

    return med

#control treatment
control = dom_fitness("C_")
RpD = dom_fitness("RpD_")
RvD = dom_fitness("RvD_")

ControlMedian = extract_median(matrix(control))
RpDMedian = extract_median(matrix(RpD))
RvDMedian = extract_median(matrix(RvD))

plot(range(0,201),log10(ControlMedian))
plot(range(0,201),log10(RpDMedian))
plot(range(0,201),log10(RvDMedian))

grid()


title("Log10 of Median fitness")

xticks([40,80,120,160,200],('50','100','150','200','250'))
xlabel('Update (x1000)')

yticks([0,1,2,3,4,5],('0','10^1','10^2','10^3','10^4','10^5'))
ylabel('Log10 Median Fitness')

#makeboxplot("Final Dominant Fitness (log10)",200,0,"Log10(Fitness)","Control",transpose(log10(matrix(control))),"RvD",transpose(log10(matrix(RvD))),"RpD",transpose(log10(matrix(RpD))))
import scipy.stats as sp
print sp.mannwhitneyu(matrix(control)[:,200],matrix(RpD)[:,200])

savefig('test.svg')
raw_input()
