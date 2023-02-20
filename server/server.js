const express = require('express');
const bodyParser = require('body-parser'); // loading json from the front end

const app = express();

const PORT = process.env.PORT || 3000;

//#region middle-ware
app.use(bodyParser.json());  // using json

//#endregion

//#region list of data needed quickly

//#endregion

/*
    /api/controllers/user/login //<===== for loging
    /api/controllers/user/sign_up //<=== signing up
*/

app.post('/api/controllers/user/sign_up', (request, response) => {
    try{

        const data = request.body; // same as flask data = json.load(request.data)
        
        console.warn(data);
        
        response.sendStatus(200); // sending back status code

    }catch(error){
        console.error(error.toString());
    }
});

app.listen(PORT, () => {
    console.clear();
    console.log(`Listening on port ${PORT}`);
});