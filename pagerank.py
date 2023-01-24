import time
import numpy as np
from scipy import sparse

# Nodes: 875713 Edges: 5105039

beta = float(input("input beta:"))
iterator_times = int(input("input iterator time:"))
time_start=time.time()
total_nodes = 875713
Edges = 5105039

'''test_path = 'web-Google2.txt'
read_file = open(test_path)'''
path = 'web-Google.txt'
read_file = open(path)
page_set = []
row = []
col = []
mtx_dt = []
flag = True

def is_changed(node,old_node):
    if node == old_node:
        return False
    else:
        return True
def write_all(list_infor):
    with open("PageRank.txt","w") as w:
        for i in list_infor:
            w.write('{} {}\n'.format("Result", i))
    #w.write("Execution time is ")
    w.close()
def largest(list_infor,infor2):
    with open("Top_10_Nodes.txt","w") as w:
        w.write("From Top1 to Top 10 \n")
        for j in range(10):
            w.write('{} {}  {}\n'.format("Node", list_infor[j],infor2[j]))
    #w.write("Execution time is " + time)
    w.close()
def calulate(Matrix,v0,v1):
    v0 = Matrix*v0 + v1
    return v0

max_node_num = 0
max_node2_num = 0
for line in read_file:
    if line[0] != '#':
        split_line = line.strip().split('\t')
        '''
            0	11342
            0	824020
            0	867923
            0	891835
            11342	0
            11342	27469
            11342	38716
            11342	309564
            11342	322178
            11569   1
        '''
        if flag == True:
            flag = False
            node = split_line[0]
            count = 1
            page_set.append(split_line)
        elif is_changed(split_line[0],node) and flag is not True:
            prob = 1 /(count)
            cor = beta * prob
            for i in range(count):
                str = (page_set[i])
                row.append(str[0])
                col.append(str[1])
                if max_node_num < int(str[0]):
                    max_node_num = int(str[0])
                else:
                    max_node_num = max_node_num
                if max_node2_num<int(str[1]):
                    max_node2_num = int(str[1])
                else:
                    max_node2_num = max_node2_num
                mtx_dt.append(cor)
            page_set.clear()
            page_set.append(split_line)
            node = split_line[0]
            count = 1
        else:
            count += 1
            page_set.append(split_line)

max_node = max(max_node2_num,max_node_num)+1
Matrix = sparse.csr_matrix((mtx_dt,(col,row)), shape=(max_node, max_node))

v0 = max_node*[(1/max_node)] 
e  = 1
p2= max_node*[(1-beta)*e/max_node] 

for i in range(iterator_times):
    temp = calulate(Matrix,v0,p2)
    v0 = temp

sort_data = np.argsort(-v0)
result = []
for i in range(10):
    result.append(sort_data[i])
result1 = []
for i in range(10):
    result1.append(v0[result[i]])

write_all(v0)
largest(result,result1)
print("Top ten nodes: ",result)
time_end=time.time()
execution_time_og = time_end-time_start
execution_time = round(execution_time_og,3)

print('time cost',execution_time,'second')
