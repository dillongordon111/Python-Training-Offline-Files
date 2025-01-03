
import numpy as np
import streamlit as st
import pandas as pd 

st.title('Heat transfer calculator')


#Heat transfer for water
gpm = (st.number_input("Enter GPM"))
dt = (st.number_input("Enter Temperature Differential in F"))
t2 = (st.number_input("Enter Temperature 2 in F"))
t1 = (st.number_input("Enter Temperature 1 in F"))
gp = (st.number_input("Enter Glycol %"))
oat = (st.number_input("Enter Outside Air Temperature in F"))
cf = 1
gph = gpm * 60

if gp == 50:
    cf = .000018 * oat + .875
elif gp == 40:
    cf = .0000639 * oat + .91
elif gp == 30: 
    cf = 8e-05 * oat +.94
elif gp == 20:
    cf = 1e-05 * oat +.97
elif gp == 0:
    cf = -.00044 * oat + 1.05
def water(gph,dt,t2,t1,gp,oat,cf):
    if dt != 0:
        return 500 * gph * dt * cf
    else:
        return 500 * gph * (t2-t1) * cf   
    
heat_transfer = water(gph,dt,t2,t1,gp,oat,cf)
st.write(str(round(heat_transfer, 2)) + " BTU/Hr")


def converttombh(heat_transfer):
    return (heat_transfer/1000)

mbh = converttombh(heat_transfer)
st.write(str(round(mbh, 2)) + " MBH/Hr")