function display_computed_results(data)
{
    var generated_list;
    generated_list = '<ul class="list-group">';

    for (var i = data.solution_steps[0].length; i >1; i--)
    {
	       generated_list += '<li class="list-group-item">'+data.solution_steps[0][i]+'</li>';
    }


    generated_list += '</ul>';
    $("#results_list").html(generated_list);
}


var board = [[1,2,3],
             [8,0,4],
             [7,6,5]];

var position = [[0,0],[0,1],[0,2],
                [1,0],[1,1],[1,2],
                [2,0],[2,1],[2,2]];


// Initializing the canvas object
var canvas = oCanvas.create({
	canvas: "#puzzle"
});

var squares_list = [];

for (var i= 0; i < position.length; i++)
{


  var rectangle = canvas.display.rectangle({
  	x: position[i][1]*100,
  	y: position[i][0]*100,
  	width: 100,
  	height: 100,
  	fill: "#ddddda"
  });
  rectangle.tile_value = board[position[i][0]][position[i][1]];
  //(position[i]);
  var text = canvas.display.text({
  	x: 50,
  	y: 35,
  	origin: { x: "center", y: "top" },
  	font: "bold 30px sans-serif",
  	text: board[position[i][0]][position[i][1]] ,
  	fill: "#0aa"
  });
  rectangle.addChild(text);

  squares_list.push(rectangle);
}

for (var i= 0; i < position.length; i++)
{
  canvas.addChild(squares_list[i]);

}

canvas.bind("click tap", function(){

  for(var x = 0; x < computed_data.solution_steps.length ; x++)
  {
    setTimeout(timeout(x), 100000);
  }

});

function timeout(x)
{
  setTimeout(animate(x),100000);
}

function animate(x)
{
  for (var i= 0; i < squares_list.length; i++)
  {
    squares_list[i].remove();
    canvas.redraw();
  }
  squares_list = [];
  for (var i= 0; i < position.length; i++)
  {


    var rectangle = canvas.display.rectangle({
      x: position[i][1]*100,
      y: position[i][0]*100,
      width: 100,
      height: 100,
      fill: "#ddddda"
    });
    rectangle.tile_value = computed_data.solution_steps[x][position[i][0]][position[i][1]];
    //console.log(position[i]);
    var text = canvas.display.text({
      x: 50,
      y: 35,
      origin: { x: "center", y: "top" },
      font: "bold 30px sans-serif",
      text: computed_data.solution_steps[x][position[i][0]][position[i][1]] ,
      fill: "#0aa"
    });
    rectangle.addChild(text);

    squares_list.push(rectangle);
  }
  for (var i= 0; i < squares_list.length; i++)
  {
    squares_list[i].delay(500);
    canvas.addChild(squares_list[i]);
  }


}
