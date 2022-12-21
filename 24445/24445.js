const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [N, M, R] = input.shift().split(" ").map(Number);

  const graph = Array.from(Array(N + 1), () => []);
  const visited = Array(N + 1).fill(0);

  for (let str of input) {
    const [a, b] = str.split(" ");
    graph[a].push(b);
    graph[b].push(a);
  }
  graph.forEach((e) => e.sort((a, b) => b - a));
  //   console.log(graph);
  const answer = new Array(N).fill(0);

  visited[R] = 1;
  cnt = 2;
  const queue = [R];

  const bfs = (cur) => {
    while (queue.length > 0) {
      let cur = queue.shift();

      for (let i of graph[cur]) {
        if (visited[i] === 0) {
          queue.push(i);
          visited[i] = cnt;
          cnt++;
        }
      }
    }
  };

  bfs(R);
  visited.splice(0, 1);
  console.log(visited.join("\n"));
}
