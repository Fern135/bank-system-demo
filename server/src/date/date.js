class DT {
    constructor() { // starts the Date object to be used in the entire class
        this.d      = new Date();
        this.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        this.days   = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    }

    getDayDate() { // converts a date to a more readable format
        return this.d.toDateString();
    }

    getDayDateISO() { // converts a Date object to a string, using the ISO standard format
        return this.d.toISOString()
    }

    getFullYear() { // returning the full year in 4 digit number
        return this.d.getFullYear();
    }

    getMonth() { // get the month 
        return this.months[this.d.getMonth()];
    }

    getDate() { // returns the day of a date as a number (1-31)
        return this.d.getDate();
    }

    getTime12() { // returning the time in 12 hour format
        return this.d.getHours() % 12 || 12;
    }

    getTime24() { // get the time in 24 hour format
        return this.d.getHours + " : " + this.d.getMinutes() + " : " + this.d.getSeconds();
    }

    getDayOfWeek() { // returns the day of the week
        return this.days[this.d.getDay()];
    }
}

module.exports = DT;
