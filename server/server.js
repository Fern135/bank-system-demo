const express       = require('express');//<================= using node express
const bodyParser    = require('body-parser'); //<============ loading json from the front end
const Database      = require("./src/db/db"); //<============ connecting to local db
const Email         = require("./src/email/email")//<======== sending email
const Encryption    = require("./src/encrypt/encrypt");//<=== encryption functionality


const app = express();


//#region middle-ware
require('dotenv').config();  // getting data from .env files
app.use(bodyParser.json());  // using json
//#endregion

//#region constants
const PORT          = process.env.PORT || 3000;
const emailUserName = process.env.emailUserName;
const emailPassword = process.env.emailPassword;
const secretKey     = process.env.secret_key;
//#endregion

//#region classes used
const db    = new Database(); /* get, all methods need await example: const rows = await db.all(sql); */
const email = new Email(emailUserName, emailPassword);
const enc   = new Encryption(secretKey);
//#endregion

/*
    email usage
    const to = 'recipient-email@example.com';
    const subject = 'Test Email';
    const templateName = 'welcome';
    const templateData = { name: 'John' };
    email.sendEmail(to, subject, templateName, templateData);
*/

/*
    /api/controllers/user/login //<===== for loging
    /api/controllers/user/sign_up //<=== signing up
*/

app.post('/api/controllers/user/sign_up', async (request, response) => {
    try{

        const data = request.body; // same as flask data = json.load(request.data)
        
        console.warn(data['user_name']);
        
        response.sendStatus(200); // sending back status code

    }catch(error){
        console.error(error.toString());
        response.sendStatus(500);
    }
});

app.post('/api/controllers/user/login', async (request, response) => {
    try{

        const data = request.body; // same as flask data = json.load(request.data)
        
        console.warn(data);
        
        response.sendStatus(200); // sending back status code

    }catch(error){
        console.error(error.toString());
        response.sendStatus(500);
    }
});

app.listen(PORT, () => {
    db.runSqlScriptFile("../server/src/db/sql/banking.sql");
    console.clear();
    console.log(`Listening on port ${PORT}`);
});