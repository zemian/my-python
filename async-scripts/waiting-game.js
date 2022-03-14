// JavaScript version of explaining Event and Wait process
// https://stackoverflow.com/questions/68139555/difference-between-async-await-in-python-vs-javascript

// This async function will resolve
// after the number of ms provided has passed
const wait = (ms) => {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function main() {
  console.log(2)
  await wait(100)
  console.log(4)
}

console.log(1)
main()
console.log(3)