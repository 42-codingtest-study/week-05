const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [N, M, R] = input.shift().split(" ").map(Number);

  const graph = Array.from(Array(N + 1), () => []);
  const visited = new Array(N + 1).fill(false);
  for (let str of input) {
    const [a, b] = str.split(" ");
    graph[a].push(b);
    graph[b].push(a);
  }
  graph.forEach((e) => e.sort((a, b) => b - a));
  let cnt = 1;
  const answer = new Array(N).fill(0);

  const dfs = (cur) => {
    visited[cur] = true;
    answer[cur - 1] = cnt++;
    for (let next of graph[cur]) {
      if (visited[next]) continue;

      dfs(+next);
    }
  };
  dfs(R);

  console.log(answer.join("\n"));
}
