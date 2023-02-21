const sqlite3 = require('sqlite3').verbose();
const fs      = require('fs');
const util    = require("../util/util");
const DT      = require("../date/date");

// const date = new DT(); // DT not a constructor? what? 

class Database extends util {
  /**
   * 
   * @param { database name } db_name 
   */
  constructor(db_name="bankingDefault") {
    try{
      super(util);
      this.db = new sqlite3.Database(`./${db_name}.db`, (err) => {
        if (err) {
          console.error(err.message);
            
        } else {
          // this.createDb();
          // this.createTable();
          console.info('Connected to the database.');

        }
      });

    }catch(error){
      console.error(`error in db: ${this.toString(error)}`);
    }
  }

  /**
   * 
   * @param {where the sql file is located to run} scriptFilePath 
   */
  runSqlScriptFile(scriptFilePath) {
    try{
      const script = fs.readFileSync(scriptFilePath, 'utf8');
      this.db.exec(script, function (err) {
        if (err) {
          console.error('Error running script:', err);
        } else {
          console.log('Script executed successfully');
        }
      });

    }catch(error){
      console.error(super.toString(error));
      
      //TODO: Not important but get this working at one point in time
      const err = `\n${DT.getTime12()} | ${DT.getDayOfWeek()} |\n
      ${DT.getMonth()} / ${DT.getDate()} / ${DT.getFullYear()}|\n
      ${super.toString(error)}`;
      super.writeToFile("./log/", err);
    }
  }

  /**
   * 
   * @param { sql } sql 
   * @param { const row = await db.get('SELECT * FROM users WHERE id = ?', [id]); } params 
   * @returns promise <any> 
   */
  run(sql, params = []) {
    return new Promise((resolve, reject) => {
      this.db.run(sql, params, function (err) {
        if (err) {
          console.error(err.message);
          reject(err);

        } else {
          resolve({ id: this.lastID });

        }
      });
    });
  }

  /**
   * 
   * @param { sql } sql 
   * @param { const row = await db.get('SELECT * FROM users WHERE id = ?', [id]); } params 
   * @returns promise <any> 
  */
  async get(sql, params = []) {
    return new Promise((resolve, reject) => {
      this.db.get(sql, params, (err, row) => {
        if (err) {
          console.error(err.message);
          reject(err);
        } else {
          resolve(row);
        }
      });
    });
  }

  /**
   * 
   * @param { sql } sql 
   * @param { const row = await db.get('SELECT * FROM users WHERE id = ?', [id]); } params 
   * @returns promise <any> 
  */
  async all(sql, params = []) {
    return new Promise((resolve, reject) => {
      this.db.all(sql, params, (err, rows) => {
        if (err) {
          console.error(err.message);
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  /**
   * close the connection
   */
  close() {
    try{
      this.db.close((err) => {
        if (err) {
          console.error(err.message);
        } else {
          console.log('Closed the database connection.');
        }
      });
    }catch(error){
      console.error(this.toString(error));
    }
  }
}

module.exports = Database;