import redis from 'redis';

// Create Redis client
const subscriber = redis.createClient();

// On successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// On error
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(message);

  // Unsubscribe and quit on KILL_SERVER message
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  }
});
