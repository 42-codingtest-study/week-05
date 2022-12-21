const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let N = input[0].split(" ")[0] * 1;
  let M = input[0].split(" ")[1] * 1;
  let V = input[0].split(" ")[2];

  const graph = new Object();
  for (let i = 1; i <= N; i++) {
    graph[i] = [];
  }

  for (let i = 1; i <= M; i++) {
    const a = input[i].split(" ")[0];
    const b = input[i].split(" ")[1];

    graph[a].push(b);
    graph[b].push(a);
  }
  //   console.log(graph);

  const dfs = (graph, start) => {
    const checked = [];
    const willcheck = [];

    willcheck.push(start);

    while (willcheck.length) {
      const node = willcheck.pop();
      if (!checked.includes(node)) {
        checked.push(node);
        willcheck.push(...graph[node].sort((a, b) => a - b).reverse());
      }
    }
    return checked;
  };

  const bfs = (graph, start) => {
    const checked = [];
    const willcheck = [];

    willcheck.push(start);

    while (willcheck.length) {
      const node = willcheck.shift();
      if (!checked.includes(node)) {
        checked.push(node);
        willcheck.push(...graph[node].sort((a, b) => a - b));
      }
    }
    return checked;
  };
  console.log(dfs(graph, V).join(" "));
  console.log(bfs(graph, V).join(" "));
}
