
import { Client } from 'pg'

const client = new Client({
  user: 'postgres',        // apna username
  host: 'localhost',
  database: 'todo',  // apna database name
  password: 'postgrasql123',    // apna password
  port: 5432,
});

client.connect()
  .then(() => console.log("Connected Successfully ✅"))
  .catch(err => console.error("Connection Error ❌", err));

export default client;