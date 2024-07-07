console.log("New Array implementation");

class CustomArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  getItem(index) {
    return this.data[index];
  }

  getAllItems() {
    return this.data;
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    if (this.length >= 1) {
      delete this.data[this.length - 1];
      this.length--;
    } else {
      console.log("No Items in the array");
    }
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }

    delete this.data[this.length - 1];
    this.length--;
  }

  unshiftItems(index, data) {
    this.length++;

    for (let i = this.length - 1; i > index; i--) {
      console.log("the i", i);
      this.data[i] = this.data[i - 1];
    }

    this.data[index] = data;
  }
}

const newArr = new CustomArray();

newArr.push("This is first test");
newArr.push("This is second test");
newArr.push("This is third test");
newArr.push("This is fourth test");
newArr.push("This is fifth test");

console.log("New Array ", newArr);

newArr.unshiftItems(0, "This is zeroth test");

newArr.pop();

console.log("New Array delete ", newArr);
