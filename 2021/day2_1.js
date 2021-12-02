"use strict";
debugger;

let input = document.body.textContent.split('\n');
input.pop();

let subPos = {
	horiz: 0,
	depth: 0
};

for (let i in input) {
	let command = input[i].split(' ');
	switch(command[0]) {
		case 'forward':
			subPos.horiz += parseInt(command[1]);  break;
		case 'down':
			subPos.depth += parseInt(command[1]);  break;
		case 'up':
			subPos.depth -= parseInt(command[1]);  break;
	}
}

console.log(`The final position is: Horizontal: ${subPos.horiz}, Depth: ${subPos.depth}.  Final answer: ${subPos.horiz * subPos.depth}.`);