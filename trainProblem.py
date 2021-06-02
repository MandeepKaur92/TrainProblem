from flask import Flask
app = Flask(__name__)
@app.route("/")
def route():
    edges = [['A', 'B', 5], ['C', 'D', 8], ['D', 'C', 8], ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2],
             ['E', 'B', 3], ['A', 'E', 7], ['B', 'C', 4]]
    shotest = []
    routes=[]
    start = 'A'
    end = 'C'
    count = 0
    for i, val in enumerate(edges):
        r1 = edges[i][0]
        r2 = edges[i][1]
        for j , val in enumerate(edges):
            k=j+1
            if k == len(edges):
                break
            else:
                if r1 == start and r2 == end:
                    distance=edges[i][2]
                    print(f"{start}-{end} :{distance}")
                    routes.append(start,end,str(distance))
                    return f'Route, {str(start)}-{str(end)}-{str(distance)}'
                    break
                else:
                    if (r2 == edges[k][0] and r1==start) and (edges[k][1] == end) :
                                distance_1=edges[i][2]
                                distance_2=edges[k][2]
                                distance = distance_1 + distance_2
                                print(f"{r1}-{edges[k][0]}-{edges[k][1]}")
                                print("Distance:",distance)
                                count+=1
                                shotest.append(distance)
                                r=str(r1)
                                edges_k_0=str(edges[k][0])
                                edges_k_1=str(edges[k][1])
                                dist=str(distance)
                                routes.append(r+"-"+edges_k_0+"-"+edges_k_1+"   distance:"+dist)

        for i in range(len(shotest)-1):
            if shotest[i]< shotest[i + 1]-1:
                min=shotest[i]
            else:
                min=shotest[i+1]
    print("shortest path distance:",min)
    print("Number of routes",count)
    return f'Number of routes:{str(count)}, {routes} , Shortest Path:{str(min)}'

route()
if __name__ == '__main__':
    app.run()
