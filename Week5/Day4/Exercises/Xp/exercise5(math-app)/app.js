import { add, multiply } from './math.js';
import calculate from 'lodash';

const sum = add(8, 12);
const product = multiply(6, 7);

const numbers = [100, 200, 300];
const total = calculate.sum(numbers);

console.log(`8 + 12 = ${sum}`);
console.log(`6 * 7 = ${product}`);
console.log(`Sum of [100, 200, 300] = ${total}`);
