from uk.Algorithm.AStar import AStar
from uk.Algorithm.AStar_t import AStar_t
from uk.Heuristics.Manhattan import Manhattan
import json
import time
from uk.Heuristics.Nielssen import Nielssen
from uk.Heuristics.Out_Row_Column import Out_row_column

__author__ = 'ricardo'

from flask import Flask, Response

app = Flask(__name__)



# Defining Heuristc Manhathan object giving a goal state
mh  = Manhattan([[1,2,3],[8,0,4],[7,6,5]])
nl  = Nielssen([[1,2,3],[8,0,4],[7,6,5]])
out  = Out_row_column([[1,2,3],[8,0,4],[7,6,5]])
#Creating an Astar object parsin the heuristic the initial state and the goal state
#--- heuristic must implement method calculate so you can define any object heuristic

@app.route("/")
def root():
    print(app.send_static_file('index.html'))
    return app.send_static_file('index.html')


@app.route("/api/<puzzle>/<heuristic>")
def api_compute(puzzle,heuristic):
    #print(puzzle)
    puzzle_raw = puzzle.split(',')
    computable_format = [[0,0,0],[0,0,0],[0,0,0]]

    computable_format[0][0] = int(puzzle_raw[0])
    computable_format[0][1] = int(puzzle_raw[1])
    computable_format[0][2] = int(puzzle_raw[2])
    computable_format[1][0] = int(puzzle_raw[3])
    computable_format[1][1] = int(puzzle_raw[4])
    computable_format[1][2] = int(puzzle_raw[5])
    computable_format[2][0] = int(puzzle_raw[6])
    computable_format[2][1] = int(puzzle_raw[7])
    computable_format[2][2] = int(puzzle_raw[8])
    print(heuristic)

    #print(computable_format)
    if heuristic == "mh":
        star = AStar_t(mh,computable_format,[[1,2,3],[8,0,4],[7,6,5]])
    elif heuristic == "nl":
        star = AStar_t(nl,computable_format,[[1,2,3],[8,0,4],[7,6,5]])
    elif heuristic == "out":
        star = AStar_t(out,computable_format,[[1,2,3],[8,0,4],[7,6,5]])

    starttime = time.time()
    computed = star.execute()
    finishtime  = time.time()

    response = json.dumps(computed)
    print(response)
    return Response(response, mimetype="application/json")


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True,threaded=True)