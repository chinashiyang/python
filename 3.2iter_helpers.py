import numpy as np
def scalar_product(a_array,b_array):
    result=None
    try:
        a_array=np.array(a_array,dtype=int)
        b_array=np.array(b_array,dtype=int)
        result=sum(a_array*b_array)
        #result=np.dot(a,b)
    except:
        print('Does not meet the conversion conditions！')
    print(result if result!=None else 'Inner product failure！')
scalar_product([1,'1'],[2, 2])
scalar_product([1,'az'],[2,2])