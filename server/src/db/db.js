const sqlite3 = require('sqlite3').verbose();


class Database {
  /**
   * 
   * @param { database name } db_name 
   */
  constructor(db_name="bankingDefault") {
    try{
      this.db = new sqlite3.Database(`./${db_name}.db`, (err) => {
        if (err) {
          console.error(err.message);
            
        } else {
          // this.createDb();
          // this.createTable();
          console.info('Connected to the database.');

        }
      });

    }catch(err){
      console.error(`error in db: ${err.toString()}`);
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
    this.db.close((err) => {
      if (err) {
        console.error(err.message);
      } else {
        console.log('Closed the database connection.');
      }
    });
  }
}

module.exports = Database;