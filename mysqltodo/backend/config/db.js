
// import mysql from 'mysql2/promise';

// const dbConfig = {
//   host: 'localhost',
//   user: 'root',
//   password: 'admin',
//   database: 'todo_db',
//   port : 3306,
//   waitForConnections: true,
//   connectionLimit: 10,
//   queueLimit: 0
// };

// const pool = mysql.createPool(dbConfig);
// // console.log('Database connection pool created.' pool);
// export default pool;

import mysql from 'mysql2/promise';

const pool = mysql.createPool({
  host: 'localhost',      // ya jo host Workbench me use ho raha hai
  port: 3306,             // Workbench me jo port hai wahi use karo
  user: 'root',           // aapka MySQL user
  password: 'admin',      // aapka MySQL password
  database: 'todo_app',    // exact database name
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

export default pool;
