/*
\ o /
 \|/
  |
 / \
weeeee!!!!!

I'm bad as ascii art...
*/
const readline = require('readline');
const table = require('./json/periodic-table.json');

const readInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(query) {
  return new Promise((resolve, reject) => {
    try {
      readInterface.question(query, resolve);
    }
    catch(err) {
      reject(err);
    }
  });
}

function availability(checkList, checkSet) {
  return checkList.map((el) => checkSet.has(el))
}

function processName(name) {
  let singles = Array.from(name).map((char) => char.toLowerCase())
  let doubles = singles.map((char, i) => singles[i] + singles[i + 1])
  // the last character gets joined to undefined, so drop that...
  doubles = doubles.splice(0, doubles.length - 1)
  return {singles, doubles};
}

function gobots({singles, doubles}) {
  console.log(singles, doubles)
}

const main = () => {
  const symbolSet = new Set(table.elements.map((e) => e.symbol.toLowerCase()));
  question('What name should I check?\n>')
    .then(name => processName(name))
    .then(gobots)
    .then(() => readInterface.close());

}

main()
