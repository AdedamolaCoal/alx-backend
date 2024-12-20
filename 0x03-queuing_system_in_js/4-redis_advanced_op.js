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

// Store hash values using hset
const setHashValues = () => {
  client.hset('HolbertonSchools', 'Portland', '50', redis.print);
  client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
  client.hset('HolbertonSchools', 'New York', '20', redis.print);
  client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
  client.hset('HolbertonSchools', 'Cali', '40', redis.print);
  client.hset('HolbertonSchools', 'Paris', '2', redis.print);
};

// Display the hash values using hgetall
const displayHashValues = () => {
  client.hgetall('HolbertonSchools', (err, object) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(object);
  });
};

// Call the functions
setHashValues();
displayHashValues();
