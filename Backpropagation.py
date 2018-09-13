import numpy as np

# initialize -----------------------
data_x = [0.6, 0.7]
data_y = [0.5, 0.6]
ERRORo1 = 100.0
ERRORo2 = 100.0
ERRORtotal = 100.0

w1 = 0.40
w2 = 0.55
w3 = 0.45
w4 = 0.30

w5 = 0.65
w6 = 0.25
w7 = 0.35
w8 = 0.50

first_rate = 0.3
second_rate = 0.05
# -----------------------------------

def COMBI(i1, w1, i2, w2):
    return (i1 * w1) + (i2 * w2)

def SIGMOID(x):
    return 1 / (1 + np.e**(-x))

def ERROR(real, output):
    return 1 / 2 * (real - output)**2

def ERRORTOTAL():
    return ERRORo1 + ERRORo2

def ErrorDiffOut(out, real): # error differential about out
    return out - real

def SIGMOID_DIFF(x):  # sigmoid differential about x
    return SIGMOID(x) * (1 - SIGMOID(x))

def COMMON_VALUE(NET, INPUT):
    return SIGMOID_DIFF(NET) * INPUT

def FIRST_SLOPE(OUTo, REAL, NETo, OUTh):
    return ErrorDiffOut(OUTo, REAL) * SIGMOID_DIFF(NETo) * OUTh

def STEP_SECOND_SLOPE(OUTo1, REAL1, NETo1, WEIGHT, NETh1, INPUT1):
    return FIRST_SLOPE(OUTo1, data_y[0], NETo1, w5) * COMMON_VALUE(NETh1, data_x[0])

def SECOND_SLOPE(OUTo1, REAL1, NETo1, WEIGHT1, OUTo2, REAL2, NETo2, WEIGHT2, NETh1, INPUT1):
    return STEP_SECOND_SLOPE(OUTo1, REAL1, NETo1, WEIGHT1, NETh1, INPUT1) + STEP_SECOND_SLOPE(OUTo2, REAL2, NETo2, WEIGHT2, NETh1, INPUT1)

print("##INITIAL VALUE##")
print("dataset[0] : ({0},{1}), dataset[1] : ({2}, {3})".format(data_x[0], data_y[0], data_x[1], data_y[1]))
print("w1 : {0}, w2 : {1}, w3 : {2}, w4 : {3}".format(w1, w2, w3, w4))
print("w5 : {0}, w6 : {1}, w7 : {2}, w8 : {3}".format(w5, w6, w7, w8))
print("ERRORo1 : {0}, ERRORo2 : {1}, ERRORtotal : {3}".format(ERRORo1, ERRORo2, ERRORtotal))

while ERRORtotal > 0.00001:
    NETh1 = COMBI(data_x[0], w1, data_x[1], w2)
    OUTh1 = SIGMOID(NETh1)
    NETh2 = COMBI(data_x[0], w3, data_x[1], w4)
    OUTh2 = SIGMOID(NETh2)

    NETo1 = COMBI(OUTh1, w5, OUTh2, w6)
    OUTo1 = SIGMOID(NETo1)
    NETo2 = COMBI(OUTh1, w7, OUTh2, w8)
    OUTo2 = SIGMOID(NETo2)

    ERRORo1 = ERROR(data_y[0], OUTo1)
    ERRORo2 = ERROR(data_y[1], OUTo2)

    ERRORtotal = ERRORTOTAL()

    print("#############################################")
    print("NETh1 : {0}, OUTh1 : {1}".format(NETh1, OUTh1))
    print("NETh2 : {0}, OUTh2 : {1}".format(NETh2, OUTh2))
    print("Eo1 : {0}, Eo2 : {1}".format(ERRORo1, ERRORo2))
    print("Error Total : {0}".format(ERRORtotal))
    print("#############################################")

    w1 = w1 - (second_rate * SECOND_SLOPE(OUTo1, data_y[0], NETo1, w5, OUTo2, data_y[1], NETo2, w7, NETh1, data_x[0]))
    w2 = w2 - (second_rate * SECOND_SLOPE(OUTo1, data_y[0], NETo1, w5, OUTo2, data_y[1], NETo2, w7, NETh1, data_x[1]))
    w3 = w3 - (second_rate * SECOND_SLOPE(OUTo1, data_y[0], NETo1, w6, OUTo2, data_y[1], NETo2, w8, NETh2, data_x[0]))
    w4 = w4 - (second_rate * SECOND_SLOPE(OUTo1, data_y[0], NETo1, w6, OUTo2, data_y[1], NETo2, w8, NETh2, data_x[1]))

    w5 = w5 - (first_rate * FIRST_SLOPE(OUTo1, data_y[0], NETo1, OUTh1))
    w6 = w6 - (first_rate * FIRST_SLOPE(OUTo1, data_y[0], NETo1, OUTh2))
    w7 = w7 - (first_rate * FIRST_SLOPE(OUTo2, data_y[1], NETo2, OUTh1))
    w8 = w8 - (first_rate * FIRST_SLOPE(OUTo2, data_y[1], NETo2, OUTh2))
