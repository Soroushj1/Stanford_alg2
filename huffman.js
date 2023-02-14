const fs = require("fs");
const {Heap} = require("heap-js");

// If function uses "this" then it is considered a constructor function.
// It has the power to create objects.
// Objects can be created with "new ClassName" or Object.create(ClassName)
// Look into "prototype". ClassName.prototype.get(){} for example creates a function for all objects.


const BinaryTree = function(value){
    this.value= value;
    this.left = this.right = null;
}

// There is another way of writing object oriented code as below:

// class BinaryTreeNode{
//   constructor(value){
//     this.value = value
//     this.left = this.right = null
//   }
// }


// functions can be written in different ways.
function readTxtFile(string){

  let hashMap = {};
  let array = fs
    .readFileSync(string, "utf8")
    .split("\n")
    .map((elem) => parseInt(elem));
    array = array.slice(1);
    // let array =  ["10", "37", "59", "43", "27", "30", "96", "96", "71", "8", "76"].map((elem)=> parseInt(elem))
    let len = array.length
  array.forEach((key, value) => {
    hashMap[key] = value
  });
  return { array, len, hashMap };
}


// Takes elements of the array, turns them into nodes with value, left, and right attributes
// After that, it adds the elements to a queue.
const huffmanQueue = function(arr,len) {
  let root;
  let queue = [];
  for(let i = 0; i<len; i++){
    let element = new BinaryTree(arr[i]);
    queue.push(element);
  }
  // sort in the order of the values to take the smallest two. This could also be done with a heap data structure
  queue.sort((a,b)=> a.value-b.value);
  // this is where the magic compression happens. 
  while(queue.length>1){
    let a = queue[0];
    queue.shift();
    let b = queue[0];
    queue.shift();
    let ab = new BinaryTree(a.value+b.value);
    ab.left = a;
    ab.right = b;
    queue.push(ab)
    root = ab
    queue.sort((a,b)=> a.value - b.value)
  }

  return root;
}


// Facinating that the function name is different but the recursive function is the same. 

const huffmanPrinter_max =  function printHaufman(root,string){
  let depth;
  if(root == null){
    depth = 0 
  }else if(root.left == null && root.right == null){
    depth = 1
  } else{
    depth = Math.max(printHaufman(root.left, string+"0"), printHaufman(root.right, string+"1"))+1;
  }
  return depth;

}

const huffmanPrinter_min =  function printHaufman(root,string){
  let depth;
  if(root == null){
    depth = 0 
  }else if(root.left == null && root.right == null){
    depth = 1
  } else{
    depth = Math.min(printHaufman(root.left, string+"0"), printHaufman(root.right, string+"1"))+1;
  }
  return depth;

}


let {array, len, hashMap} = readTxtFile("huffman.txt");
let root = huffmanQueue(array, len)
console.log(huffmanPrinter_max(root, "")-1)
console.log(huffmanPrinter_min(root, "")-1)