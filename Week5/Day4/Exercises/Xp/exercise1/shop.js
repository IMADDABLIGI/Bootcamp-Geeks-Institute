// import {products} from './products.js';

const products = require('./products.js').products;

// console.log(products);

const verifyProducts = (product) => {
    products.forEach(element => {
        if (element.name.toLowerCase() === product.toLowerCase())
            return console.log("product is in products")
    })
    console.log("Product not in products")
}

verifyProducts("suzuki");
