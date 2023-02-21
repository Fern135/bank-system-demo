const fs = require('fs');
const dt = require("../date/date");

class Util{
    constructor(){
        this.chars     = `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-[]"";/.,<>?`;
        this.result    = '';
    }

    /**
     * 
     * @param {length to generate the string} length 
     * @returns random string with length size
     */
    generateRandomString(length) {
        for (let i = 0; i < length; i++) {
            this.result += this.chars.charAt(Math.floor(Math.random() * this.chars.length));
        }
        return this.result;
    }

    /**
     * 
     * @param {where we're writing to} filePath 
     * @param {what we're writing} data 
     */
    writeToFile(filePath, data){
        fs.writeFile(filePath, data, (err) => {
            if (err) {
              console.error(err);
            } else {
              console.log('Data written to file successfully.');
            }
          });
    }

    /**
     * 
     * @param {minimum number to choose} min 
     * @param {maximum number to choose} max 
     * @returns random number between min and max
     */
    getRandomNumber(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    }

    /**
     * 
     * @param {list to choose from} arr 
     * @returns item from list
     */
    randChoice(arr = []) { // choice version from python
        return arr[Math.floor(Math.random() * arr.length)];
    }
    
    /**
     * 
     * @returns random number
     */
    rnd() { 
        return Math.random();
    }

    /**
     * 
     * @param {number to check if it's float} num 
     * @returns bool
     */
    isFloat(num) {
        return Number.isFloat(num);
    }

    /**
     * 
     * @param {number to check if it's int} num 
     * @returns bool
     */
    isInt(num) { 
        return Number.isInteger(num);
    }

    /**
     * 
     * @param {number to check if it's a number} num 
     * @returns bool
     */
    isNumber(num) { 
        return (!isNaN(num) && typeof num === 'number'); 
    }

    isOdd(number) { 
        return number % 2 === 1 ? true : false;
    }

    /**
     * 
     * @param {to check if even} number 
     * @returns bool
     */
    isEven(number) {
        return number % 2 == 0;
    }

    /**
     * 
     * @param {to check if string or not} str 
     * @returns bool
     */
    isString(str) {
        return typeof str === 'string' || str instanceof String;
    }

    /**
     * 
     * @param {to check if object or not} val 
     * @returns bool
     */
    isObject(val) {
        return val instanceof Object;
    }

    /**
     * 
     * @param {check if it's array} myARR 
     * @returns bool
     */
    isArray(myARR) { 
        return myARR.constructor === Array;
    }

    /**
     * 
     * @param {check if it's a form of date} myDate 
     * @returns bool
     */
    isDate(myDate) { 
        return myDate.constructor === Date;
    }

    /**
     * 
     * @param {if data is empty} data 
     * @returns bool
     */
    isEmpty(data) { 
        return !data.trim().length;
    }

    /**
     * 
     * @param {data being measured} data 
     * @returns bool
     */
    len(data) { 
        return parseInt(data.length);
    }

    /**
     * 
     * @param {to turn into interger} data 
     * @returns data as int
     */
    turnInt(data) { 
        return parseInt(data);
    }

    /**
     * 
     * @param {to turn into uppercase} str 
     * @returns str as uppercase
     */
    uperCase(str) { 
        return str.toUpperCase();
    }

    /**
     * 
     * @param {to turn into lowerCase} str 
     * @returns str as lowerCase
     */
    lowerCase(str) { 
        return str.toLowerCase();
    }

    /**
     * 
     * @param {to turn into string} data 
     * @returns data as string
     */
    toString(data) { 
        return data.toString();
    }

    /**
     * 
     * @param {to trim the edges} str 
     * @returns str with no empty areas
     */
    trim(str) { 
        return str.trim();
    }

    /**
     * 
     * @param {to check if it's json or not} data 
     * @returns bool
     */
    isJson(data) { 
        try {
            JSON.parse(data);
        } catch (e) {
            return false;
        }
        return true;
    }

    /**
     * 
     * @param {to turn into json} data 
     * @returns data as json
     */
    jsonify(data) { 
        return JSON.parse(data);
    }

    /**
     * 
     * @param {main string} main_string 
     * @param {which word we're replacing} rep_word 
     * @param {word we're replacing rep_word with} rep_with 
     * @returns main_string with rep_with instead of rep_word
     */
    replaceWord(main_string, rep_word, rep_with) { 
        return main_string.replace(rep_word, rep_with);
    }

    /**
     * 
     * @param {main string} str 
     * @param {word we searching} searchWord 
     * @returns bool
     */
    strSearch(str, searchWord) { 
        return str.search(searchWord);
    }

    /**
     * 
     * @param {main string} str 
     * @param {what we search} val 
     * @returns bool
     */
    hasVal(str, val) { 
        return str.includes(val);
    }

    /**
     * 
     * @param {email we're checking} mail 
     * @returns bool
     */
    ValidateEmail(mail) { 
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
            return true
        }
        return false
    }

    /**
     * 
     * @param {time to wait} ms 
     * @returns promise aka the time waiting
     */
    Sleep(ms) { 
        return new Promise(resolve => setTimeout(resolve, ms));
    }

}

module.exports = Util;