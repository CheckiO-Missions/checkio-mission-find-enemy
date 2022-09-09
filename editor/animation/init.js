//Dont change it
requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function findEnemyCanvas(dom, dataInp, dataExp) {
            var color = {
                'dark': {
                    'blue': "#294270",
                    'orange': "#F0801A",
                },
                'light': {
                    'blue': "#8FC7ED",
                    'orange': "#FABA00",
                },
            };
            var cellSize = 40;
            var attr = {
                'cell': {
                    'normal': {
                        "stroke": color.dark.blue,
                        "stroke-width": 1,
                        "fill": color.light.blue
                    },
                    'arc': {
                        "stroke": color.dark.blue,
                        "stroke-width": 1,
                        "fill": color.light.orange
                    },
                    'marked': {
                        "stroke": color.dark.blue,
                        "stroke-width": 1,
                        "fill": color.dark.orange
                    },
                },
                'arrow': {
                    "stroke": color.dark.blue,
                    "stroke-width": 1,
                    "fill": color.dark.blue
                },
                'text': {
                    "font-family": "Roboto, Arial, serif",
                    "font-size": 1.4 * cellSize / 4,
                    "stroke": color.dark.blue
                }
            };
            var zx = 10;
            var zy = 0;
            var defaultmap = [];
            for(var r=1; r<=9; r+=1) {
                var [r1, r2] = [[], []];
                for(var i=65; i<=90; i+=1) {
                    var c = String.fromCharCode(i);
                    if (i%2){
                        r1.push(c+r);
                    } else {
                        r2.push(c+r);
                    }
                }
                defaultmap.push(r1);
                defaultmap.push(r2);
            }
            var arrow_co = [];
            var [you, dir, enemy] = dataInp;

            function hexagon(canvas, x0, y0, radius, hn) {
                var path = "";
                for (var i = 0; i <= 6; i++) {
                    var a = i * 60;
                    var x = radius * Math.cos(a * Math.PI / 180);
                    var y = radius * Math.sin(a * Math.PI / 180);
                    path +=
                        (i == 0 ? "M": "L") + (x + x0) + "," + (y + y0);
                    if (hn === you) {
                        var ax = (radius-8)*Math.cos(a * Math.PI/180);
                        var ay = (radius-8)*Math.sin(a * Math.PI/180);
                        arrow_co.push({'x': ax + x0, 'y': ay + y0});
                    }
                }
                path += "Z";
                return canvas.path(path);
            }

            //draw
            var m1 = you.charCodeAt(0);
            var m2 = enemy.charCodeAt(0);
            var col = Math.ceil((Math.max(m1, m2) - 64) / 2);
            var paper = Raphael(dom, 
                (cellSize-5) * col * 2,
                (cellSize-5) * 10,
                0, 0);
            for (var i=0; i < 18; i+=1) {
                for (var j=0; j < col; j+=1) {
                    var hn = defaultmap[i][j];
                    var cx = zx + 1.5 * cellSize * j 
                        + cellSize / 2
                        + (i % 2 ? 3 * cellSize / 4 : 0);
                    var cy = (i + 1) * cellSize
                        * Math.sin(Math.PI / 3) / 2 - zy;
                    var attrHex = attr.cell.normal;
                    if (dataExp && dataExp[hn[0]]
                        && dataExp[hn[0]][0] <= hn[1]
                        && dataExp[hn[0]][1] >= hn[1]) {
                        attrHex = attr.cell.arc;
                    }
                    if ([you, enemy].indexOf(hn) > -1) {
                        attrHex = attr.cell.marked;
                    }
                    hexagon(paper, cx, cy, cellSize/2,hn).attr(attrHex);
                    paper.text(cx, cy, hn !== you ? hn: '').attr(attr.text);
                }
            }

            //arrow
            var dir_num = ['N','NE','SE','S','SW', 'NW'].indexOf(dir);
            var [a, b, c, d] =
                [(dir_num + 1) % 6, (dir_num + 2) % 6,
                 (dir_num + 4) % 6, (dir_num + 5) % 6];
            var path = 'M'
                + arrow_co[a].x + ',' + arrow_co[a].y
                + 'L' + arrow_co[b].x + ',' + arrow_co[b].y
                + 'L'
                + (arrow_co[c].x + (arrow_co[d].x - arrow_co[c].x) / 2)
                + ','
                + (arrow_co[c].y + (arrow_co[d].y - arrow_co[c].y) / 2)
                + 'Z';
            paper.path(path).attr(attr.arrow);
        }
        
        var $tryit;

        var io = new extIO({
            animation: function($expl, data){
                findEnemyCanvas(
                    $expl[0],
                    data.in,
                    data.ext.explanation ? data.ext.explanation : {});
            }
        });
        io.start();
    }
);
