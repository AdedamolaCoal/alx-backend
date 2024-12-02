import redis from 'redis';

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

// Function to set a new key-value pair in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the value of a key from Redis
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(result);
  });
};

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
