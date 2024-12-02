import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Promisify Redis commands
const getAsync = promisify(client.get).bind(client);

// Function to display the value of "School" key
const displaySchoolValue = async () => {
  try {
    const value = await getAsync('School');
    console.log(value);
  } catch (error) {
    console.error(error);
  }
};

// Set and get values in Redis
client.set('School', 'Holberton', redis.print);
displaySchoolValue();
client.set('School', '100', redis.print);
displaySchoolValue();
